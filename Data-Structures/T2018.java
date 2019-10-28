import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.Float;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class T2018 {
   private String line;
   private float x[];
   private float y[];
   private LinkedList<Node> Graph;
   private LinkedList<Edge> Edges;
   private BufferedReader br;

   public T2018() {
      Graph = new LinkedList<Node>();
      Edges = new LinkedList<Edge>();
   }

   public void readInput() {
      x = new float[400];
      y = new float[400];
      try {
         br = new BufferedReader(new FileReader("Tdata.txt"));

         for (int i = 0; i < 400; i++) {
            line = br.readLine();
            String[] values = line.split(",");
            x[i] = Float.parseFloat(values[0]);
            y[i] = Float.parseFloat(values[1]);
            //System.out.print(x[i] + " ," + y[i] + "\n");
            Node newNode = new Node(x[i], y[i]); // Creating a new Node while reading coordinates
            Graph.add(newNode); // Adding new a Node into the Graph
         }
         System.out.println(Graph.size()+" Nodes created");
      } catch (Exception e) {
      }
   }               
   private void writeOutput() {
      try {
         BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
         for (int i = 0; i < 10; i++) {
            bw.write(Float.toString(x[i]));
            bw.write(",");
            bw.write(Float.toString(y[i]));
            bw.newLine();
         }
         bw.close();

      } catch (IOException e) {
         System.err.format("IOException: %s%n", e);
      }
      System.out.println("Tiedosto kirjoitettu");
   }
   
   // Adds the closest and the second closest neighbors to every node
   // Also creates edges for the Edges list
   public void findNeighbors() {
         for (Node n1:Graph) {
            float closest = 9999;
            float secondClosest = 9999;
            Edge ed = null;
            Edge ed2 = null;

            for (Node n2:Graph) { // Setting up neighbors
               try {
                  float distance = euclideanDistance(n1,n2);
                  if (n2 == n1) { // Skips the same node
                  }else if (distance < closest) {
                     secondClosest = closest;
                     closest = distance;
                     ed2 = ed;
                     ed = new Edge(n1, n2, closest);
                     
                     
                  }else if (closest < distance && distance < secondClosest) {
                     secondClosest = distance;
                     ed2 = new Edge(n1, n2, secondClosest);
                  }
               } catch (Exception e) {
               }
            }
            Collections.addAll(Edges, ed,ed2); // New edges
            Collections.addAll(n1.getOutEdges(),ed,ed2); // Add edges to node outEdges list
         }
   }

   // Adds a one more neighbor to a node and a new edge to the Edges list
   public void moreNeighbors() {
      float closest = 99999;
      Edge ed = null;
      
      for (Node n1:Graph) {
         float lastNeighbor = n1.getOutEdges().getLast().getDistance(); // Checking the distance of the last neighbor

         for (Node n2:Graph) { // Setting up 1 more neighbor
            try {
               float distance = euclideanDistance(n1,n2);
               if (n2 == n1) { // Skips the same node
               }else if (distance > lastNeighbor && distance < closest) {
                  closest = distance;
                  ed = new Edge(n1, n2, closest);
               }
            } catch (Exception e) {
            }
         }
         n1.getOutEdges().add(ed);
         Edges.add(ed); // New edge
      }
      
   }
   
   // Calculates distance between nodes
   private float euclideanDistance(Node current, Node n) {
      float x1 = current.getX();
      float y1 = current.getY();
      float x2 = n.getX();
      float y2 = n.getY();
      return (float) Math.sqrt((Math.pow((x1 - x2), 2)) + (Math.pow((y1 - y2), 2)));
   }
   
   // Finds the average node coordinate
   private float[] FindAverage(LinkedList<Node> nList) {
      float xAverage = 0;
      float yAverage = 0;
      
      for(Node n:nList) {
         xAverage = xAverage + n.getX();
         yAverage = yAverage  + n.getY();
      }
      
      xAverage = xAverage / nList.size();
      yAverage = yAverage / nList.size();
      float a[] = {xAverage,yAverage};
      return a;
   }
   
   // Distance from average node coordinates
   private float euclideanDistance2(Node current, float a[]) {
      float x1 = current.getX();
      float y1 = current.getY();
      float x2 = a[0];
      float y2 = a[1];
      return (float) Math.sqrt((Math.pow((x1 - x2), 2)) + (Math.pow((y1 - y2), 2)));
   }
  
   // Breadth First order
   public int BFS(int n,BufferedWriter bw,BufferedWriter bw2,LinkedList<Node> Graph1){
      int visitCount = 0;
      try {
         LinkedList<Edge> queue = new LinkedList<Edge>(); 
         bw.write(Graph1.get(n).toString());  // Printing the first node
         bw.newLine();
         bw2.write(Graph1.get(n).inOut(Edges));  // Printing the in- and out decrees of the node
         bw2.newLine();
         Graph1.get(n).setVisited(true);
         visitCount++;
         queue = Graph1.get(n).getOutEdges();
         
         while(queue.size()>0) {
            LinkedList<Edge> queue2 = new LinkedList<Edge>();
            for(Edge j:queue) {
               if(Graph1.get(Graph1.indexOf(j.getEnd())).isVisited() == false) {
                  bw.write(j.getEnd().toString()); // Printing the neighbors of the first node
                  bw.newLine();
                  bw2.write(j.getEnd().inOut(Edges)); // Same to in- and out decrees
                  bw2.newLine();
                  Graph1.get(Graph1.indexOf(j.getEnd())).setVisited(true);
                  visitCount++;
                  for(Edge e:j.getEnd().getOutEdges()) {   // Getting the neighbors of the printed neighbors
                     queue2.add(e);
                  }
               }
            }
            queue = queue2;   // Reseting the queue and repeating the process till all nodes have been printed
         }
         for(Node n1:Graph1) {   // Printing rest of the node subgraphs
            if(n1.isVisited()==false) {
               bw.newLine();
               bw2.newLine();
               BFS(Graph1.indexOf(n1),bw,bw2,Graph1);
            }
         }
      }catch(IOException e) {
         System.out.println("an Error occoured in BFS");
      }
      return visitCount;
   }

   // Depth First order
   public int DFS(int n,BufferedWriter bw2,boolean all,LinkedList<Node> Graph1) throws IOException {
      int visitedCount = 0;
      LinkedList<Edge> queue = new LinkedList<Edge>();
      if(Graph1.get(n).isVisited()==false) {
         bw2.write(Graph1.get(n).toString());  // Printing the first node
         bw2.newLine();
         visitedCount++;
      }
      Graph1.get(n).setVisited(true);
      queue = Graph1.get(n).getOutEdges();

      for (Edge n1 : queue) { // Printing the neighbors of the first node recursively, prioritizing the closest first.
         if (n1.getEnd().isVisited() == false) {
            bw2.write(n1.getEnd().toString());
            bw2.newLine();
            Graph1.get(Graph1.indexOf(n1.getEnd())).setVisited(true);
            visitedCount++;
            visitedCount = visitedCount + DFS(Graph1.indexOf(n1.getEnd()), bw2,false,Graph1);
         }
      }
      if(all) {
         for(Node i:Graph1) {  // Printing rest of the node subgraphs
            if(i.isVisited()==false) {
               bw2.newLine();
               DFS(Graph1.indexOf(i),bw2,true,Graph1);
            }
         }
      }
      return visitedCount;
   }
   
   // Checking if the Graph is unified a Graph
   public int combineGraph(int n) {
      int visitedCount = 0;
      LinkedList<Edge> queue = new LinkedList<Edge>();
      if(Graph.get(n).isVisited()==false) {
         Graph.get(n).setVisited(true);
         visitedCount++;
      }
      queue = Graph.get(n).getOutEdges();

      for (Edge n1 : queue) { // Checking the neighbors of the first node recursively, prioritizing the closest first.
         if (n1.getEnd().isVisited() == false) {
            Graph.get(Graph.indexOf(n1.getEnd())).setVisited(true);
            visitedCount++;
            visitedCount = visitedCount + combineGraph(Graph.indexOf(n1.getEnd()));
         }
      }
      return visitedCount;
   }
   
   // Deletes given node and recalculates neighbors and Edges accordingly
   public void deleteNode(int gIndex) {
      Graph.remove(gIndex);
      Edges = new LinkedList<Edge>();
      
      for(Node n:Graph) { // Reset Node outEdge lists
         n.setOutEdges(new LinkedList<Edge>());
      }
      
      findNeighbors();
      System.out.println("Node deleted. Graph size = "+Graph.size());
   }
    
   // Writes only nodes that are considered as outliers (Distance from average node coordinate > 2.0)
   public int BFS_Outliers(int n,BufferedWriter bw,LinkedList<Node> Graph1){
      int visitCount = 0;
      try {
         LinkedList<Edge> queue = new LinkedList<Edge>(); 
         if(Graph1.get(n).getDistance() > 2) {
            bw.write(Graph1.get(n).toString());  // Printing the first node
            bw.newLine();
         }
         Graph1.get(n).setVisited(true);
         visitCount++;
         queue = Graph1.get(n).getOutEdges();
         
         while(queue.size()>0) {
            LinkedList<Edge> queue2 = new LinkedList<Edge>();
            for(Edge j:queue) {
               if(Graph1.get(Graph1.indexOf(j.getEnd())).isVisited() == false) {
                  if(j.getEnd().getDistance() > 2) {  // Defines outlier distance from average node coordinate
                     bw.write(j.getEnd().toString()+ " Distance from average node coordinate = "+j.getEnd().getDistance());
                     bw.newLine();
                  }
                  Graph1.get(Graph1.indexOf(j.getEnd())).setVisited(true);
                  visitCount++;
                  for(Edge e:j.getEnd().getOutEdges()) {   // Getting the neighbors of the printed neighbors
                     queue2.add(e);
                  }
               }
            }
            queue = queue2;   // Reseting the queue and repeating the process till all nodes have been printed
         }
         for(Node n1:Graph1) {   // Printing rest of the node subgraphs
            if(n1.isVisited()==false) {
               bw.newLine();
               BFS_Outliers(Graph1.indexOf(n1),bw,Graph1);
            }
         }
      }catch(IOException e) {
         System.out.println("an Error occoured in BFS");
      }
      return visitCount;
   }
   
   public static void main(String[] args) throws IOException {
      T2018 ht = new T2018();
      ht.readInput();
      ht.writeOutput();
      ht.findNeighbors();
      Collections.sort(ht.Edges);
      for(Edge e:ht.Edges) System.out.println(e.getDistance());
            
      //  3. Breadth First order
      BufferedWriter bw = new BufferedWriter(new FileWriter("BFS.txt"));
      BufferedWriter bw2 = new BufferedWriter(new FileWriter("Degrees.txt"));
      ht.BFS(0,bw,bw2,ht.Graph);
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw2.close();
      bw.close();
      
      // 4. Depth First order
      bw = new BufferedWriter(new FileWriter("DFS.txt"));
      ht.DFS(0,bw,true,ht.Graph);
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw.close();
      
      // 6. Remove a given node
      Scanner sc = new Scanner(System.in);
      System.out.println("There are "+ht.Graph.size()+" Nodes in the Graph");
      System.out.println("Choose an index of the node which you want to delete. (0 - "+ht.Graph.size()+")");
      int gIndex = sc.nextInt();
      ht.deleteNode(gIndex);
      
      bw = new BufferedWriter(new FileWriter("DIM.txt"));
      bw2 = new BufferedWriter(new FileWriter("Degrees.txt"));
      ht.BFS(0,bw,bw2,ht.Graph);
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw2.close();
      bw.close();
      
      // 7. Add more nearest neighbors
      System.out.println("\nNext step is to combine the Graph.\nYou migh want to check the files before more neighbors are added.");
      boolean lippu = false;
      while(!lippu) {
         String y = sc.nextLine();
         if(y.equals("y")) {
            lippu=true;
         }else System.out.println("Type \"y\" to proceed when you are ready.");
      }
      sc.close();
      
      ht.combineGraph(0);
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw = new BufferedWriter(new FileWriter("trash.txt"));
      int visitedNeighbors = ht.DFS(0,bw,false,ht.Graph);
      while(visitedNeighbors < ht.Graph.size()) { // Adds neighbors till there is a path from a node to any node
         for(Node n1:ht.Graph) n1.setVisited(false);
         ht.moreNeighbors();
         Collections.sort(ht.Edges); // Keeps the Edges list sorted
         visitedNeighbors = ht.DFS(0,bw,false,ht.Graph); // Checks if the Graph is a unified graph
      }
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw = new BufferedWriter(new FileWriter("COMP.txt"));
      ht.DFS(0,bw,false,ht.Graph);
      for(Node n1:ht.Graph) n1.setVisited(false);
      bw.close();
      
      // 10. Sets the distance value of a node to distance from the average node coordinate
      float a[] = ht.FindAverage(ht.Graph);
      for(Node n:ht.Graph) n.setVisited(false);
      for(Node n:ht.Graph) n.setDistance(ht.euclideanDistance2(n, a)); // Sets the distance value according to average
      bw = new BufferedWriter(new FileWriter("OUTLIER.txt"));
      ht.BFS_Outliers(0, bw, ht.Graph);
      bw.close();
       
      System.out.println("Tasks 1,2,3,4,5,6,7,10 are done!");  
   } 
}