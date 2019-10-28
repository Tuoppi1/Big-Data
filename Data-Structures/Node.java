import java.util.LinkedList;

public class Node {
   private float x;
   private float y;
   private boolean visited;
   private LinkedList<Edge> outEdges;
   private float distance;
   
   public Node(float x,float y) {
      setX(x);
      setY(y);
      setVisited(false);
      setOutEdges(new LinkedList<Edge>());
      setDistance(0);
   }


   public float getX() {
      return x;
   }

   public void setX(float x) {
      this.x = x;
   }

   public float getY() {
      return y;
   }

   public void setY(float y) {
      this.y = y;
   }

   public boolean isVisited() {
      return visited;
   }

   public void setVisited(boolean visited) {
      this.visited = visited;
   }
   
   public String toString() {
      return (x+", "+y);
   }

   public LinkedList<Edge> getOutEdges() {
      return outEdges;
   }

   public void setOutEdges(LinkedList<Edge> outEdges) {
      this.outEdges = outEdges;
   }
   
   public String inOut(LinkedList<Edge> Edges) {
      String s ="Node "+toString()+"\n In nodes = ";
      String s2 =" Out nodes = ";
      for(Edge e:Edges) {
         if(e.getEnd() == this)
         s = s+e.getStart().toString()+"\t";
      }
      for(Edge e:outEdges)s2 = s2+e.getEnd().toString()+"\t";
      return s+"\n"+s2+"\n\n";
   }
   
   public void resetOutEdges() {
      this.outEdges = new LinkedList<Edge>();
   }


   public float getDistance() {
      return distance;
   }


   public void setDistance(float distance) {
      this.distance = distance;
   }
}
