package br.com.caelum.ed.vetores;

public class TesteContemAluno {
	public static void main(String[] args) {
		Aluno a1 = new Aluno();
		Aluno a2 = new Aluno();
		Aluno aluno = new Aluno();
		
		a1.setNome("Rafael");
		a2.setNome("Paulo");
		aluno.setNome("Ana");
		
		Vetor lista = new Vetor();
		
		lista.adiciona(a1);
		lista.adiciona(a2);
		
		System.out.println(lista.contem(a1));
		System.out.println(lista.contem(a2));
		System.out.println(lista.contem(aluno));
	}
}
