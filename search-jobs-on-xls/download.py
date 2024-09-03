import os

import httpx
from consts import XLSX_ORIGIN_URL, XLSX_FILE
from logger import get_logger

logger = get_logger.use()


def get_spredsheet():
    response = httpx.get(
        XLSX_ORIGIN_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        },
        follow_redirects=True
    )

    with open(XLSX_FILE, "wb") as file:
        if os.path.isfile(XLSX_FILE):
            file.truncate(0)

        file.write(response.content)


if __name__ == "__main__":
    get_spredsheet()
