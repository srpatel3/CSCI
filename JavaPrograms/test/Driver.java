import java.util.*;


class Driver{
    public static void main(String[] args) {
        Scanner inFromKey = new Scanner(System.in);
        int input = 0;
        while ( input != 4){
            System.out.println("Enter Your Choice:\n1.Inset Data into heap\n2.Remove Element From Heap\n4\.Exit");
            input = inFromKey.nextInt();
            switch (input) {
                case 1:
                    System.out.println("You have selected First Option");
                    break;
                case 2:
                    System.out.println("You have selected second option");
                    break;

                default:
                    break;
            }
        }
        System.out.println("Hii I am in Driver");
    }
}
