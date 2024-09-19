import httpx
import random
import asyncio
import pandas as pd
from tqdm import tqdm
from urllib.parse import urlparse

from settings.logger import logger


def filter_planilha1(df: pd.DataFrame, bound_sim_requests=15):

    # Usar tqdm para a barra de progresso com asyncio
    # Para isso, precisamos criar uma função wrapper para tqdm e asyncio
    async def process_links_with_progress(links):
        with tqdm(total=len(links), desc="Processando Links") as pbar:
            redirected_links = []

            async with httpx.AsyncClient(follow_redirects=True) as client:
                sem = asyncio.Semaphore(bound_sim_requests)

                async def bound_follow_redirect(link):
                    async with sem:
                        result = await follow_redirect_to_return_correct_url(
                            link, client
                        )
                        pbar.update(1)
                        return result

                tasks = [bound_follow_redirect(link) for link in links]
                redirected_links = await asyncio.gather(*tasks)

            return redirected_links

    async def follow_redirect_to_return_correct_url(link, client) -> str:
        parsed_url = urlparse(link)
        if not parsed_url.scheme:
            link = "http://" + link

        retries = 3
        for attempt in range(retries):
            try:
                response = await client.get(link, timeout=30.0)
                return response.url
            except httpx.ReadTimeout as e:
                logger.warning(
                    f"ReadTimeout ao acessar o link {link}. Tentativa {attempt + 1} de {retries}."
                )
                await asyncio.sleep(
                    random.uniform(1, 3)
                )  # Espera aleatória entre 1 e 3 segundos
            except httpx.RequestError as e:
                logger.error(f"Erro ao acessar o link {link}: {e}")
                return link

        logger.error(f"Falha ao acessar o link {link} após {retries} tentativas.")
        logger.info("Retornando com link original")
        return link

    df = df.drop(index=[0, 1]).reset_index(drop=True)
    df = df[df[["Localidade", "Uf"]].isna().any(axis=1)]
    df["Localidade"] = df["Localidade"].fillna("").astype(str)
    df["Localidade"] = df["Localidade"].map(
        lambda localidade: (
            "REMOTO" if not localidade or localidade == "" else localidade
        )
    )

    links = df["Link"].tolist()
    logger.info(f"Processando {len(links)} links do Jornada Tech.")

    redirected_links = asyncio.run(process_links_with_progress(links))

    df["Link"] = redirected_links

    logger.info("Processamento concluído. Dados prontos para mesclagem.")

    return df


def filter_planilha2(df):
    df = df.drop(index=0).reset_index(drop=True)
    df = df[df["Localidade"].str.lower() == "remoto"]

    return df
