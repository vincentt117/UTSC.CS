package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

import backend.Client;
import backend.Driver;
import backend.Itinerary;
import backend.ResultItinerary;
import backend.Trip;

/**
 * Created by vincentteng on 2016-12-01.
 */

public class DisplaySearchedFlights extends AppCompatActivity {
    private Driver driver;
    private Client client;
    private ResultItinerary resultItinerary;
    private EditText et_origin, et_destination, et_date;
    // List view
    private ListView lv;

    // Listview Adapter
    ArrayAdapter<String> adapter;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_display_searched_flights);
        Intent intent = this.getIntent();
        // grab all the necessary data
        driver = (Driver) intent.getSerializableExtra("driver");
        client = (Client) intent.getSerializableExtra("client");
        resultItinerary = (ResultItinerary) intent.getSerializableExtra("itinerary");
        setAllInformation();

    }

    public void onNewIntent(Intent intent){
        // grab all the necessary data for a refresh and redo the page
        driver = (Driver) intent.getSerializableExtra("driver");
        client = (Client) intent.getSerializableExtra("client");
        resultItinerary = (ResultItinerary) intent.getSerializableExtra("itinerary");
        setAllInformation();

    }
    public void setAllInformation(){
        // this is a helper method to help load all the data on the page
        // now we have to unravel the classes to be able to get the individual flights to
        // parse into the page
        ArrayList<String> items = new ArrayList<>();
        ArrayList<Itinerary> result = resultItinerary.getResItinerary();
        ArrayList<Trip> trips;
        // grab all the text for the list items
        for(Itinerary i: result) {
            // here to format this, we want a rows of itinerary information
            String text = "";
            trips = i.getTripList();
            for (Trip trip : trips) {
                // then we grab all the flight information and put it into the file
                text += "Departs from: " + trip.getOrigin();
                text += " at " + trip.getDepartureTime();
                text += " to arrive at " + trip.getDestination();
                text += " at " + trip.getArrivalTime();
                // then we place and -> to show that the flights are connected
                text += " -> ";
            }
            text += " , Trip will take: " + i.getTotalTime();
            text += " , Number of free seats: " + i.getLowestNumSeats();
            text += " , Will cost in total: " + i.getTotalCost();
            items.add(text);
        }
        lv = (ListView) findViewById(R.id.list_view);
        // Adding items to listview
        adapter = new ArrayAdapter<String>(this, R.layout.list_item, R.id.item_name, items);
        lv.setAdapter(adapter);
    }
}
