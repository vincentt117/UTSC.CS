package backend;

import java.util.Date;

public class Client extends Account implements java.io.Serializable {

  private static final long serialVersionUID = 1L;
  private String address;
  private String creditCardNumber;
  private Date creditCardExpiry;

  /**
   * Creates a new instance of the Client with the parameter.
   * 
   * @param email
   *          Email address of the <code>client</code>
   * @param firstName
   *          First Name of the <code>client</code>
   * @param lastName
   *          Last Name of the <code>client</code>
   * @param address
   *          Address of the <code>client</code>
   * @param creditCardNumber
   *          Credit card # of the <code>client</code>
   * @param creditCardExpiry
   *          Expiration date of teh <code>client</code>'s credit card
   */
  public Client(String email, String firstName, String lastName, String address,
      String creditCardNumber, Date creditCardExpiry) {
    super(email, firstName, lastName);
    this.address = address;
    this.creditCardNumber = creditCardNumber;
    this.creditCardExpiry = creditCardExpiry;
  }

  /**
   * Given a Itinerary, removes that Itinerary from the itinerary of the Client.
   * 
   * @param booking
   *          The Itinerary or flights to be removed from the itinerary
   */
  // this method could also be overloaded to allow for only the ids to delete
  // the flight for more flexibility
  /*
   * public void cancelFlight(Itinerary booking) { bookings.remove(booking); }
   */

  /**
   * Given a Itinerary, books that Itinerary for the client.
   * 
   * @param booking
   *          The Itinerary or flights to be booked
   */
  /*
   * public void purchaseFlight(Itinerary booking) { bookings.add(booking); }
   */

  /**
   * Given an Itinerary, calculate the total cost of that Itinerary.
   * 
   * @return cost a double value representing the cost
   */
  /*
   * public double calculateTotalCost(Itinerary itinerary) { return
   * itinerary.getTotalCost(); }
   */

  /**
   * Returns that total cost of all Itineraries booked by the client.
   * 
   * @return cost a double value representing the cost
   */
  /*
   * public double displayTotalCost() { double totalCost = 0; for (Itinerary i :
   * bookings) { totalCost += i.getTotalCost(); } return totalCost; }
   */

  /**
   * Returns the current mailing address of a customer as a string Some examples
   * of this is L1V 6Y9, or 1500 Queens Street, Toronto.
   * 
   * @return the address The mailing address of the client represented by a
   *         String
   */
  public String getAddress() {
    return address;
  }

  /**
   * Set the mailing address of the client.
   * 
   * @param address
   *          the address to set The mailing address of the client represented
   *          by a String
   */
  public void setAddress(String address) {
    this.address = address;
  }

  /**
   * Return the credit card number of the <code>client</code>.
   * 
   * @return the creditCardNumber
   */
  public String getCreditCardNumber() {
    return creditCardNumber;
  }

  /**
   * Set the credit card number to the parameter string.
   * 
   * @param creditCardNumber
   *          the creditCardNumber to set
   */
  public void setCreditCardNumber(String creditCardNumber) {
    this.creditCardNumber = creditCardNumber;
  }

  /**
   * Return the credit card expiration date of the <code>client</code>.
   * 
   * @return the creditCardExpiry
   */
  public Date getCreditCardExpiry() {
    return creditCardExpiry;
  }

  /**
   * Set the credit card expiration date to the parameter string.
   * 
   * @param creditCardExpiry
   *          the creditCardExpiry to set
   */
  public void setCreditCardExpiry(Date creditCardExpiry) {
    this.creditCardExpiry = creditCardExpiry;
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
    Client other = (Client) obj;
    if (address == null) {
      if (other.address != null) {
        return false;
      }
    } else if (!address.equals(other.address)) {
      return false;
    }
    if (creditCardExpiry == null) {
      if (other.creditCardExpiry != null) {
        return false;
      }
    } else if (!creditCardExpiry.equals(other.creditCardExpiry)) {
      return false;
    }
    if (creditCardNumber != other.creditCardNumber) {
      return false;
    }
    return true;
  }

  @Override
  public String toString() {
    return "Client [" + super.toString() + ", address = " + address + ", creditCardNumber = "
        + creditCardNumber + ", creditCardExpiry = " + creditCardExpiry + "]";
  }

}
