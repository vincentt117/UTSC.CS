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
import backend.ResultItinerary;
import backend.Trip;

/**
 * @author lovehela
 *
 */
public class ResultingItineraryTest {

  private ResultItinerary testRI;
  private ArrayList<Itinerary> itineraries;
  private Itinerary itinerary1;
  private Date itinerary1d1;
  private Date itinerary1d2;
  private double itinerary1Cost;
  
  private Itinerary itinerary2;
  private Date itinerary2d1;
  private Date itinerary2d2;
  private double itinerary2Cost;
  
  private Itinerary itinerary3;
  private Date itinerary3d1;
  private Date itinerary3d2;
  private double itinerary3Cost;
  
  /**
   * @throws java.lang.Exception
   */
  @Before
  public void setUp() throws Exception {
    itineraries = new ArrayList<>();
    
    // first create the itineraries
    itinerary1d1 = new Date(77900);
    itinerary1d2 = new Date(97900);
    itinerary1Cost = 3000;
    itinerary1 = createItinerary(itinerary1d1, itinerary1d2, itinerary1Cost);
    
    itinerary2d1 = new Date(67900);
    itinerary2d2 = new Date(77900);
    itinerary2Cost = 5000;
    itinerary2 = createItinerary(itinerary2d1, itinerary2d2, itinerary2Cost);
    
    itinerary3d1 = new Date(87900);
    itinerary3d2 = new Date(117900);
    itinerary3Cost = 1000;
    itinerary3 = createItinerary(itinerary3d1, itinerary3d2, itinerary3Cost);
    
    // now add them to the itinerary list
    itineraries.add(itinerary1); // same comment with itineraries as with initialization, this is annoying
    itineraries.add(itinerary2);
    itineraries.add(itinerary3);
    
    testRI = new ResultItinerary(itineraries);
  }
  
  public Itinerary createItinerary(Date d1, Date d2, double cost){ 
    // honestly, the rest of the stuff doesn't really matter as they are strings
    ArrayList<Trip> trips = new ArrayList<>();
    trips.add(new Flight("1421esgp", d1, d2, "Toronto Metro", "Toronto", "Paris", cost));
    return new Itinerary(trips);
  }

  /**
   * Test method for {@link backend.Itinerary#ResultItinerary()}.
   */
  @Test
  public void testResultItinerary() {
   itineraries.add(null);
    try{
      testRI = new ResultItinerary(itineraries);
    }catch(Exception e){
      fail("Creates an error not specified in the documentation when creating with an null itinerary: " + e.getStackTrace());;
    }
    itineraries = null;
    try{
      testRI = new ResultItinerary(itineraries);
    }catch(Exception e){
      fail("Creates an error not specified in the documentation when creating with an null: " + e.getStackTrace());;
    }

  }
  /**
   * @throws java.lang.Exception
   */
  @After
  public void tearDown() throws Exception {
  }

  /**resItinerary
   * Test method for {@link backend.ResultItinerary#sortByCost()}.
   */
  @Test
  public void testSortByCost() {
    // first put them in the proper order
    itineraries = new ArrayList<>();
    itineraries.add(itinerary3);
    itineraries.add(itinerary1);
    itineraries.add(itinerary2);
    assertEquals("Tested sortByCost, Expected: " + itineraries + " Returns: " + testRI.sortByCost(), itineraries, testRI.sortByCost().getResItinerary());
  }

  /**
   * Test method for {@link backend.ResultItinerary#sortByTime()}.
   */
  @Test
  public void testSortByTime() {
    itineraries = new ArrayList<>();
    itineraries.add(itinerary2);
    itineraries.add(itinerary1);
    itineraries.add(itinerary3);
    assertEquals("Tested sortByTime, Expected: " + itineraries + " Returns: " + testRI.sortByCost(), itineraries, testRI.sortByTime().getResItinerary());
  }

  /**
   * Test method for {@link backend.ResultItinerary#getResItinerary()}.
   */
  @Test
  public void testGetResItinerary() {
    assertEquals("Tested getResItinerary, Expected: " + itineraries + " Returns: " + testRI.sortByCost(), itineraries, testRI.getResItinerary());
  }

  /**
   * Test method for {@link backend.ResultItinerary#setResItinerary(java.util.ArrayList)}.
   */
  @Test
  public void testSetResItinerary() {
    itineraries = new ArrayList<>();
    itineraries.add(itinerary2);
    itineraries.add(itinerary1);
    itineraries.add(itinerary3);
    testRI.setResItinerary(itineraries);
    assertEquals("Tested getResItinerary, Expected: " + itineraries + " Returns: " + testRI.sortByCost(), itineraries, testRI.getResItinerary());
  }

}
