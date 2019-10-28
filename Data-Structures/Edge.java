
public class Edge implements Comparable<Edge>{
   private Node start;
   private Node end;
   private float distance;
   
   public Edge(Node start,Node end,float distance) {
      setStart(start);
      setEnd(end);
      setDistance(distance);
   }

   public Node getStart() {
      return start;
   }
   
   @Override
   public int compareTo(final Edge e) {
      return Float.compare(this.getDistance(),e.getDistance());
   }
   
   public String toString() {
      return "Distance from start node "+start.toString()+" to end node "+end.toString()+" is "+distance;
   }

   public void setStart(Node start) {
      this.start = start;
   }

   public Node getEnd() {
      return end;
   }

   public void setEnd(Node end) {
      this.end = end;
   }

   public float getDistance() {
      return distance;
   }

   public void setDistance(float distance) {
      this.distance = distance;
   }
}
