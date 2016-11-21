/**
 * 
 */
package classtests;

import static org.junit.Assert.*;

import java.util.Date;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Flight;

/**
 * @author lovehela
 *
 */
public class FlightTest {

  private Flight testFlight;
  private String flightNumber;
  private Date departureTime;
  private Date arrivalTime;
  private String airline;
  private String origin;
  private String destination;
  private double cost;
  
  /**
   * @throws java.lang.Exception
   */
  @Before
  public void setUp() throws Exception {
    flightNumber = "1423rda";
    departureTime = new Date(120103214);
    arrivalTime = new Date(214243254);
    airline = "UofT";
    origin = "UTSC";
    destination = "Scarborough Town Center";
    cost = 0;
    testFlight = new Flight(flightNumber, departureTime, arrivalTime, airline, origin, destination, cost);
  }

  /**
   * @throws java.lang.Exception
   */
  @After
  public void tearDown() throws Exception {
  }

  /**
   * Test method for {@link backend.Flight#getTripDuration()}.
   */
  @Test
  public void testGetTripDuration() {
    assertEquals("Trip Duration Returns improper Trip Duration: " + testFlight.getTripDuration() + "Expected:" + (arrivalTime.getTime() - departureTime.getTime()), testFlight.getTripDuration(), arrivalTime.getTime() - departureTime.getTime());
  }


  /**
   * Test method for {@link backend.Flight#getFlightNumber()}.
   */
  @Test
  public void testGetFlightNumber() {
    assertEquals("Test getFlightNumber, Returns improper Flight number expected" + flightNumber + "returns:" + testFlight.getFlightNumber(), testFlight.getFlightNumber(), flightNumber);
  }

  /**
   * Test method for {@link backend.Flight#getAirline()}.
   */
  @Test
  public void testGetAirline() {
    assertEquals("Test getAirline, Returns: " + testFlight.getAirline() + " Expected: " + airline, testFlight.getAirline(), airline);
  }

  /**
   * Test method for {@link backend.Flight#setAirline(java.lang.String)}.
   */
  @Test
  public void testSetAirline() {
    airline = "Different Airline";
    testFlight.setAirline(airline);
    assertEquals("Test setAirline, Returns: " + testFlight.getAirline() + " Expected: " + airline, testFlight.getAirline(), airline);
  }

  /**
   * Test method for {@link backend.Flight#equals(java.lang.Object)}.
   */
  @Test
  public void testEqualsObject() {
    Flight otherFlight = new Flight(flightNumber, departureTime, arrivalTime, airline, origin, destination, cost);
    assertEquals("Tested equals to identical flight Expected: " + otherFlight + " Compared: " + testFlight, testFlight, otherFlight);
  }

}
