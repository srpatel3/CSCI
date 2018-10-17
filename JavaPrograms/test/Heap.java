public class Heap{
    // Helpful Tips
    // parent index = (currentIndex -2) /2
    // leftChild Index = currentIndex *2 +1
    // rightChileIndet = currentIndex*2 +2 
    private int totalCap = 10;
    // To keep track of total no of elements in array
    private int size = 0;
    // declare an array to hold the elements of heap
    int[] items = new int[totalCap];
    

    // For Swapping Values at two indices
    private voif swap(int index1, int index2){
        int temp = items[index1];
        items[index1] = items[index2];
        items[index2] = temp;
    }

    // For getting parent Index from current element in Heap
    private int getParentIndex ( int index){
        return (index - 1)/2;
    }

    // Get the index of a Right Child from Current Parent
    private int getRightChildIndex(int index){
        return (index*2) + 2;
    }

    // Get the index of a Left Child from Current Parent
    private int getLeftChildIndex(int index){
        return (index*2) + 1;
    }

    // Check if parent has left child or not
    private boolean hasLeftChild(int index){
        return getLeftChildIndex(index) < size;
    }

    // Check if parent has right child or not
    private boolean hasRightChild(int index){
        return getRightChildIndex(index) < size;
    }

    // Lol It is funny
    private boolean hasParent(int index){
        return getParentIndex(index) >= 0;
    }

    // this gets value for a left child of a parent
    private int getLeftChild(int index){
        return items[getLeftChildIndex(index)];
    }

    // Same with the right CHild
    private int getRightChild(int index){
        return items[getRightChildIndex(index)];
    }

    // Same Thing with parent
    private int getParent(int index){
        return items[getParentIndex(index)];
    }

}