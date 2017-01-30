package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;

import java.util.ArrayList;

import backend.Client;
import backend.Driver;
import backend.Itinerary;
import backend.Trip;

public class ClientHomepage extends AppCompatActivity {

    private Driver driver;
    private Client client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_homepage);

        Intent intent = getIntent();

        client = (Client) intent.getSerializableExtra("client");

        TextView clientName = (TextView) findViewById(R.id.client_name);
        clientName.setText(client.getFirstName() + " " + client.getLastName());
        TextView bookedFlights = (TextView) findViewById(R.id.booked_flights);
        //access client bookedlights
        // to do this, we grab the booked flights from client and
        // then to string them to get the info
          ArrayList<Itinerary> bookings = client.getBookedItineraries();
         String content = "";
         for(Itinerary itinerary : bookings){
           content += itinerary.toString() + "\n";
         }
         TextView flightsBooked = (TextView) findViewById(R.id.booked_flights);
         flightsBooked.setText(content);
    }

    public void onClickSearchFlights(View v) {
        Intent intentSearch = new Intent(this, SearchFlights.class);
        intentSearch.putExtra("driver", driver);
        intentSearch.putExtra("client", client);
        startActivity(intentSearch);
    }

    public void onClickEditProfile(View v) {
        Intent intentEdit = new Intent(this, EditProfile.class);
        intentEdit.putExtra("driver", driver);
        intentEdit.putExtra("client", client);
        startActivity(intentEdit);
    }

    public void Logout(View v) {
        Intent intentLogout = new Intent(this, Login.class);
        intentLogout.putExtra("driver", driver);
        startActivity(intentLogout);
    }
}

