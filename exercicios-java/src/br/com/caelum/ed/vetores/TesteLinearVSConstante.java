package br.com.caelum.ed.vetores;

public class TesteLinearVSConstante {
	public static void main(String[] args) {
//		Vetor4 vetor4 = new Vetor4();
		Vetor vetor =  new Vetor();
		
		long inicio = System.currentTimeMillis();
		
//		for (int i = 1; i < 100000; i++) {  
//			Aluno aluno = new Aluno();
//			vetor4.adiciona(aluno);
//		} 
		
		
		//Diferença de quase 2.5 segundos
		
		for (int i = 1; i < 100000; i++) {
			Aluno aluno = new Aluno();
			vetor.adiciona(aluno);
		}
		
		long fim = System.currentTimeMillis();
		long fim4 = System.currentTimeMillis();
		
		double tempo4 = (fim4 - inicio) / 1000.0;
		double tempo = (fim - inicio) / 1000.0;
		
		System.out.println("Tempo em segundos usando 'for' questao 4: "+tempo4);
		System.out.println("Tempo em segundos: "+tempo);
	}
}
