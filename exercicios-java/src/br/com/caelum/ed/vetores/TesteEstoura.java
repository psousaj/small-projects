package br.com.caelum.ed.vetores;

public class TesteEstoura {
	public static void main(String[] args) {
		Vetor4 vetor = new Vetor4();
		
		for (int i = 0; i < 1000001; i++) {
			Aluno aluno = new Aluno();
			vetor.adiciona(aluno);
		}
	}
}
