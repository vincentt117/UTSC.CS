package backend;

import java.util.ArrayList;

/**
 * A class that represents an <code>Itinerary</code>.
 * 
 * @author Ciel
 *
 */
public class Itinerary {

  private double totalCost;
  private long totalTime;
  private ArrayList<Trip> tripList;

  /**
   * Creates a new instance of an <code>Itinerary</code>.
   * 
   * @param tripList
   *          the <code>Trip</code>s that will make up the
   *          <code>Itinerary</code>
   */
  public Itinerary(ArrayList<Trip> tripList) {
    this.tripList = tripList;
    double tempCost = 0;
    long tempDuration = 0;
    for (Trip o : tripList) {
      tempCost += o.getCost();
      tempDuration += o.getTripDuration();
    }
    this.totalCost = tempCost;
    this.totalTime = tempDuration;
  }

  /**
   * Returns the layover time between each <code>Trip</code> in the
   * <code>Itinerary</code>.
   * 
   * @return the list of layover time
   */
  public ArrayList<Long> getLayoverTime() {
    ArrayList<Long> layover = new ArrayList<Long>();
    long arrivalTime = 0;
    for (Trip o : tripList) {
      if (arrivalTime == 0) {
        arrivalTime = o.getArrivalTime().getTime();
      } else {
        long layoverTime = o.getDepartureTime().getTime() - arrivalTime;
        layover.add(layoverTime);
        arrivalTime = o.getArrivalTime().getTime();
      }
    }
    return layover;
  }

  /**
   * Returns the total cost of the <code>Itinerary</code>.
   * 
   * @return the totalCost
   */
  public double getTotalCost() {
    return totalCost;
  }

  /**
   * Modifies the total cost of the <code>Itinerary</code>..
   * 
   * @param totalCost
   *          the totalCost to set
   */
  public void setTotalCost(double totalCost) {
    this.totalCost = totalCost;
  }

  /**
   * Returns the total travel time of the <code>Itinerary</code>.
   * 
   * @return the totalTime
   */
  public long getTotalTime() {
    return totalTime;
  }

  /**
   * Modifies the total travel time of the <code>Itinerary</code>.
   * 
   * @param totalTime
   *          the totalTime to set
   */
  public void setTotalTime(long totalTime) {
    this.totalTime = totalTime;
  }

  /**
   * Returns the list of <code>Trip</code>s contained in the
   * <code>Itinerary</code>.
   * 
   * @return the tripList
   */
  public ArrayList<Trip> getTripList() {
    return tripList;
  }

  /**
   * Modifies the list of <code>Trip</code>s contained in the
   * <code>Itinerary</code>.
   * 
   * @param tripList
   *          the tripList to set
   */
  public void setTripList(ArrayList<Trip> tripList) {
    this.tripList = tripList;
  }

  public boolean bookSeat(){
    boolean bookedAllSeats = true; // keep track if we booked the flights
    int numBooked = 0; // to keep track of how many flights were booked so we and stop the process
                       // if there is an error
    for (Trip o : this.getTripList()) {
     bookedAllSeats = bookedAllSeats && o.bookSeats(1);
      // if we couldn't book everything, then stop, return the previous seats and return the failure
      // and make sure to release the flights already booked
      if(!bookedAllSeats){
        // we restart the loop
        for (Trip v : this.getTripList()){
          if(numBooked <=0){
            return bookedAllSeats;
          }
          v.addNewSeats(1);
          numBooked--;
        }
      }
      numBooked++;
    }
    return bookedAllSeats;
  }

  public void removeBooking(){
    // since we are only releasing a client's booking, we only need to increment the seats by 1
    for (Trip o : this.getTripList()) {
      o.addNewSeats(1);
    }
  }

  /*
   * (non-Javadoc)
   * 
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString() {
    String retString = "";
    for (Trip t : tripList) {
      retString = t.toString() + "\n";
    }
    retString += String.format("%.2f", this.getTotalCost()) + "\n";
    retString += String.format("%.2f", (double) this.getTotalTime() / 3600000) + "\n";
    return retString;
  }

  /**
   * Looks through the itinerary to see if there is any space available in the flights
   *
   * @return the amount of space available in the itinerary as an int
     */
  public int getLowestNumSeats(){
    // basically a method to find if there are any seats in the itinerary to see if it can be booked
    int lowestSeat = -1;
    // just go through the code and look to see if there are any lower seats
    for(Trip trip : tripList){
      if(trip.getNumSeats() < lowestSeat || lowestSeat == -1){
        lowestSeat = trip.getNumSeats();
      }
    }
    return lowestSeat;
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
    Itinerary other = (Itinerary) obj;
    if (Double.doubleToLongBits(totalCost) != Double.doubleToLongBits(other.totalCost)) {
      return false;
    }
    if (totalTime != other.totalTime) {
      return false;
    }
    if (tripList == null) {
      if (other.tripList != null) {
        return false;
      }
    } else if (!tripList.equals(other.tripList)) {
      return false;
    }
    return true;
  }

}
