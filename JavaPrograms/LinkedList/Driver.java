import java.util.*;
public class Driver{
  public static void main(String[] args) {
    System.out.println("Inside Main"); 
    LinkedList lst = new LinkedList();
    Scanner inFromKey = new Scanner(System.in);
    int input = 1;
    while (input != 4){
      System.out.println("Enter Your Choice: \n1.Add Item to List\n2.Print Item\n3.Delete Item From List\n4. Exit");
      input = inFromKey.nextInt();
      switch (input) {
        case 1:
          System.out.println("Enter Node data information : ");
          lst.addNode(inFromKey.nextInt());
          System.out.println("Value Added to the list");
          break;
        case 2:
          lst.printList();
          break;
        case 3:
          System.out.println("Enter Item You want to delete in List");
          lst.deleteItem(inFromKey.nextInt());
          break;
        default:
          break;
      }
      // input = inFromKey.nextInt();
    // lst.addNode(3);
    }
    
  }
}
