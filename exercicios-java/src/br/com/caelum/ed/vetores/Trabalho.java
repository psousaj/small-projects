package br.com.caelum.ed.vetores;

import br.com.caelum.ed.vetores.Vetor;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

public class Trabalho {
	public static void main(String[] args) {
		Vetor lista = new Vetor();
		Vetor novaLista = new Vetor();
		List<Aluno> listaVector = new Vector<>();
		ArrayList<Aluno> listaArrayList = new ArrayList<Aluno>();		

		double quantidade = 1000; //seta quantidade de alunos em cada vetor 
		
		System.out.println("---------------------------");
		lista.tamanho();
		
		for (int i = 0; i < quantidade; i++) {
			Aluno aluno = new Aluno();
			lista.adiciona(aluno);
		}
		
		Aluno aluno1 = (Aluno) lista.pega(0); //define nome do objeto tipo Aluno do Vetor (lista) na posição 0
		aluno1.setNome("Jose Teste");
		
		lista.tamanho();
		
		System.out.println("\nAluno posicao 0: "+lista.pega(0)); //imprime o objeto que foi setado o nome no Vetor (lista)
		System.out.println("---------------------------");
		
//		///			///			///			///			///			///			///
		
		novaLista.tamanho();
		
		for (int i = 0; i < quantidade; i++) {
			novaLista.adiciona(lista.pega(i));
		}
		
		novaLista.tamanho();
		
		System.out.print("---------------------------");
		
//		///			///			///			///			///			///			///
	
		System.out.printf("\nO tamanho do vector e: %s\n", listaVector.size());
		
		for (int i = 0; i < quantidade; i++) {
			Aluno aluno = (Aluno) novaLista.pega(i);
			listaVector.add(aluno);
		}
		
		System.out.printf("O tamanho do vector agora e: %s\n", listaVector.size());
		System.out.println("\nAluno posicao 0: "+listaVector.get(0)); //Verifica se o objeto que foi passado para o novo Vetor 
		                                                             //é o mesmo setado antes "Jose Teste"
		
		System.out.println("---------------------------");
		
//		///			///			///			///			///			///			///
		
		System.out.printf("O tamanho do ArrayList e: %s", listaArrayList.size());
		
		for (int i = 0; i < quantidade; i++) {
			Aluno aluno = (Aluno) listaVector.get(i);
			listaArrayList.add(aluno);
		}
		
		System.out.printf("\nO tamanho do ArrayList agora e: %s", listaArrayList.size());
		System.out.println("\n\nAluno posicao 0: "+listaArrayList.get(0));
		
		System.out.println("---------------------------");
		
	}
	
}
