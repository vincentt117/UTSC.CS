package backend;

import java.util.ArrayList;
import java.util.Collections;

/**
 * A class that represents a <code>ResultItinerary</code>.
 * 
 * @author Ciel
 *
 */

public class ResultItinerary {

  private ArrayList<Itinerary> resItinerary;

  /**
   * Creates a new instance of a <code>ResultItinerary</code>.
   * 
   * @param resItinerary
   *          the list of <code>Itineraries</code>
   */

  public ResultItinerary(ArrayList<Itinerary> resItinerary) {
    this.resItinerary = resItinerary;
  }

  /**
   * Removes a specific Itinerary inside ResultItinerary.
   * 
   * @param itinerary
   *          the itinerary to be removed
   */
  public void removeItinerary(Itinerary itinerary) {
    for (Itinerary i : this.resItinerary) {
      if (i.equals(itinerary)) {
        resItinerary.remove(i);
      }
    }
  }

  /**
   * Sorts the <code>ResultItinerary</code> by cost.
   * 
   * @return the sorted <code>ResultItinerary</code> by cheapest to expensive.
   */
  public ResultItinerary sortByCost() {
    // store all the costs in a new array
    ArrayList<Double> costs = new ArrayList<>();
    for (Itinerary i : this.resItinerary) {
      costs.add(i.getTotalCost());
    }
    // sort that array
    Collections.sort(costs);
    // match the itineraries with the corresponding costs
    ArrayList<Itinerary> sortedCost = new ArrayList<Itinerary>();
    for (double c : costs) {
      for (Itinerary i : this.resItinerary) {
        if (i.getTotalCost() == c && !sortedCost.contains(i)) {
          sortedCost.add(i);
        }
      }
    }
    ResultItinerary sorted = new ResultItinerary(sortedCost);
    return sorted;
  }

  /**
   * Sorts the <code>ResultItinerary</code> by cost.
   * 
   * @return the sorted <code>ResultItinerary</code> by least amount of total
   *         time to most.
   */
  public ResultItinerary sortByTime() {
    // store all the times in a new array
    ArrayList<Long> times = new ArrayList<>();
    for (Itinerary i : this.resItinerary) {
      times.add(i.getTotalTime());
    }
    // sort that array
    Collections.sort(times);
    // match the itineraries with the corresponding times
    ArrayList<Itinerary> sortedTime = new ArrayList<Itinerary>();
    for (long t : times) {
      for (Itinerary i : this.resItinerary) {
        if (i.getTotalTime() == t && !sortedTime.contains(i)) {
          sortedTime.add(i);
        }
      }
    }
    ResultItinerary sorted = new ResultItinerary(sortedTime);
    return sorted;
  }

  /**
   * Returns the ArrayList representation of <code>ResultItinerary</code>
   * object.
   * 
   * @return the ArrayList representation of resItinerary
   */
  public ArrayList<Itinerary> getResItinerary() {
    return resItinerary;
  }

  /**
   * Modifies the <code>ResultItinerary</code> object.
   * 
   * @param resItinerary
   *          the resItinerary to set
   */
  public void setResItinerary(ArrayList<Itinerary> resItinerary) {
    this.resItinerary = resItinerary;
  }

  /*
   * (non-Javadoc)
   * 
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString() {
    return " [resItinerary=" + resItinerary + "]";
  }

  /*
   * (non-Javadoc)
   * 
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (obj == null) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    ResultItinerary other = (ResultItinerary) obj;
    if (resItinerary == null) {
      if (other.resItinerary != null) {
        return false;
      }
    } else if (!resItinerary.equals(other.resItinerary)) {
      return false;
    }
    return true;
  }

}
