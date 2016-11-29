package backend;

import backend.FlightDatabase;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

public class Test {

  public static final Duration MIN_LAYOVER = Duration.ofMinutes(30);
  public static final Duration MAX_LAYOVER = Duration.ofHours(6);

  private static DateFormat date = new SimpleDateFormat("yyyy-MM-dd");
  private static DateFormat dateTime = new SimpleDateFormat("yyyy-MM-dd HH:mm");

  public static void main(String args[]) throws ParseException {

    // create the dates
    DateFormat df = new SimpleDateFormat("MM-dd-yyyy HH:mm");
    Date d1a = df.parse("12-10-2016 09:09");
    Date d1d = df.parse("9-30-2016 16:37");
    Date d2a = df.parse("12-11-2016 09:09");
    Date d2d = df.parse("12-9-2016 09:09");

    /*
     * //add the flights to the itinerary ArrayList<Trip> flighta = new=
     * ArrayList<Trip>(); flighta.add(a); Itinerary itinerary1 = new
     * Itinerary(flighta); ArrayList<Trip> flightb = new ArrayList<Trip>();
     * flightb.add(b); Itinerary itinerary2 = new Itinerary(flightb);
     * //instantiate the resultitinerary ArrayList<Itinerary> array1 = new
     * ArrayList<Itinerary>(); array1.add(itinerary2); array1.add(itinerary1);
     * //show the costs before getting sorted for (Itinerary i : array1) {
     * System.out.println(i.getTotalCost()); } //show the costs after getting
     * sorted ResultItinerary result = new ResultItinerary(array1);
     * ResultItinerary p = result.sortByCost(); System.out.println(p);
     */
    // System.out.println(new Client("a", "a", "a", "a", "a",
    // d1d).searchItinerary("London", "Rome", d1d));
    /*ResultItinerary a = (new Client("a", "a", "a", "a", "a", d1d).searchItinerary("London", "Rome",
        d1d));
    for (Itinerary i : a.getResItinerary()) {
      System.out.println(i);
    }*/
    
      String flightNum1 = "AC213"; Date departure1 = null; Date arrival1 =
      null; try { departure1 = dateTime.parse("2016-11-29 11:30"); arrival1 =
      dateTime.parse("2016-11-29 15:45"); } catch (ParseException ex) {
      ex.printStackTrace(); } String airline1 = "Air Canada"; double price1 =
      630.99;
      
      String flightNum2 = "AC768"; Date departure2 = null; Date arrival2 =
      null; try { departure2 = dateTime.parse("2016-11-29 19:30"); arrival2 =
      dateTime.parse("2016-11-29 22:00"); } catch (ParseException ex) {
      ex.printStackTrace(); } String airline2 = "Air Canada Rouge"; double
      price2 = 530.99;
      
      String stopover = "YYZ"; double totalPrice = price1 + price2; Duration
      totalDuration = Duration.between(departure1.toInstant(),
      arrival2.toInstant());
      
      String flight1Formatted = String.format("%s;%s;%s;%s;%s;%s", flightNum1,
      dateTime.format(departure1), dateTime.format(arrival1), airline1, "A",
      stopover); String flight2Formatted = String.format("%s;%s;%s;%s;%s;%s",
      flightNum2, dateTime.format(departure2), dateTime.format(arrival2),
      airline2, stopover, "B"); String oneItineraryFormatted =
      String.format("%s\n%s\n%.2f\n%.2f", flight1Formatted, flight2Formatted,
      totalPrice, totalDuration.toMinutes() / 60.0);
      
      List<String> itineraries = new ArrayList<>();
      itineraries.add(oneItineraryFormatted);
      
      System.out.println(itineraries);
     
  }
}