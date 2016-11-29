package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

import backend.Client;

/**
 * Created by Ciel on 2016-11-26.
 */

public class EditProfile extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.edit_profile_client);
    }

    public void backToHomepage(View v) {
        Intent intentBack = new Intent(this, ClientHomepage.class);
        //check if the email exists in our database
        //if it does send it to the client home page
        startActivity(intentBack);
    }

}
