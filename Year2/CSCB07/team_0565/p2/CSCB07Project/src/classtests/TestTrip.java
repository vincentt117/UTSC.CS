package classtests;

import static org.junit.Assert.*;

import java.util.Date;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Flight;
import backend.Trip;

public class TestTrip {

  private Trip testTrip;
  private Date departureTime;
  private Date arrivalTime;
  private String origin;
  private String destination;
  private double cost;
  
  @Before
  public void setUp() throws Exception {
    departureTime = new Date(4721894);
    arrivalTime = new Date(909543554);
    origin = "Toronto";
    destination = "UTSC";
    cost = 100;
    testTrip = new Flight("", departureTime, arrivalTime, "", origin, destination, cost);
  }

  @After
  public void tearDown() throws Exception {
  }

  @Test
  public void testGetDepartureTime() {
    assertEquals("Test getDepartureTime, Expected" + departureTime + "returns:" + testTrip.getDepartureTime(), testTrip.getDepartureTime(), departureTime);
  }

  @Test
  public void testSetDepartureTime() {
    departureTime = new Date(352945);
    testTrip.setDepartureTime(departureTime);
    assertEquals("Test setDepartureTime, Expected" + departureTime + "returns:" + testTrip.getDepartureTime(), testTrip.getDepartureTime(), departureTime);
  }

  @Test
  public void testGetArrivalTime() {
    assertEquals("Test getArrivalTime, Expected" + arrivalTime + "returns:" + testTrip.getArrivalTime(), testTrip.getArrivalTime(), arrivalTime);
  }

  @Test
  public void testSetArrivalTime() {
    arrivalTime = new Date(557352945);
    testTrip.setArrivalTime(arrivalTime);
    assertEquals("Test setArrivalTime, Expected" + arrivalTime + "returns:" + testTrip.getArrivalTime(), testTrip.getArrivalTime(), arrivalTime);
  }

  @Test
  public void testGetOrigin() {
    assertEquals("Test setOrigin, Expected" + origin + "returns:" + testTrip.getOrigin(), testTrip.getOrigin(), origin);
  }

  @Test
  public void testSetOrigin() {
    origin = "569 Oshawa";
    testTrip.setOrigin(origin);
    assertEquals("Test getOrigin, Expected" + origin + "returns:" + testTrip.getOrigin(), testTrip.getOrigin(), origin);
  }

  @Test
  public void testGetDestination() {
    assertEquals("Test getDestination, Expected" + destination + "returns:" + testTrip.getDestination(), testTrip.getDestination(), destination);
  }

  @Test
  public void testSetDestination() {
    destination = "569 Oshawa";
    testTrip.setDestination(destination);
    assertEquals("Test setDestination, Expected" + destination + "returns:" + testTrip.getDestination(), testTrip.getDestination(), destination);
  }

  @Test
  public void testGetCost() {
    assertEquals("Test getCost, Expected" + cost + "returns:" + testTrip.getCost(), testTrip.getCost(), cost, 0.0000001);
  }

  @Test
  public void testSetCost() {
    cost = 560;
    testTrip.setCost(cost);
    assertEquals("Test setCost, Expected" + cost + "returns:" + testTrip.getCost(), testTrip.getCost(), cost, 0.0000001);
  }

  @Test
  public void testGetTripDuration() {
    double duration = arrivalTime.getTime() - departureTime.getTime();
    assertEquals("Test getTripDuration, Expected" + duration + "returns:" + testTrip.getTripDuration(), testTrip.getTripDuration(), duration, 0.0000001);
  }

  @Test
  public void testSetTripDuration() {
    // I'm not sure what to do with this method, as when we change the duration, we must also have the
    // departure time or arrival time changed, must ask Ciel if this should be taken out
    fail("Not yet implemented");
  }

}
