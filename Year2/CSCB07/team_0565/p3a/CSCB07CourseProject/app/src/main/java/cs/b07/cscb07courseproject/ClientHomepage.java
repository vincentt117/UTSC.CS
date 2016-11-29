package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;

import backend.Client;

public class ClientHomepage extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_homepage);

        Intent intent = getIntent();

        //Client client = (Client) intent.getSerializableExtra("clientKey");

        //TextView clientName = (TextView) findViewById(R.id.client_name);
        //clientName.setText(client.getFirstName() + " " + client.getLastName());
        //TextView bookedFlights = (TextView) findViewById(R.id.booked_flights);
        //access client bookedlights
    }

    public void onClickSearchFlights(View v) {
        Intent intentSearch = new Intent(this, SearchFlights.class);
        startActivity(intentSearch);
    }

    public void onClickEditProfile(View v) {
        Intent intentEdit = new Intent(this, EditProfile.class);
        startActivity(intentEdit);
    }

    public void Logout(View v) {
        Intent intentLogout = new Intent(this, Login.class);
        startActivity(intentLogout);
    }
}

