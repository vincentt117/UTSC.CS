package classtests;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import backend.Admin;

public class AdminTest {

  private String firstName;
  private String lastName;
  private String email;
  private String password;
  private Admin testAdmin;
  
  @Before
  public void setUp() throws Exception {
  }

  @After
  public void tearDown() throws Exception {
  }

  @Test
  public void testAdmin() {
    try{
      // first test to see if it can make and admin normally
      firstName = "Taylor";
      lastName = "Smaith";
      email = "Taylor.Smith@gmail.com";
      password = "123456789";
    
      testAdmin = new Admin(firstName, lastName, email, password);
    }catch(Exception e){
      fail("cannot normally create an admin");
    }
    
    try{
      // now test to see what happens if empty strings are added
      firstName = "";
      lastName = "";
      email = "";
      password = "";
    
      testAdmin = new Admin(firstName, lastName, email, password);
    }catch(Exception e){
      fail("cannot create admin with empty strings");
    }
    
    try{
      // last test to see what happens if strings are null
      firstName = null;
      lastName = null;
      email = null;
      password = null;
      
      testAdmin = new Admin(firstName, lastName, email, password);
    }catch(Exception e){
      fail("cannot create admin with null strings");
    }

  }

  @Test
  public void testUploadFlightInfo() {
    // Phase 3
  }

  @Test
  public void testViewData() {
    // Phase 3
  }

}
