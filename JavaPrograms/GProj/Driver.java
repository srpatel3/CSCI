import java.text.DecimalFormat;
import java.util.*;

public class Driver{

	public static void main(String[] args){
		DecimalFormat df = new DecimalFormat("#.00");
		ArrayList<Node> cordList = new ArrayList<>();
		// cordList.add(node);
		double impact = Math.random()*100;
		//while (!isFinalState(cordList)){
		int count = 0;
		//while (count < 100){
		//	impact = Math.random()*100;
			
		//	System.out.println("Generate Random number is... "+impact);
		//	count ++;
		//}
		cordList.add(new Node(8,10));
		cordList.add(new Node(2,5));
		cordList.add(new Node(70, 80));
		Collections.sort(cordList);
		updateCordList(76, cordList);
		updateCordList(9, cordList);
	}
	
	
	public static void updateCordList(double cord, ArrayList<Node> cordList){
		for(int i = 0; i < cordList.size(); i++){
			Node node = cordList.get(i);
			if(isOntheLeft(cord,node)){
				System.out.println("Drops on the left for "+ node.toString());
				
				break;
			}
			else if(isInBetween(cord,node)){
				System.out.println("Drops in Between for "+node.toString());
				break;
			}
			
			else {
				if(i == cordList.size() -1 ){
					//Just add New Cord
					System.out.println("Drops new Record Booyah..." + node.toString());
					break;
	
				else{
					System.out.println("New but not at last");
					break;
				}
			}
			
			//System.out.println(cordList.get(i).toString());
		}
	}
	
	public static boolean isInBetween(double cord, Node node){
		if( node.getLeft() < cord && node.getRight() > cord){
			return true;
		}
		else{
			return false;
		}
	}
	public static boolean isOntheRight(double cord, Node node){
		if( node.getRight() < cord){
			return true;
		}
		else{
			return false;
		}
	}

	public static boolean isOntheLeft(double cord, Node node){
		if ( node.getLeft() > cord){
			return true;
		}
		else{
			return false;
		}
	}


	
	public static boolean isFinalState(ArrayList<Node> cordList){
		if ( cordList.size() == 1 && cordList.get(0).getLeft() == 0.0 && 
cordList.get(0).getRight() == 100.0){
			return true;
		}
		else{
			return false;
		}
	}
}
