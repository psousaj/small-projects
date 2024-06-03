package br.com.caelum.ed.vetores;

public class Vetor4 {

	private Object [] objetos = new Object[100];
	private Aluno [] alunos = new Aluno [10000];
	
	private int totalDeObjetos = 0;
	
	public void adiciona(Aluno aluno) {
		this.garantaEspaco();
		for (int i = 0; i < this.alunos.length; i++) {
			if (this.alunos[i] == null) {
				this.alunos[i] = aluno;
				break;
			}
		}
	}
	
	private boolean posicaoValida(int posicao) {
		return posicao >= 0 && posicao <= this.totalDeObjetos;
	}
	
	public void adiciona (int posicao, Aluno aluno) {
		this.garantaEspaco();
		if (!this.posicaoValida(posicao)) {
			throw new IllegalArgumentException("Posição inválida");
		} 
		
		for (int i = this.totalDeObjetos - 1; i >= posicao; i-=1) {
			this.objetos[i + 1] = this.objetos[i];
		}
		
		this.objetos[posicao] = aluno;
		this.totalDeObjetos++;
	}
	
//	private boolean posicaoOcupada(int posicao) {
//		return posicao >= 0 && posicao < this.totalDeObjetos;
//	}
	
	public Object pega (int posicao) {
		return this.alunos[posicao];
	}
	
	public void remove (int posicao) {
		if (!this.posicaoValida(posicao)) {
			throw new IllegalArgumentException("Posição inválida");
		} 
		
		for (int i = posicao; i < this.totalDeObjetos - 1; i++) {
			this.objetos[i] = this.objetos[i + 1];
		}
		this.totalDeObjetos--;
	}
	
	
	public boolean contem(Aluno aluno) {
		for (int i = 0; i < this.alunos.length; i++) {
			if (aluno == this.alunos[i]); {
				return true;
			}
 		}
		return false;
	}
	
	public int tamanhoInt () {
		return this.totalDeObjetos;
	}
	
	public void tamanho () {
		System.out.printf("O tamanho da lista e: %s\n", this.totalDeObjetos);
	}
	
	public String toString() {
		if (this.totalDeObjetos == 0) {
			return "[]";
		}
		
		StringBuilder builder = new StringBuilder();
		builder.append("[");
		
		for (int i = 0; i < this.totalDeObjetos -1; i++) {
			builder.append(this.objetos[i]);
			builder.append(", ");
		}
		builder.append(this.objetos[this.totalDeObjetos - 1]);
		builder.append("]");
		
		return builder.toString();
	}
	
	private void garantaEspaco() {
		if (this.totalDeObjetos == this.objetos.length) {
			Aluno [] novaArray = new Aluno[this.objetos.length*2];
			for (int i = 0; i < this.alunos.length; i++) {
				novaArray[i] = this.alunos[i];
			}
			this.objetos = novaArray;
		}
	}
}
