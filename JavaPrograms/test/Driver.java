import java.util.*;

public class Driver{
    public static void main(String[] args) {
       // MergeSort Q = new MergeSort();
      // Q.sort();
      Scanner inFromKey = new Scanner(System.in);
      int input = 0;
      // LinkedList newList = new LinkedList(new Node(20));
      Node newList = new Node(1);
      while (input != 4){
        System.out.println("Enter Your Choice...\n1.Add Element\n2.Delete Element\n3.Search Element\n4.Exit...!!!");
        input = inFromKey.nextInt();
        switch(input){
          case 1:
            System.out.println("Enter Element to add : ");
            newList.addNode(inFromKey.nextInt());
            break;
            case 2 :
              newList.printBST();
              System.out.println();
              break;
          // case 2:
          //   System.out.println("Enter the element you want to delete : ");
          //   newList.deleteElement(inFromKey.nextInt());
          //   break;
          case 4:
            System.out.println("Thank You...!!!");
            break;
          default:
            System.out.println("Wrong Choice try again...");
            break;
        }
      }
    }
}
