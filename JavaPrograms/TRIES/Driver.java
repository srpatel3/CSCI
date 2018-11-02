import java.util.Scanner;

class Driver{
	public static void main(String[] args){
		Trie TR = new Trie();
		TR.insertString("shirish");
		TR.insertString("patel");
		if (TR.search("patel"))
			System.out.println("Yes it is here");
		else
			System.out.println("NOpe not here");

		if (TR.search("shirishpatel")){
			System.out.println("Yes it is there");
		}		
		else{
			System.out.println("It is not there");
		}
	}
}
