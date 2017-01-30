package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import java.text.ParseException;

import backend.Admin;
import backend.Client;
import backend.Driver;
import backend.Flight;


/**
 * Created by mandy on 2016-11-28.
 */


public class AdminHomepage extends AppCompatActivity {
    public static final String FLIGHT_DB = "flight_db";
    public static final String CLIENT_DB = "client_db";
    EditText et_flight_file;
    EditText et_client_file;
    Driver driver;
    Admin admin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.admin_homepage);
        Intent intent = getIntent();
        driver = (Driver) intent.getSerializableExtra("driver");
        admin = (Admin) intent.getSerializableExtra("admin");
        et_client_file = (EditText) findViewById(R.id.et_client_file);
        et_flight_file = (EditText) findViewById(R.id.et_flight_file);


//        // get absolute path
//        File flightsFile = new File(this.getApplicationContext().getFilesDir(), FLIGHT_FILE_NAME);
//        // convert flightsFile into string
//        String FlightsFilePath = flightsFile.getPath();
    }

    public void onClickEditClientInfo(View v) {
        Intent intentEditClientProfile = new Intent(this, AdminEditClientInfo.class);
        Client client = driver.getClientDatabase().getClient().get(((EditText) findViewById(R.id.et_clients_email)).getText().toString());
        intentEditClientProfile.putExtra("driver", this.driver);
        intentEditClientProfile.putExtra("admin", admin);
        intentEditClientProfile.putExtra("client", client);
        startActivity(intentEditClientProfile);
    }

    public void onClickViewClientsItineraries(View v) {
        Intent intentViewClientItineraries = new Intent(this, AdminDisplaySearchedFlights.class);
        intentViewClientItineraries.putExtra("driver", this.driver);
        intentViewClientItineraries.putExtra("admin", admin);
        startActivity(intentViewClientItineraries);
    }

    public void onClickAdminSearchFlights(View v) {
        Intent intentAdminSearchFlights = new Intent(this, AdminSearchFlights.class);
        intentAdminSearchFlights.putExtra("driver", this.driver);
        intentAdminSearchFlights.putExtra("admin", admin);
        startActivity(intentAdminSearchFlights);
    }

    public void onClickEditFlights(View v) {
        Flight flight = driver.getFlightDatabase().getFlight((((EditText) findViewById(R.id.et_flight_number)).getText().toString()));
        Intent intentEditFlights = new Intent(this, AdminEditFlights.class);
        intentEditFlights.putExtra("driver", this.driver);
        intentEditFlights.putExtra("admin", admin);
        intentEditFlights.putExtra("flight", flight);
        startActivity(intentEditFlights);
    }

    public void onClickLoadClientFile(View v) {
        String client_file = et_client_file.getText().toString();
        driver.uploadClientInfo(client_file);

        Intent intentDisplayClientDB = new Intent(this, AdminDisplayClientDB.class);
        intentDisplayClientDB.putExtra(CLIENT_DB, driver.getClientDatabase());
        intentDisplayClientDB.putExtra("driver", this.driver);
        intentDisplayClientDB.putExtra("admin", admin);
        startActivity(intentDisplayClientDB);
    }
    public void onClickLoadFlightFile(View v) throws ParseException{
        String flight_file = et_flight_file.getText().toString();
        driver.uploadFlightInfo(flight_file);
        Intent intentDisplayFlightDB = new Intent(this, AdminDisplayFlightDB.class);
        intentDisplayFlightDB.putExtra(FLIGHT_DB, driver.getFlightDatabase());
        intentDisplayFlightDB.putExtra("driver", this.driver);
        intentDisplayFlightDB.putExtra("admin", admin);
        startActivity(intentDisplayFlightDB);
    }


    public void onClickLoadAdminLogOut(View v) {
        Intent intentAdminLogout = new Intent(this, Login.class);
        intentAdminLogout.putExtra("driver", this.driver);
        startActivity(intentAdminLogout);
    }
}

