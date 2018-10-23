public class QuickSort{

// Input array
// Choose pivot element (Could be random)
// Run algorithm
// Partition current array based on pivot element
// repeat the same step


  public int[] array;;

  // Constructor
  public QuickSort(){
    array = new int[] {5,7,8,4,1,9,2,6,0,12};
  }

  public void swapElements(int startIndex, int endIndex){
    int temp = this.array[startIndex];
    this.array[startIndex] = this.array[endIndex];
    this.array[endIndex] = temp;
  }
 
  public void ImplementSort(int startIndex, int endIndex){
    System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex;
    int pivotIndex = (startIndex + endIndex)/2;
    int partIndex = partition(startIndex, endIndex);
    System.out.println(partIndex);
    
    // ImplementSort(startIndex, partIndex);
    // ImplementSort(startIndex+1, endIndex);
  }

  public int partition(int startIndex, int endIndex){
    int pivotElement = (startIndex+endIndex)/2;
    while ( startIndex < endIndex){
      if(this.array[startIndex] > this.array[pivotElement] && this.array[endIndex] < this.array[pivotElement]){
        swapElements(startIndex,endIndex);
        startIndex++;
        endIndex--;
      }
      else{
        if(this.array[startIndex] < this.array[pivotElement]){
          startIndex++;
        }
        if(this.array[endIndex] > this.array[pivotElement]){
          endIndex--;
        }
      }
    }
    return startIndex;
  }

  public void sort(){
    int startIndex = 0;
    int endIndex = this.array.length -1;
    // int pivot = array[3];
    // System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex+" pivotElement : "+pivot);
    ImplementSort(startIndex, endIndex);
  }
  // To print the array
  public void printArray(){
    for(int i=0;i<10;i++){
      System.out.print(array[i] + " ");
    }
    System.out.println();
  }
}
