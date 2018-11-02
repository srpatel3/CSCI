public class Node{
  public Node leftNode;
  public Node rightNode;
  public int data;

  public Node(int data){
    this.data = data;
  }


  public void addNode(int data){
    if(data > this.data){
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
  }


  public void printBST(){
    // System.out.println("I am hgere");
    if(this.leftNode != null){
      this.leftNode.printBST();
    }
    System.out.print(this.data+ " ");
    if(this.rightNode!=null){
      this.rightNode.printBST();
    }
  }

}
