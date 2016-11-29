package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import backend.FlightDatabase;

/**
 * Created by mandy on 2016-11-29.
 */

public class AdminDisplayFlightDB extends AppCompatActivity{

    private FlightDatabase flightDatabase;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.admin_search_flights);

        // get the Intent that launched me
        Intent intent = getIntent();
        flightDatabase = (FlightDatabase) intent.getSerializableExtra(AdminHomepage.FLIGHT_DB);

        String content = flightDatabase.toString();
        TextView view = (TextView) findViewById(R.id.flightDB_info);
        view.setText(content);

        // write method here to save file?
    }

}