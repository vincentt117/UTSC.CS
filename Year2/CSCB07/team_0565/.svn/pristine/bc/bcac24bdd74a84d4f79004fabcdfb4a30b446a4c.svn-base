package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import backend.Client;
import backend.Driver;
import backend.Itinerary;
import backend.Trip;

/**
 * Created by Ciel on 2016-11-26.
 */

public class BookingResult extends AppCompatActivity {

    Driver driver;
    Itinerary itinerary;
    Client client;
    TextView welcome = (TextView)findViewById(R.id.welcome);
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Intent intent = this.getIntent();
        this.driver = (Driver) intent.getSerializableExtra("driver");
        this.client = (Client) intent.getSerializableExtra("client");
        this.itinerary = (Itinerary) intent.getSerializableExtra("itinerary");
        // Check if all flights in the itinerary could be booked
        boolean canBook = true;
        for(Trip trip: itinerary.getTripList()){
            if(trip.getNumSeats() == 0){
                canBook = false;
            }
        }
        if(canBook) {
            itinerary.bookSeat();
            client.addItinerary(itinerary);
            welcome.setText("Your booking was successful.");

        }
        else{
            welcome.setText("Due to flight Capcity(ies), your booking could not be processed");
        }
        setContentView(R.layout.booking_result);
    }

}
