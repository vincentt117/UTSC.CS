package classtests;

import static org.junit.Assert.*;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Client;
import backend.Flight;
import backend.FlightDatabase;

public class TestAccount {
  private String email;
  private String firstName;
  private String lastName;
  private Client testAccount;
  private  DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm");

  @Before
  public void setUp() throws Exception {
    email = "pikachu@gmail.com";
    firstName = "pika";
    lastName = "chu";
    testAccount = new Client(email, firstName, lastName, "1235 Scar", "124235435", new Date(21413));
  }

  @After
  public void tearDown() throws Exception {
  }

  @Test
  public void testGetEmail() {
    assertEquals("Expected: " + email + " Returns: " + testAccount.getEmail(), testAccount.getEmail(), email);
  }

  @Test
  public void testSetEmail() {
    email = "hrere";
    testAccount.setEmail(email);
    assertEquals("Expected: " + email + " Returns: " + testAccount.getEmail(), testAccount.getEmail(), email);
  }

  @Test
  public void testGetFirstName() {
    assertEquals("Expected: " + firstName + " Returns: " + testAccount.getFirstName(), testAccount.getFirstName(), firstName);
  }

  @Test
  public void testSetFirstName() {
    firstName = "Terra";
    testAccount.setFirstName(firstName);
    assertEquals("Expected: " + firstName + " Returns: " + testAccount.getFirstName(), testAccount.getFirstName(), firstName);
  }

  @Test
  public void testGetLastName() {
    assertEquals("Expected: " + lastName + " Returns: " + testAccount.getLastName(), testAccount.getLastName(), lastName);
  }

  @Test
  public void testSetLastName() {
    lastName = "Smith";
    testAccount.setLastName(lastName);
    assertEquals("Expected: " + lastName + " Returns: " + testAccount.getLastName(), testAccount.getLastName(), lastName);
  }

  @Test
  public void testSearchItinerary() {
    FlightDatabase testData = new FlightDatabase(System.getProperty("user.dir"));
    try{
      Flight flight = new Flight("12345", format.parse("2016-12-21 12:00"), format.parse("2016-12-21 1:00"), "Paris", "Toronto", "Paris", 1000);
      Flight flight2 = new Flight("1037143", format.parse("2016-12-21 2:00"), format.parse("2016-12-21 4:00"), "Paris", "Paris", "Tokyo", 4000);
      Flight flight3 = new Flight("1067143", format.parse("2016-12-21 4:30"), format.parse("2016-12-21 6:00"), "Paris", "Tokyo", "UTSC", 5000);
      testData.addFlight(flight2);
      testData.addFlight(flight);
      testData.addFlight(flight3);
    } catch(Exception e){
      
    }
    
    testData.serialize(testData.getFlights());
    
    testAccount.searchItinerary("Toronto", "UTSC", new Date(1234)); // the basic case of searching the itineraries
    
  }
  

}
