/**
 * 
 */
package classtests;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Client;
import backend.Flight;
import backend.Itinerary;
import backend.Trip;

/**
 * @author lovehela
 *
 */
public class ClientTest {
  private String firstName;
  private String lastName;
  private String email;
  private String address;
  private List<Itinerary> bookings;
  private String creditCardNumber;
  private Date creditCardExpiry;
  private Client testClient;
  private double tripCost = 3000;
  
  /**
   * @throws java.lang.Exception
   */
  @Before
  public void setUp() throws Exception {
    address = "1656 Military Trail";
    bookings = new ArrayList<>(); // just make a new booking with arbitrary flights
    bookings.add(createItinerary());
    bookings.add(createItinerary());
    creditCardNumber = "231210";
    creditCardExpiry = new Date(2139210);
    String email = "1432142@gmail.com";
    String firstName = "Taylor"; 
    String lastName = "Rose";
    testClient = new Client(email, firstName, lastName, address, creditCardNumber, creditCardExpiry);
  }
  
  /**
   * @throws java.lang.Exception
   */
  public Itinerary createItinerary(){
    ArrayList<Trip> trips = new ArrayList<>();
    trips.add(new Flight("1421esgp", new Date(100), new Date(1000), "Toronto Metro", "Toronto", "Paris", tripCost));
    return new Itinerary(trips);
  }

  /**
   * @throws java.lang.Exception
   */
  @After
  public void tearDown() throws Exception {
  }

  /**
   * Test method for {@link backend.Client#cancelFlight(backend.Itinerary)}.
   */
  /*@Test
  public void testCancelFlight(){
    bookings.remove(bookings.get(0));
    Client expectedClient = new Client(age, address, bookings, creditCardNumber, creditCardExpiry);
    testClient.cancelFlight(bookings.get(0));
    assertEquals("Test cancelFlight failed, Expected: " + expectedClient + "Returned" + testClient, expectedClient, testClient);
  }*/

  /**
   * Test method for {@link backend.Client#purchaseFlight(backend.Itinerary)}.
   */    
  /*@Test
  public void testPurchaseFlight(){
    bookings.add(bookings.get(0));
    Client expectedClient = new Client(age, address, bookings, creditCardNumber, creditCardExpiry);
    testClient.cancelFlight(bookings.get(0));
    assertEquals("Test purchaseFlight, Expected :" + expectedClient + " Returns: " + testClient, expectedClient, testClient);
  }*/

  /**
   * Test method for {@link backend.Client#calculateTotalCost(backend.Itinerary)}.
   */
  /*@Test
  public void testCalculateTotalCost() {
    double expectedCost = tripCost; // here all trips are the same cost
    double actualCost = testClient.calculateTotalCost(bookings.get(0));
    assertEquals("Test calculateTotalCost, Expected :" + expectedCost + " Returns: " + actualCost, expectedCost, actualCost, 0.00000001);
  }*/

  /**
   * Test method for {@link backend.Client#displayTotalCost()}.
   */
  /*@Test
  public void testDisplayTotalCost() {
    double expectedCost = tripCost*2; // basically since we have two trips costing the same, the expected cost is 2 time the amount in the trip
    double actualCost = testClient.displayTotalCost();
    assertEquals("Test calculateTotalCost, Expected :" + expectedCost + " Returns: " + actualCost, expectedCost, actualCost, 0.00000001);
  }*/


  /**
   * Test method for {@link backend.Client#getAddress()}.
   */
  @Test
  public void testGetAddress() {
    assertEquals("test getAddress, Expected: " + address + " Returns: " + testClient.getAddress() + " Expected: " + address, testClient.getAddress(), address);
  }

  /**
   * Test method for {@link backend.Client#setAddress(java.lang.String)}.
   */
  @Test
  public void testSetAddress() {
    address = "1000 Elsmere Road";
    testClient.setAddress(address);
    assertEquals("Test setAddress, Expected: " + address + " Returns: " + testClient.getAddress() + " Expected: " + address, testClient.getAddress(), address);
  }

  /**
   * Test method for {@link backend.Client#getCreditCardNumber()}.
   */
  @Test
  public void testGetCreditCardNumber() {
    assertEquals("Test getCreditCardNumber, Expected: " + creditCardNumber + " Returns: " + testClient.getCreditCardNumber() + " Expected: " + creditCardNumber, testClient.getCreditCardNumber(), creditCardNumber);
  }

  /**
   * Test method for {@link backend.Client#setCreditCardNumber(int)}.
   */
  @Test
  public void testSetCreditCardNumber() {
    creditCardNumber = "3432";
    testClient.setCreditCardNumber(creditCardNumber);
    assertEquals("Test setCreditCardNumber, Expected: " + creditCardNumber + " Returns: " + testClient.getCreditCardNumber() + " Expected: " + creditCardNumber, testClient.getCreditCardNumber(), creditCardNumber);
  }

  /**
   * Test method for {@link backend.Client#getCreditCardExpiry()}.
   */
  @Test
  public void testGetCreditCardExpiry() {
    assertEquals("Test getCreditCardExpiry, Expected: " + creditCardExpiry + " Returns: " + testClient.getCreditCardExpiry() + " Expected: " + creditCardExpiry, testClient.getCreditCardExpiry(), creditCardExpiry);
  }

  /**
   * Test method for {@link backend.Client#setCreditCardExpiry(java.util.Date)}.
   */
  @Test
  public void testSetCreditCardExpiry() {
    creditCardExpiry = new Date(2132414);
    testClient.setCreditCardExpiry(creditCardExpiry);
    assertEquals("Test setCreditCardExpiry, Expected: " + creditCardExpiry + " Returns: " + testClient.getCreditCardExpiry() + " Expected: " + creditCardExpiry, testClient.getCreditCardExpiry(), creditCardExpiry);
  }

}
