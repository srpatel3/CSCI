import java.util.*;

public class Trie{
	public Node root;

	//Constructor	
	public Trie(){
		this.root = new Node();
	}


	//To insert a String in Trie

	public void insertString(String Key){
		int length = Key.length();
		int count = 0;
		int indexToAdd = 0;
		Node currentNode = this.root;
	
		for (count = 0; count < length; count++){
			indexToAdd = Key.charAt(count) - 'a';
			System.out.println(indexToAdd);
			if(currentNode.children[indexToAdd] == null)
				currentNode.children[indexToAdd] = new Node(Key.charAt(count));
			currentNode = currentNode.children[indexToAdd];
		}

		currentNode.isWord = true;
	}


	//Searching Element
	public boolean search(String Key){
		int count = 0;
		int indexToCheck = 0;
		Node currentNode = this.root;
		for(int i = 0; i < Key.length();i++){
			indexToCheck = Key.charAt(i) - 'a';
			if(currentNode.children[indexToCheck] == null)
				return false;
			currentNode = currentNode.children[indexToCheck];
		}
		return (currentNode != null && currentNode.isWord == true);
	}
}
