package backend;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;

/**
 * A Class that represent a <code>FlightDatabase</code>.
 * 
 * @author Ciel
 *
 */
public class FlightDatabase extends Database implements java.io.Serializable {

  private static final long serialVersionUID = 1L;
  private String filepath;
  private HashMap<String, Flight> flights;

  /**
   * Creates a new instance of a <code>FlightDatabase</code>.
   * 
   * @param filepath
   *          the pathname of the file to read and store the data from
   */
  public FlightDatabase(String filepath) {
    this.filepath = filepath;
    this.flights = new HashMap<String, Flight>();
    // serialize(this.flights);
  }

  /**
   * Deserializes the file storing the serialized <code>HashMap</code> for the
   * FlightDatabase.
   * 
   * @return the HashMap that stores all the flights
   */
  @SuppressWarnings("unchecked")
  public HashMap<String, Flight> deserialize() {
    HashMap<String, Flight> object = null;
    try {
      FileInputStream fileIn = new FileInputStream(this.filepath);
      ObjectInputStream in = new ObjectInputStream(fileIn);
      object = (HashMap<String, Flight>) in.readObject();
      in.close();
      fileIn.close();
    } catch (IOException in) {
      in.printStackTrace();
    } catch (ClassNotFoundException cl) {
      System.out.println("Flight class not found");
      cl.printStackTrace();
    }
    return object;
  }

  /**
   * Serializes the HashMap to a file.
   * 
   * @param flights
   *          the HashMap to be serialized
   */
  public void serialize(HashMap<String, Flight> flights) {
    try {
      FileOutputStream fileOut = new FileOutputStream(this.filepath);
      ObjectOutputStream out = new ObjectOutputStream(fileOut);
      out.writeObject(flights);
      out.close();
      fileOut.close();
    } catch (IOException in) {
      in.printStackTrace();
    }
  }

  /**
   * Adds a <code>Flight</code> to the <code>FlightDatabase</code>.
   * 
   * @param flight
   *          the <code>Flight</code> instance to be added
   */
  public void addFlight(Flight flight) {
    String key = flight.getFlightNumber();
    this.flights.put(key, flight);
    serialize(this.flights);
  }

  /**
   * Removes a specific <code>Flight</code> to the <code>FlightDatabase</code>.
   * 
   * @param flightNumber
   *          the <code>flightNumber</code> of the <code>Flight</code> to be
   *          removed.
   */
  public void removeFlight(String flightNumber) {
    this.flights.remove(flightNumber);
    serialize(this.flights);
  }

  /**
   * Returns HashMap of <code>Flights</code>.
   * 
   * @return the flights
   */
  public HashMap<String, Flight> getFlights() {
    return flights;
  }

  /**
   * Modifies the HashMap of <code>Flights</code>.
   * 
   * @param flights
   *          the new set of flights
   */
  public void setFlights(HashMap<String, Flight> flights) {
    this.flights = flights;
  }

  /**
   * Adding the flights given the parameter file path.
   * 
   * @param filepath
   *          Given file path
   * @throws IOException
   *           In case files are not found
   * @throws ParseException
   *           In case file is not properly formatted
   */
  public void addFlightsFromFile(String filepath) throws IOException, ParseException {

    String line;
    BufferedReader reader = new BufferedReader(new FileReader(filepath));
    while ((line = reader.readLine()) != null) {
      DateFormat date = new SimpleDateFormat("yyyy-MM-dd HH:mm");
      String[] splitArray = line.split(";");
      String flightNumber = splitArray[0];
      Date departureTime = date.parse(splitArray[1]);
      Date arrivalTime = date.parse(splitArray[2]);
      String airline = splitArray[3];
      String origin = splitArray[4];
      String destination = splitArray[5];
      double cost = Double.parseDouble(splitArray[6]);

      Flight newFlight =
          new Flight(flightNumber, departureTime, arrivalTime, airline, origin, destination, cost);
      this.flights.put(flightNumber, newFlight);

    }
    reader.close();
    serialize(this.flights);

    // testing
//    for (String key : this.flights.keySet()) {
//      System.out.println("KEY:  " + key + "   VALUE:  " + this.flights.get(key));
//    }
  }

}
