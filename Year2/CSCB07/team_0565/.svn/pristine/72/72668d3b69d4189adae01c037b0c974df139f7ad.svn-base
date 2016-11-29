package cs.b07.cscb07courseproject;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {

    Button bLogin;
    EditText et_email, et_password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //File userdata = this.getApplicationContext().getFilesDir();
        //Driver driver = new Driver();
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);

        et_email = (EditText) findViewById(R.id.et_email);
        et_password = (EditText) findViewById(R.id.et_password);
    }

    public void onClickRegister(View v) {
        //send to register page
        Intent intentRegister = new Intent(this, ClientRegistration.class);
        startActivity(intentRegister);
        }

    public void onClickLogin(View v) {
        String email = et_email.getText().toString();
        String password = et_password.getText().toString();
        if (email.equals("admin") && password.equals("1234")) {
            Intent intentLoginAdmin = new Intent(this, AdminHomepage.class);
            //check if the email exists in our database
            //if it does send it to the client home page
            startActivity(intentLoginAdmin);
        }
        else {
            Intent intentLogin = new Intent(this, ClientHomepage.class);
            //check if the email exists in our database
            //if it does send it to the client home page
            startActivity(intentLogin);
        }
    }
}

