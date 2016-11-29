package backend;

import java.util.Date;

/**
 * A class that represents a <code>Trip</code>.
 * 
 * @author Ciel
 *
 */
public abstract class Trip implements java.io.Serializable {

  private static final long serialVersionUID = 1L;
  private Date departureTime;
  private Date arrivalTime;
  private String origin;
  private String destination;
  private long tripDuration;

  /**
   * Creates a new instance of a <code>Trip</code>.
   * 
   * @param departureTime
   *          the time of departure
   * @param arrivalTime
   *          the time of arrival
   * @param origin
   *          the location of departure
   * @param destination
   *          the location of arrival
   * @param cost
   *          the cost of the trip
   * @param numSeats
   * 		  the number of available seats for the trip
   */
  public Trip(Date departureTime, Date arrivalTime, String origin, String destination,
      double cost, String numSeats) {
    this.departureTime = departureTime;
    this.arrivalTime = arrivalTime;
    this.origin = origin;
    this.destination = destination;
    this.tripDuration = departureTime.getTime() - arrivalTime.getTime();
  }

  /**
   * Returns the departure time of the <code>Trip</code>.
   * 
   * @return the departureTime
   */
  public Date getDepartureTime() {
    return departureTime;
  }

  /**
   * Modifies the departure time of the <code>Trip</code>.
   * 
   * @param departureTime
   *          the departureTime to set
   */
  public void setDepartureTime(Date departureTime) {
    this.departureTime = departureTime;
  }

  /**
   * Returns the arrival time of the <code>Trip</code>.
   * 
   * @return the arrivalTime
   */
  public Date getArrivalTime() {
    return arrivalTime;
  }

  /**
   * Modifies the arrival time of the <code>Trip</code>.
   * 
   * @param arrivalTime
   *          the arrivalTime to set
   */
  public void setArrivalTime(Date arrivalTime) {
    this.arrivalTime = arrivalTime;
  }

  /**
   * Returns the location of departure.
   * 
   * @return the origin
   */
  public String getOrigin() {
    return origin;
  }

  /**
   * Modifies the location of departure.
   * 
   * @param origin
   *          the origin to set
   */
  public void setOrigin(String origin) {
    this.origin = origin;
  }

  /**
   * Returns the destination.
   * 
   * @return the destination
   */
  public String getDestination() {
    return destination;
  }

  /**
   * Modifies the destination.
   * 
   * @param destination
   *          the destination to set
   */
  public void setDestination(String destination) {
    this.destination = destination;
  }


  /**
   * Returns the duration of the <code>Trip</code>.
   * 
   * @return the tripDuration
   */
  public long getTripDuration() {
    return tripDuration;
  }

  /**
   * Modifies the duration of the <code>Trip</code>.
   * 
   * @param tripDuration
   *          the tripDuration to set
   */
  public void setTripDuration(long tripDuration) {
    this.tripDuration = tripDuration;
  }
  
/*
   * (non-Javadoc)
   * 
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString() {
    return departureTime + ";" + arrivalTime + ";" + origin + ";" + destination + ";";
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
    Trip other = (Trip) obj;
    if (arrivalTime == null) {
      if (other.arrivalTime != null) {
        return false;
      }
    } else if (!arrivalTime.equals(other.arrivalTime)) {
      return false;
    }
    if (departureTime == null) {
      if (other.departureTime != null) {
        return false;
      }
    } else if (!departureTime.equals(other.departureTime)) {
      return false;
    }
    if (destination == null) {
      if (other.destination != null) {
        return false;
      }
    } else if (!destination.equals(other.destination)) {
      return false;
    }
    if (origin == null) {
      if (other.origin != null) {
        return false;
      }
    } else if (!origin.equals(other.origin)) {
      return false;
    }
    if (tripDuration != other.tripDuration) {
      return false;
    }
    return true;
  }

}
