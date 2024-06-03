package br.com.caelum.ed.vetores;

public class TestedeTempoDoContem {
	public static void main(String[] args) {
		Vetor vetor = new Vetor();
//		Vetor4 vetor4 =  new Vetor4();
		long inicio = System.currentTimeMillis();
		
		for (int i = 0; i < 30000; i++) {
			Aluno aluno =  new Aluno();
			if (!vetor.contem(aluno)) {
				System.out.println("Erro: Aluno "
						+aluno+" não foi adicionado");
			}
		}
		
		for (int i = 0; i < 30000; i++) {
			Aluno  aluno = new Aluno();
			if (vetor.contem(aluno)) {
				System.out.println("Erro: Aluno "
						+aluno+" foi adicionado");
			}
		}
//		//			///			///			///			///			///
//		for (int i = 0; i < 30000; i++) {
//			Aluno aluno =  new Aluno();
//			if (!vetor4.contem(aluno)) {
//				System.out.println("Erro: Aluno "
//						+aluno+" não foi adicionado");
//			}
//		}
//		
//		for (int i = 0; i < 30000; i++) {
//			Aluno  aluno = new Aluno();
//			if (vetor4.contem(aluno)) {
//				System.out.println("Erro: Aluno "
//						+aluno+" foi adicionado");
//			}
//		}
//		///			///			///			///			///			///
		long fim = System.currentTimeMillis();
		double tempo = (fim - inicio) / 1000.0;
		System.out.println("Tempo: "+tempo);
	}
}
