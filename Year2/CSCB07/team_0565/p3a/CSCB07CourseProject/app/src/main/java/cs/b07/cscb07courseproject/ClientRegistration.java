package cs.b07.cscb07courseproject;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;
import android.content.Intent;
import android.view.View;
import backend.Client;

public class ClientRegistration extends AppCompatActivity implements View.OnClickListener{

    Button bRegister;
    EditText et_email, et_firstName, et_lastName, et_address, et_ccNumber, et_ccDate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_registration);

        et_email = (EditText) findViewById(R.id.et_email);
        et_firstName = (EditText) findViewById(R.id.et_firstName);
        et_lastName = (EditText) findViewById(R.id.et_lastName);
        et_address = (EditText) findViewById(R.id.et_address);
        et_ccNumber = (EditText) findViewById(R.id.et_ccNumber);
        et_ccDate = (EditText) findViewById(R.id.et_ccDate);
        bRegister = (Button) findViewById(R.id.b_Register);
        bRegister.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case R.id.b_Register:

                String email = et_email.getText().toString();
                String firstName = et_firstName.getText().toString();
                String lastName = et_lastName.getText().toString();
                String address = et_address.getText().toString();
                String ccNumber = et_ccNumber.getText().toString();
                String ccDate = et_ccDate.getText().toString();
                Client registeredClient = new Client(email,firstName,lastName,address,ccNumber,ccDate);

                Intent intent = new Intent(this, RegisteredClient.class);
                intent.putExtra("newClient", registeredClient);
                startActivity(intent);
        }
    }
}
