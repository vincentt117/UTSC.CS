package backend;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.file.Path;
import java.nio.file.Paths;
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
  public HashMap<String, Flight> deserialize() {
    HashMap<String, Flight> object = null;
    try {
      FileInputStream fileIn = new FileInputStream(this.filepath);
      ObjectInputStream in = new ObjectInputStream(fileIn);
      object = (HashMap<String, Flight>) in.readObject();
      in.close();
      fileIn.close();
    } catch (IOException i) {
      i.printStackTrace();
    } catch (ClassNotFoundException c) {
      System.out.println("Flight class not found");
      c.printStackTrace();
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
    } catch (IOException i) {
      i.printStackTrace();
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
      String flightNumber;
      final String airline;
      final String origin;
      final String destination;
      Date departureTime;
      final Date arrivalTime;
      final double cost;
      DateFormat date = new SimpleDateFormat("yyyy-MM-dd HH:mm");
      String[] splitArray = line.split(";");
      flightNumber = splitArray[0];
      departureTime = date.parse(splitArray[1]);
      arrivalTime = date.parse(splitArray[2]);
      airline = splitArray[3];
      origin = splitArray[4];
      destination = splitArray[5];
      cost = Double.parseDouble(splitArray[6]);

      Flight newFlight = new Flight(flightNumber, departureTime, arrivalTime, airline, origin,
          destination, cost);
      this.flights.put(flightNumber, newFlight);

    }
    reader.close();
    serialize(this.flights);

    // testing
    for (String key : this.flights.keySet()) {
      System.out.println("KEY:  " + key + "   VALUE:  " + this.flights.get(key));
    }
  }

}
