package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

/**
 * Created by mandy on 2016-11-29.
 */

public class AdminEditFlights extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.admin_edit_flights);
    }

    public void onClick_EditFlight_to_Homepage(View v) {
        Intent intentHomepage = new Intent(this, AdminHomepage.class);
        startActivity(intentHomepage);
    }
}
