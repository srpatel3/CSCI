public class Driver{
  public static void main(String[] args) {
      System.out.println("In Driver Method");
      QuickSort Q = new QuickSort();
      Q.printArray();
      Q.sort();
      Q.printArray();
  }
}
