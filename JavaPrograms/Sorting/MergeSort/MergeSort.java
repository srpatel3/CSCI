public class MergeSort{
  int array[];

  // Constructor
  public MergeSort(){
    this.array = new int[]{90,40,21,30,60,50,100,80};
  }



  public void mergeArrays(int startIndex, int middleIndex, int endIndex){
    // Get the Size of arrays to be merged
    // Why +1 though in first array
    // May be we are starting From zero...???
    int sizeOfArray1 = middleIndex - startIndex + 1;
    int sizeOfArray2 = endIndex - middleIndex;

    int[] leftArray = new int[sizeOfArray1];
    int[] rightArray = new int[sizeOfArray2];

    // Copy both the array values in temp array and then merge them
    for(int i=0;i<sizeOfArray1; i++){
      leftArray[i] = this.array[startIndex+i];
    }
    for(int i=0;i<sizeOfArray2;i++){
      rightArray[i] = this.array[middleIndex+1+i];
    }
    // Start Merging arrays

    int indexArray1=0,indexArray2=0;
    int indexFinalArray = startIndex;
    while(indexArray1 < sizeOfArray1 && indexArray2 < sizeOfArray2){
      if(leftArray[indexArray1] <= rightArray[indexArray2]){
        this.array[indexFinalArray] = leftArray[indexArray1];
        indexArray1++;
      }
      else{
        this.array[indexFinalArray] = rightArray[indexArray2];
        indexArray2++;
      }
      indexFinalArray++;
    }

    while(indexArray1 < sizeOfArray1){
      this.array[indexFinalArray] = leftArray[indexArray1];
      indexFinalArray++;
      indexArray1++;
    }

    while(indexArray2 < sizeOfArray2){
      this.array[indexFinalArray] = rightArray[indexArray2];
      indexFinalArray++;
      indexArray2++;
    }

  }
  public void startSorting(int startIndex, int endIndex){
    if(startIndex < endIndex){
        int middleIndex = (startIndex + endIndex) / 2;
        startSorting(startIndex,middleIndex);
        startSorting(middleIndex+1,endIndex);

        mergeArrays(startIndex, middleIndex, endIndex);
    }
  }
  public void sort(){
    System.out.println("Array Before Sorting : ");
    printArray();
    startSorting(0,this.array.length-1);
    System.out.println("Array After sorting");
    printArray();
    // Deviding Array into two different halves
    // int middleIndex = (0+this.array.length)/2;
    // System.out.println(middleIndex);
  }

  public void printArray(){
    for(int i=0; i< this.array.length; i++){
      System.out.print(this.array[i]+" ");
    }
    System.out.println();
  }
}
