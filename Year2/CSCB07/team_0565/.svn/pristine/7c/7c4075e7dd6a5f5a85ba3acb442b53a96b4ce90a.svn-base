package backend;

import java.util.Date;

/**
 * A class that represents a <code> Flight </code>.
 * 
 * @author lovehela
 *
 */
public class Flight extends Trip {

  private static final long serialVersionUID = 1L;
  private String flightNumber;
  private String airline;

  /**
   * Creates a new instance of <code> Flight </code>.
   * 
   * @param flightNumber
   *          unique flight number of flight
   * @param departureTime
   *          departure time of flight
   * @param arrivalTime
   *          arrival time of flight
   * @param airline
   *          airline company of flight
   * @param origin
   *          place of origin of flight
   * @param destination
   *          place of destination of flight
   * @param cost
   *          cost of flight ticket
   */
  public Flight(String flightNumber, Date departureTime, Date arrivalTime, String airline,
      String origin, String destination, double cost, String numSeats) {
    super(departureTime, arrivalTime, origin, destination, cost, numSeats);
    this.flightNumber = flightNumber;
    this.airline = airline;
  }
  

  /**
   * Returns the representation of the unique flight id given to the flights.
   * 
   * @return the flightNumber Returns the flight number as a unique alphanumeric
   *         String
   */
  public String getFlightNumber() {
    return flightNumber;
  }

  // No setFlightNumber as flight number is a id
  // Ids are ususally not changed but I decided to add it in a commentin case
  // different design decision later

  /**
   * Returns the airline that the current flight runs by.
   * 
   * @return airline A String representing the company running that specific
   *         flight
   */
  public String getAirline() {
    return airline;
  }

  /**
   * Sets the airline of the flight to be a different value.
   * 
   * @param airline
   *          A string representing the company that runs the flight
   */
  public void setAirline(String airline) {
    this.airline = airline;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    if (!super.equals(o)) return false;

    Flight flight = (Flight) o;

    if (this.getTripDuration() != flight.getTripDuration()) return false;
    if (this.getNumSeats() != flight.getNumSeats()) return false;
    if (Double.compare(flight.getCost(), this.getCost()) != 0) return false;
    if (flightNumber != null ? !flightNumber.equals(flight.flightNumber) : flight.flightNumber != null)
      return false;
    return airline != null ? airline.equals(flight.airline) : flight.airline == null;

  }

  @Override
  public int hashCode() {
    int result = super.hashCode();
    long temp;
    result = 31 * result + (flightNumber != null ? flightNumber.hashCode() : 0);
    result = 31 * result + (airline != null ? airline.hashCode() : 0);
    result = 31 * result + (int) (this.getTripDuration() ^ (this.getTripDuration() >>> 32));
    result = 31 * result + this.getNumSeats();
    temp = Double.doubleToLongBits(this.getCost());
    result = 31 * result + (int) (temp ^ (temp >>> 32));
    return result;
  }

  /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString()
     */
  @Override
  public String toString() {
    return  flightNumber + ";" + super.toString() + ";" + this.getCost() + ";" + this.getNumSeats();

  }

}
