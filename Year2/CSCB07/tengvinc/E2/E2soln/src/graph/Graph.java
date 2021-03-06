package graph;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

/**
 * An undirected graph of <code>Node</code>s.
 * 
 * @author anya
 * @param <T>
 *          the type of values in this <code>Graph</code>'s <code>Nodes</code>
 */
public class Graph<T> {

  // instance variables
  private Map<Node<T>, Set<Node<T>>> nodeToNeighbours;

  /**
   * Creates a new empty <code>Graph</code>.
   */
  // constructor
  public Graph() {
    this.nodeToNeighbours = new HashMap<Node<T>, Set<Node<T>>>();
  }

  /**
   * Returns a <code>Set</code> of <code>Node</code>s in this
   * <code>Graph</code>.
   * 
   * @return a <code>Set</code> of <code>Node</code>s in this <code>Graph</code>
   */
  public Set<Node<T>> getNodes() {
    return nodeToNeighbours.keySet();
  }

  /**
   * Returns the <code>Node</code> from this <code>Graph</code> with the given
   * ID.
   * 
   * @param id
   *          the ID of the <code>Node</code> to return
   * @return the <code>Node</code> from this <code>Graph</code> with the given
   *         ID, if such <code>Node</code> exists in this <code>Graph</code>
   * @throws NoSuchNodeException
   *           if there is no <code>Node</code> with ID <code>id</code> in this
   *           <code>Graph</code>
   */
  // getNode
  public Node<T> getNode(int id) throws NoSuchNodeException {
    Node<T> retNode = null;
    // Loop through the map and attempt to find a Node with the given id
    for (Node<T> nodes : nodeToNeighbours.keySet()) {
      if (nodes.getId() == id) {
        retNode = nodes;
      }
    }
    if (retNode != null) {
      return retNode;
    } else {
      throw new NoSuchNodeException();
    }

  }

  /**
   * Returns a <code>Set</code> of neighbours of the given <code>Node</code>.
   * 
   * @param node
   *          the <code>Node</code> whose neighbours are returned
   * @return a <code>Set</code> of neighbours of <code>node</code>
   */
  public Set<Node<T>> getNeighbours(Node<T> node) {
    return nodeToNeighbours.get(node);
  }

  /**
   * Returns whether <code>Node</code>s with the given IDs are adjacent in this
   * <code>Graph</code>.
   * 
   * @param id1
   *          ID of the node to test for adjacency
   * @param id2
   *          ID of the node to test for adjacency
   * @return true, if <code>Node</code>s with IDnew HashMap<Node<T>, T>()s id1
   *         and id2 are adjacent in this <code>Graph</code> (there is an edge
   *         between them), and false otherwise
   * @throws NoSuchNodeException
   *           if node with id1 or id2 is not in this <code>Graph</code>
   */
  // areAdjacent
  public boolean areAdjacent(int id1, int id2) throws NoSuchNodeException {
    if (nodeToNeighbours.containsKey(this.getNode(id1))
        && nodeToNeighbours.containsKey(this.getNode(id2))) {
      boolean isInId1 = false;
      for (Node<T> nodes : nodeToNeighbours.get(this.getNode(id1))) {
        if (nodes.getId() == id2) {
          return true;
        }
      }
      return isInId1;
    } else {
      throw new NoSuchNodeException();
    }
  }

  /**
   * Returns whether the given <code>Node</code>s are adjacent in this
   * <code>Graph</code>.
   * 
   * @param node1
   *          the node to test for adjacency with node2
   * @param node2
   *          the node to test for adjacency with node1
   * @return true, if node1 and node2 are adjacent in this <code>Graph</code>
   *         (there is an edge between them), and false otherwise
   * @throws NoSuchNodeException
   *           if node1 or node2 are not in this <code>Graph</code>
   */
  // areAdjacent
  public boolean areAdjacent(Node<T> node1, Node<T> node2) throws NoSuchNodeException {
    if (nodeToNeighbours.containsKey(node1) && nodeToNeighbours.containsKey(node2)) {
      return nodeToNeighbours.get(node1).contains(node2);

    } else {
      throw new NoSuchNodeException();
    }
  }

  /**
   * Returns the number of nodes in this <code>Graph</code>.
   * 
   * @return the number of nodes in this <code>Graph</code>
   */
  public int getNumNodes() {
    return getNodes().size();
  }

  /**
   * Returns the number of edges in this <code>Graph</code>.
   * 
   * @return the number of edges in this <code>Graph</code>
   */
  public int getNumEdges() {
    int total = 0;
    for (Node<T> node : getNodes()) {
      total += getNeighbours(node).size();
    }
    return total / 2; // the graph is undirected
  }

  /**
   * Adds a new <code>Node</code> with the given ID and value to this
   * <code>Graph</code>, if there is not a <code>Node</code> with the given ID
   * in this <code>Graph</code>.
   * 
   * @param id
   *          the ID of the new <code>Node</code>
   * @param value
   *          the value of the new <code>Node</code>
   */
  public void addNode(int id, T value) {
    boolean idNotIn = true;
    // Loop through the nodes to try and find one with the parameter id
    for (Node<T> node : nodeToNeighbours.keySet()) {
      if (node.getId() == id) {
        idNotIn = false;
      }
    }
    if (idNotIn) {
      nodeToNeighbours.put(new Node<T>(id, value), Collections.emptySet());
    }
  }

  /**
   * Adds an edge between the given nodes in this <code>Graph</code>. If there
   * is already an edge between node1 and node2, does nothing. A self-edge is
   * not added.
   * 
   * @param node1
   *          the node to add an edge to and from node2
   * @param node2
   *          the node to add an edge to and from node1
   * @throws NoSuchNodeException
   *           if node1 or node2 is not in this <code>Graph</code>
   */
  // addEdge
  public void addEdge(Node<T> node1, Node<T> node2) throws NoSuchNodeException {
    // Check if the nodes are in the graph
    if (nodeToNeighbours.containsKey(node1) && nodeToNeighbours.containsKey(node2)) {
      if (!this.areAdjacent(node1, node2)) {
        // Only add edge if the parameter nodes are no equal
        if (!node1.equals(node2)) {
          TreeSet<Node<T>> newSet1 = new TreeSet<Node<T>>(nodeToNeighbours.get(node1));
          newSet1.add(node2);
          nodeToNeighbours.replace(node1, newSet1);
          TreeSet<Node<T>> newSet2 = new TreeSet<Node<T>>(nodeToNeighbours.get(node2));
          newSet2.add(node1);
          nodeToNeighbours.replace(node2, newSet2);
        }
      }
    } else {
      throw new NoSuchNodeException();
    }
  }

  /**
   * Adds an edge between the nodes with the given IDs in this
   * <code>Graph</code>.
   * 
   * @param id1
   *          ID of the node to add an edge to and from
   * @param id2
   *          ID of the node to add an edge to and from
   * @throws NoSuchNodeException
   *           if there is no <code>Node</code> with ID id1 or ID id2 in this
   *           Graph
   */
  // addEdge
  public void addEdge(int id1, int id2) throws NoSuchNodeException {
    // Attempt to initialize and declare nodes with id's provided by the
    // parameter
    Node<T> id1Node = this.getNode(id1);
    Node<T> id2Node = this.getNode(id2);
    if (!this.areAdjacent(id1Node, id2Node)) {
      if (!id1Node.equals(id2Node)) {
        TreeSet<Node<T>> newSet1 = new TreeSet<Node<T>>(nodeToNeighbours.get(id1Node));
        newSet1.add(id2Node);
        nodeToNeighbours.replace(id1Node, newSet1);
        TreeSet<Node<T>> newSet2 = new TreeSet<Node<T>>(nodeToNeighbours.get(id2Node));
        newSet2.add(id1Node);
        nodeToNeighbours.replace(id2Node, newSet2);
      }
    }
  }

  @Override
  public String toString() {
    String result = String.format("Number of nodes: %d\nNumber of edges: %d\n", getNumNodes(),
        getNumEdges());

    for (Node<T> node : getNodes()) {
      result += String.format("%s is adjacent to: ", node);
      for (Node<T> neighbour : getNeighbours(node)) {
        result += String.format("%s ", neighbour);
      }
      result += "\n";
    }
    return result;
  }
}
