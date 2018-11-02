public class LinkedList{
  public Node head;

  public LinkedList(Node n){
    this.head = n;
  }

  public LinkedList(){
    this.head = null;
  }

  public void add(int data){
    // System.out.println("Error Here...");
    if(this.head == null){
      this.head = new Node(data);
      this.printList();
      return;
    }
    Node currentNode = this.head;
    while(currentNode.next != null){
      currentNode = currentNode.next;
    }
    currentNode.next = new Node(data);
    this.printList();
  }



  public void deleteElement(int key){
    Node currentNode = this.head;
    Node prevNode = this.head;
    if(this.head.data == key){
      this.head = this.head.next;
      System.out.println("Item Deleted...");
      this.printList();
      return;
    }
    while(currentNode.next != null){
      if(currentNode.data == key){
        prevNode.next = currentNode.next;
        System.out.println("Item Deleted...");
        this.printList();
        return;
      }
      prevNode = currentNode;
      currentNode = currentNode.next;
    }
    if(currentNode.data == key){
      prevNode.next = null;
      System.out.println("Item Deleted...");
      this.printList();
    }

  }
  public void printList(){
    Node currentNode = this.head;

    while(currentNode.next != null){
      System.out.print(currentNode.data + " ");
      currentNode = currentNode.next;
    }
    System.out.print(currentNode.data);
    System.out.println();
  }




}
