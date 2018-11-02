import java.util.Scanner;
public class Driver{

	public static void main(String[] args){
		Heap newList = new Heap();
		Scanner inFromKey = new Scanner(System.in);
		int input = 0;
		while(input !=4){
			System.out.println("1.Add Data\n2.Delete Data\n3.PrintList\n4.Exit");
			input = inFromKey.nextInt();
			switch(input){
				case 1:
					System.out.println("Enter Element : ");
					newList.addElement(inFromKey.nextInt());
					break;
				case 2:
					System.out.println("Poll Element..");
          int min = newList.pollElement();
          
					//newList.deleteElement(inFromKey.nextInt());
					break;
				case 3:
					newList.printArray();
					break;
				case 4:
					System.out.println("Thank You...!!!");
					break;
				default :
					System.out.println("Wrong Choice Try Again");
					break;
			}
		}
	}
}
