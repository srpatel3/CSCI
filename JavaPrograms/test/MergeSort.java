public class MergeSort{
  int[] array;

  //Constructor
  public MergeSort(){
    this.array = new int[]{90,30,23,60,50,10,22};
  }


  public void mergeArrays(int startIndex, int middleIndex, int endIndex){
    int sizeArray1 = middleIndex-startIndex+1;
    int sizeArray2 = endIndex - middleIndex;

    int[] tempArray1 = new int[sizeArray1];
    int[] tempArray2 = new int[sizeArray2];

    for(int i = 0; i< sizeArray1; i++){
      tempArray1[i] = this.array[startIndex+i];
    }
    for(int i=0; i<sizeArray2; i++){
      tempArray2[i] = this.array[middleIndex+i+1];
    }
    int tempIndex1 = 0, tempIndex2 = 0;
    int finalIndex = startIndex;
    while(tempIndex1 < tempArray1.length && tempIndex2 < tempArray2.length){
      if(tempArray1[tempIndex1] < tempArray2[tempIndex2]){
        this.array[finalIndex] = tempArray1[tempIndex1];
        tempIndex1++;
      }
      else{
        this.array[finalIndex] = tempArray2[tempIndex2];
        tempIndex2++;
      }
      finalIndex++;
    }

    while(tempIndex1 < tempArray1.length){
      this.array[finalIndex] = tempArray1[tempIndex1];
      finalIndex++;
      tempIndex1++;
    }

    while(tempIndex2 < tempArray2.length){
      this.array[finalIndex] = tempArray2[tempIndex2];
      finalIndex++;
      tempIndex2++;
    }
  }


  public void startSorting(int startIndex, int endIndex){
    if(startIndex < endIndex){
      int middleIndex = (startIndex + endIndex)/2;
      startSorting(startIndex, middleIndex);
      startSorting(middleIndex+1, endIndex);
      mergeArrays(startIndex, middleIndex, endIndex);
    }

  }

  public void sort(){
    System.out.println("Array Before Sorting...");
    printArray();
    startSorting(0,this.array.length-1);
    System.out.println("Array After Sorting...");
    printArray();
  }

  public void printArray(){
    for(int i=0; i<this.array.length; i++){
      System.out.print(this.array[i] + " ");
    }
    System.out.println();
  }
}
