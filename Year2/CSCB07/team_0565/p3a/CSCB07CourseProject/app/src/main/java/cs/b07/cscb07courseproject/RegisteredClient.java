package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;

import backend.Client;

public class RegisteredClient extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_registered_finish);
        Intent intent = getIntent();
        //Client registeredClient = (Client)intent.getSerializableExtra("newClient");
        //put client in database
    }

    public void backToHomepage(View view) {
        Intent intent = new Intent(this, ClientHomepage.class);
        startActivity(intent);
    }
}