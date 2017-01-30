package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

import backend.Admin;
import backend.Driver;
import backend.Flight;
import backend.FlightDatabase;

/**
 * Created by mandy on 2016-11-29.
 */

public class AdminEditFlights extends AppCompatActivity{

    Driver driver;
    Admin admin;
    Flight flight;
    EditText et_flight_no, et_departure_time, et_arrival_time, et_Airline,
            et_origin, et_destination, et_price, et_numSeats;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.admin_edit_flights);
        Intent intent = getIntent();
        driver = (Driver) intent.getSerializableExtra("driver");
        admin = (Admin) intent.getSerializableExtra("Admin");
         flight = (Flight) intent.getSerializableExtra("flight");
        et_flight_no = (EditText) findViewById(R.id.et_flight_no);
        et_departure_time = (EditText) findViewById(R.id.et_departure_time);
        et_arrival_time = (EditText) findViewById(R.id.et_arrival_time);
        et_Airline = (EditText) findViewById(R.id.et_Airline);
        et_origin = (EditText) findViewById(R.id.et_origin);
        et_destination = (EditText) findViewById(R.id.et_destination);
        et_price = (EditText) findViewById(R.id.et_price);
        et_numSeats = (EditText) findViewById(R.id.et_numSeats);
        et_flight_no.setText(flight.getFlightNumber());
        DateFormat dateTime = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        et_departure_time.setText(dateTime.format(flight.getDepartureTime()));
        et_arrival_time.setText(dateTime.format(flight.getArrivalTime()));
        et_Airline.setText(flight.getAirline());
        et_origin.setText(flight.getOrigin());
        et_destination.setText(flight.getDestination());
        et_price.setText(String.valueOf(flight.getCost()));
        et_numSeats.setText(String.valueOf(flight.getNumSeats()));

    }

    public void onClick_EditFlight_to_Homepage(View v) {
        Intent intentHomepage = new Intent(this, AdminHomepage.class);
        intentHomepage.putExtra("driver", this.driver);
        intentHomepage.putExtra("admin", admin);
        startActivity(intentHomepage);
    }
}
