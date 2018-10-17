
public class LinkedList{
    public Node head;
    public LinkedList(){
        this.head = null;
    }

    public void addNode(int data){
        if (this.head == null){
            System.out.println("Hi");
            this.head = new Node(data);
            return;
        }
        Node current = this.head;
        while(current.next != null){
            current = current.next;
        }
        current.next = new Node(data);
    }

    public void printList(){
        Node currentNode = head;
        System.out.println("\n\n");
        while (currentNode.next != null){
            System.out.print(currentNode.data+"  ");
            currentNode = currentNode.next;
        }
        System.out.println(currentNode.data);
        System.out.println("\n\n");
    }

    public void deleteItem(int data){
        Node currentNode = this.head;
        Node prevNode = this.head;
        while(currentNode.next != null){
            if (currentNode.data == data){
                prevNode.next = currentNode.next;
                System.out.println("FOund The Value");
                return;
            }
            prevNode = currentNode;
            currentNode = currentNode.next;
        }
        System.out.println("No Value FOund");
    }
}