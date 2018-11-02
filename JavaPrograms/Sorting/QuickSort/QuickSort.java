public class QuickSort{

// Input array
// Choose pivot element (Could be random)
// Run algorithm
// Partition current array based on pivot element
// repeat the same step


  public int[] array;

  // Constructor
  public QuickSort(){
    array = new int[] {50,70,80,40,10,90,20,60,0,12};
  }

  public void swapElements(int startIndex, int endIndex){
    int temp = this.array[startIndex];
    this.array[startIndex] = this.array[endIndex];
    this.array[endIndex] = temp;
  }

  public void ImplementSort(int startIndex, int endIndex){
    if(startIndex < endIndex){
      System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex);
      // System.out.println("Array :  ");
      // printArray();
      int partitionIndex = partition(startIndex, endIndex);
      // System.out.println("Partition Index : "+partitionIndex);
      System.out.println();
      System.out.println();
      System.out.println("_____________Next Iteration____________");
      // System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex);
      // int partition1 = partition(startIndex, partitionIndex-1);
      ImplementSort(startIndex, partitionIndex-1);
      ImplementSort(partitionIndex+1, endIndex);
      // int partition2 = partition(partitionIndex,endIndex);
      // int partition3 = partition(partitionIndex, partition2-1);
      // int partition4 = partition(partition2,endIndex);
      // printArray();
    }

  }

  public int partition(int startIndex, int endIndex){
    int pivotElement = this.array[endIndex];
    int index1 = startIndex-1;
    for(int index2 = startIndex; index2 < endIndex;index2++){
      if(this.array[index2] <= pivotElement){
        index1++;
        swapElements(index1,index2);
      }
    }
    index1++;
    swapElements(index1,endIndex);
    printArray();
    return index1;
  }

  // public int partition(int startIndex1, int endIndex1){
  //   int startIndex = startIndex1;
  //   int endIndex = endIndex1;
  //   int pivotElement = this.array[(startIndex + endIndex)/2];
  //   System.out.println("Pivot Element is : "+pivotElement+" With pivot Index : "+(startIndex + endIndex)/2 );
  //   System.out.println("Last Element in array is : "+this.array[endIndex]);
  //   System.out.println("For array ");
  //   for(int i=startIndex; i<= endIndex;i++){
  //     System.out.print(this.array[i]+" ");
  //   }
  //   System.out.println();
  //   while(startIndex < endIndex){
  //     if(this.array[startIndex] >= pivotElement && this.array[endIndex] <= pivotElement){
  //       System.out.println("Swapping Elements : "+startIndex+" and "+endIndex);
  //       swapElements(startIndex, endIndex);
  //       startIndex++;
  //       endIndex--;
  //     }
  //     else{
  //       if(this.array[startIndex] < pivotElement){
  //         startIndex++;
  //       }
  //       if(this.array[endIndex]> pivotElement){
  //         endIndex--;
  //       }
  //     }
  //   }
  //   // System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex);
  //   // System.out.println("Array after iteration....");
  //   printArray();
  //   startIndex--;
  //   System.out.println("StartIndex is : "+startIndex);
  //   return startIndex;
  // }

  public void sort(){
    int startIndex = 0;
    int endIndex = this.array.length -1;
    // int pivot = array[3];
    // System.out.println("startIndex : "+startIndex+" endIndex : "+endIndex+" pivotElement : "+pivot);
    ImplementSort(startIndex, endIndex);
  }
  // To print the array
  public void printArray(){
    for(int i=0;i<this.array.length;i++){
      System.out.print(array[i] + " ");
    }
    System.out.println();
  }
}
