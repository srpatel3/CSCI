import java.util.Arrays;
public class Heap{
  public int[] array;
  public int size;
  // public int capacity = 10;
  //Constructor
  public Heap(){
    this.size = 0;
    this.array = new int[2];
  }

// Code for adding element in Heap
  public void addElement(int data){
    this.checkSize();
    this.array[this.size] = data;
    this.heapyfyUp();
    this.size++;
    this.printArray();
    System.out.println();

    // System.out.println("IM");
  }


  public void heapyfyUp(){
    // System.out.println("HERE");
    int index = this.size;
    while(this.hasParent(index) && this.array[index] < this.array[this.getParentIndex(index)]){
    // System.out.println("In");
      this.swapElements(index, this.getParentIndex(index));
      index = getParentIndex(index);
    }
  }


  public void swapElements(int index1, int index2){
    int temp  = this.array[index1];
    this.array[index1] = this.array[index2];
    this.array[index2] = temp;
  }

  public int pollElement(){
    int min = this.array[0];
    this.array[0] = this.array[this.size-1];
    heapyFyDown();
    System.out.println(min);
    return min;
  }

  public void heapyFyDown(){
    
  }

  public boolean hasLeftChild(int parentIndex){
    return getLeftChildIndex(parentIndex) < size;
  }
  public boolean hasRightChild(int parentIndex){
    return getRightChildIndex(parentIndex) < size;
  }
  public boolean hasParent(int childIndex){
    return getParentIndex(childIndex) >= 0;
  }
  public int getLeftChild(int parentIndex){
    return this.array[getLeftChildIndex(parentIndex)];
  }

  public int getRightChild(int parentIndex){
    return this.array[getRightChildIndex(parentIndex)];
  }

  public int getParent(int childIndex){
    return this.array[getParentIndex(childIndex)];
  }
  // Get Indices
  public int getLeftChildIndex(int parentIndex){
    return (2*parentIndex + 1);
  }
  public int getRightChildIndex(int parentIndex){
    return (2*parentIndex +2);
  }
  public int getParentIndex(int childIndex){
    return (childIndex-1)/2;
  }


  public void printArray(){
    for(int i=0;i<this.size;i++){
      System.out.print(this.array[i]+" ");
    }
    System.out.println();
  }
// Checks if we need to increase the size of an array of not
// Must check before each addition of an element
  public void checkSize(){
    if(this.size == this.array.length){
      this.array = Arrays.copyOf(this.array, this.array.length*2);
    }
  }

}
