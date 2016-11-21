/**
 * 
 */
package classtests;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Date;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Flight;
import backend.Itinerary;
import backend.Trip;

/**
 * @author lovehela
 *
 */
public class ItineraryTest {

  private Itinerary testItinerary;
  private ArrayList<Trip> trips;
  
  private Flight flight1;
  private String flightNumber1;
  private String airline1;
  private Date departureTime1;
  private Date arrivalTime1;
  private String origin1;
  private String destination1;
  private double cost1;
  
  private Flight flight2;
  private String flightNumber2;
  private String airline2;
  private Date departureTime2;
  private Date arrivalTime2;
  private String origin2;
  private String destination2;
  private double cost2;
  
  private Flight flight3;
  private String flightNumber3;
  private String airline3;
  private Date departureTime3;
  private Date arrivalTime3;
  private String origin3;
  private String destination3;
  private double cost3;
  
  /**
   * @throws java.lang.Exception
   */
  @Before
  public void setUp() throws Exception {
    // make a list of trips to for the parameter needed to make an Itinerary
    trips = new ArrayList<>();
    
    
    // make each successive flight
    flightNumber1 = "342435";
    airline1 = "Toronto";
    departureTime1 = new Date(435643);
    arrivalTime1 = new Date(35125153);
    origin1 = "Toronto";
    destination1 = "Peterborough";
    cost1 = 100;
    flight1 = new Flight(flightNumber1, departureTime1, arrivalTime1, airline1, origin1, destination1, cost1);
    
    flightNumber2 = "343gdl;gs";
    airline2 = "Peterborough";
    departureTime2 = new Date(35125153);
    arrivalTime2 = new Date(45125153);
    origin2 = "Peterborough";
    destination2 = "Paris";
    cost2 = 100;
    flight2 = new Flight(flightNumber2, departureTime2, arrivalTime2, airline2, origin2, destination2, cost2);
    
    flightNumber3 = "ugud032489";
    airline3 = "Paris";
    departureTime3 = new Date(45125153);
    arrivalTime3 = new Date(55125153);
    origin3 = "Paris";
    destination3 = "UTSC";
    cost3 = 100;
    flight3 = new Flight(flightNumber3, departureTime3, arrivalTime3, airline3, origin3, destination3, cost3);
    
    // add them to the itinerary
    trips.add(flight1);
    trips.add(flight2);
    trips.add(flight3);
    
    // create the itinerary
    testItinerary = new Itinerary(trips);
  }

  /**
   * @throws java.lang.Exception
   */
  @After
  public void tearDown() throws Exception {
  }
  
  /**
   * Test method for {@link backend.Itinerary#Itinerary()}.
   */
  @Test
  public void testItinerary() {
    trips.add(null);
    try{
      testItinerary = new Itinerary(trips);
    }catch(Exception e){
      fail("Creates an error not specified in the documentation when creating with an itinerary with a null flight: " + e.getStackTrace());;
    }
    trips = null;
    try{
      testItinerary = new Itinerary(trips);
    }catch(Exception e){
      fail("Creates an error not specified in the documentation when creating with an itinerary with a null Itinerary: " + e.getStackTrace());;
    }

  }

  /**
   * Test method for {@link backend.Itinerary#getTotalCost()}.
   */
  @Test
  public void testGetTotalCost() {
    assertEquals("Test getTotalCost, Expected" + (cost1 + cost2 + cost3) + "returns:" + testItinerary.getTotalCost(), testItinerary.getTotalCost(), (cost1 + cost2 + cost3), 0.001);
  }

  /**
   * Test method for {@link backend.Itinerary#setTotalCost(double)}.
   */
  @Test
  public void testSetTotalCost() {
    // question for Ciel, why would we ever do this, could we set a cost for each flight?
    fail("Not yet implemented"); // TODO
  }

  /**
   * Test method for {@link backend.Itinerary#getTotalTime()}.
   */
  @Test
  public void testGetTotalTime() {
    assertEquals("Test getTotalTime, Expected" + (arrivalTime3.getTime() - departureTime1.getTime()) + "returns:" + testItinerary.getTotalTime(), testItinerary.getTotalTime(), arrivalTime3.getTime() - departureTime1.getTime(), 0.000001);
  }

  /**
   * Test method for {@link backend.Itinerary#setTotalTime(long)}.
   */
  @Test
  public void testSetTotalTime() {
    // same issue as the setTotalCost as this is a list of flights
    fail("Not yet implemented"); // TODO
  }

  /**
   * Test method for {@link backend.Itinerary#getTripList()}.
   */
  @Test
  public void testGetTripList() {
    assertEquals("Test getTripList, Expected" + trips + "returns:" + testItinerary.getTripList(), testItinerary.getTripList(), trips);
  }

  /**
   * Test method for {@link backend.Itinerary#setTripList(java.util.ArrayList)}.
   */
  @Test
  public void testSetTripList() {
    // Here Ciel, it may be easier to abstract the storage of the trips, and make the constructor need nothing to make it
    // then you can add flights to the itineraries using its own special method as it allows more abstraction
    trips = new ArrayList<>();
    
    // make each sucessive flight
    flightNumber1 = "342435";
    airline1 = "Toronto";
    departureTime1 = new Date(0000);
    arrivalTime1 = new Date(35125153);
    origin1 = "Toronto";
    destination1 = "Peterborough";
    cost1 = 100000;
    flight1 = new Flight(flightNumber1, departureTime1, arrivalTime1, airline1, origin1, destination1, cost1);
    
    flightNumber2 = "343gdl;gs";
    airline2 = "Peterborough";
    departureTime2 = new Date(35125153);
    arrivalTime2 = new Date(45125153);
    origin2 = "Peterborough";
    destination2 = "Paris";
    cost2 = 300000;
    flight2 = new Flight(flightNumber2, departureTime2, arrivalTime2, airline2, origin2, destination2, cost2);
    
    flightNumber3 = "ugud032489";
    airline3 = "Paris";
    departureTime3 = new Date(45125153);
    arrivalTime3 = new Date(785125153);
    origin3 = "Paris";
    destination3 = "UTSC";
    cost3 = 1005436;
    flight1 = new Flight(flightNumber3, departureTime3, arrivalTime3, airline3, origin3, destination3, cost3);
    
    // add them to the itinerary
    trips.add(flight1);
    trips.add(flight2);
    trips.add(flight3);
    
    assertEquals("Test getTripList, Expected" + trips + "returns:" + testItinerary.getTripList(), testItinerary.getTripList(), trips);
    assertEquals("Test getTripList changed duration, Expected" + (arrivalTime3.getTime() - departureTime1.getTime()) + "returns:" + testItinerary.getTotalTime(), testItinerary.getTotalTime(), arrivalTime3.getTime() - departureTime1.getTime(), 0.000001);
    assertEquals("Test getTripList changed costs, Expected" + (cost1 + cost2 + cost3) + "returns:" + testItinerary.getTotalCost(), testItinerary.getTotalCost(), (cost1 + cost2 + cost3), 0.001);
  }

  /**
   * Test method for {@link backend.Itinerary#equals(java.lang.Object)}.
   */
  @Test
  public void testEqualsObject() {
    ArrayList<Trip> otherTrips = new ArrayList<>();
    otherTrips.add(flight1);
    otherTrips.add(flight2);
    otherTrips.add(flight3);
    
    Itinerary otherItinerary = new Itinerary(otherTrips);

    assertEquals("Test two itineraries of the came value are equal, Expected: " + otherItinerary + "returns:" + testItinerary, testItinerary, otherItinerary);
  }

}
