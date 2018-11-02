public class BST{
  // public Node rootNode;
  public Node leftNode;
  public Node rightNode;
  public int data;

  // public BST(int data){
  //   this.data = data;
  // }
  // public Node(int data){
  //   this.data = data;
  // }

  public void addNode(int data){
    if(data < this.data){
      if(this.leftNode == null){
        this.leftNode = new Node(data);
        return;
      }
      else{
        this.leftNode.addNode(data);
      }
    }
    else{
      if(this.rightNode == null){
        this.rightNode = new Node(data);
        return;
      }
      else{
        this.rightNode.addNode(data);
      }
    }
    this.printBST();
  }


  public void printBST(){
    if(this.leftNode != null){
      this.leftNOde.printBST();
    }
    System.out.print(this.data+ " ");
    if(this.rightNode!=null){
      this.rightNode.printBST();
    }
  }
}
