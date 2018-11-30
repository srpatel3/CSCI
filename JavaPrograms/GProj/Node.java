public class Node implements Comparable{
	private double leftCord;
	private double rightCord;

	public Node(double leftCord,double rightCord){
		this.leftCord = leftCord;
		this.rightCord = rightCord;
	}
	
	//setter methofs
	public void setLeft(double cord){
		this.leftCord = cord;
	}
	public void setRight(double cord){
		this.rightCord = cord;
	}

	//getter methods
	public double getLeft(){
		return this.leftCord;
	}

	public double getRight(){
		return this.rightCord;
	}

	//returns state
	public String toString(){
		return Double.toString(this.leftCord) + " " + Double.toString(this.rightCord);
	}

	//comparing Function
	public int compareTo(Object o){
		return (this.getLeft() < ((Node) o).getLeft() ? -1 : (this.getLeft() == ((Node) o).getLeft() ? 0 : 1));
		// return this.getLeft().compareTo.(((Node) o).getLeft());
	}

}
