/**
 * 
 */
package classtests;

import static org.junit.Assert.*;

import java.util.ArrayList;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Database;
import backend.FlightDatabase;

/**
 * @author lovehela
 *
 */
public class DatabaseTest {

  private Database testDB;
  
  /**
   * @throws java.lang.Exception
   */
  @Before
  public void setUp() throws Exception {
  }

  /**
   * @throws java.lang.Exception
   */
  @After
  public void tearDown() throws Exception {
  }

  /**
   * Test method for {@link backend.Database#readFile(java.lang.String)}.
   */
  @Test
  public void testReadFile() {
    // first we see what happens when the file is given a bad path
    testDB = new FlightDatabase("");
    try{
      testDB.readFile("");
    }catch(Exception e){
      fail("Does not deal with improper inputs, please add to docstring that it throws exceptions");
    }
    // now we see if we can read the samplefile
    try{
      ArrayList<String> actualFileItem = testDB.readFile(System.getProperty("user.dir") + "/src/sampletests/flights1.txt");
      ArrayList<String> expectedFileItem = new ArrayList<>();
      expectedFileItem.add("AC489;2016-09-09 09:09;2016-09-09 13:27;FlightsRUs;Chicago;Los Angelos;300.99\n");
      expectedFileItem.add("KL490;2016-09-30 22:40;2016-10-01 01:59;Go Airline;New York;Boston;532.00\n");
      expectedFileItem.add("KL102;2016-09-30 16:43;2016-09-30 17:15;FlightsRUs;New York;Chicago;290.50\n");
      expectedFileItem.add("UA103;2016-09-30 16:37;2016-09-30 17:22;Go Airline;New York;Chicago;290.00\n");
      assertEquals("Expected: " + expectedFileItem + " Returns: " + actualFileItem, expectedFileItem, actualFileItem);
    }catch(Exception e){
      fail("does not deal with lack of file name, not throws decalaration in docstring");
    }
    // first we see what happens when the file is given another bad input
    testDB = new FlightDatabase(null);
    try{
      testDB.readFile(null);
    }catch(Exception e){
      fail("Does not deal with improper inputs, please add to docstring that it throws exceptions");
    }
  }

}
