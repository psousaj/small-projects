package br.com.caelum.ed.vetores;

public class TesteTamanhoLista {
	public static void main(String[] args) {
		Aluno a1 = new Aluno();
		Aluno a2 = new Aluno();
		Aluno a3 = new Aluno();

		a1.setNome("Rafael");
		a2.setNome("Paulo");
		
		Vetor lista = new Vetor();
		
		lista.adiciona(a1);
		lista.adiciona(a2);
		
		lista.tamanho();
		
		lista.adiciona(a3);
		
		lista.tamanho();
	}
}
