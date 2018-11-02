public class Node{
	char C;
	Node[] children;
	boolean isWord;
	
	public Node(){
		this.C = ' ';
		this.children = new Node[26];
		this.isWord = false;
	}
	//Constructor
	public Node(char c){
		this.C = c;
		this.children = new Node[26];
		this.isWord = false;
	}

	//Insert String in Trie

	//public insertString(String key){
			
	//}

}
