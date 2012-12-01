package com.mifmif.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;

public class RegisterActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        final EditText nameField = (EditText) findViewById( R.id.edit_name );
    	final EditText phoneNumberField = (EditText) findViewById( R.id.edit_phonenumber );
        final Spinner spinner = (Spinner) findViewById( R.id.spinner1 );
        
        SharedPreferences settings = getSharedPreferences("userData", 0);

        String name = settings.getString( "name", "" );
        String phoneNumber = settings.getString( "phoneNumber", "" );
        int rankPosition = settings.getInt( "rankSelectionIndex", 0 );

        nameField.setText( name );
        phoneNumberField.setText( phoneNumber );
        spinner.setSelection( rankPosition );
    }
    
    public void registerButtonClicked( View button )
    {
    	final EditText nameField = (EditText) findViewById( R.id.edit_name );
    	final EditText phoneNumberField = (EditText) findViewById( R.id.edit_phonenumber );
        final Spinner spinner = (Spinner) findViewById( R.id.spinner1 );
        
        String name = nameField.getText().toString();
        String phoneNumber = phoneNumberField.getText().toString();
        String rank = spinner.getSelectedItem().toString();
        
        SharedPreferences settings = getSharedPreferences("userData", 0);
        SharedPreferences.Editor editor = settings.edit();
        editor.putString( "name", name );
        editor.putString( "phoneNumber", phoneNumber );
        editor.putString( "rank", rank );
        editor.putInt( "rankSelectionIndex", spinner.getSelectedItemPosition() );
        editor.commit();
        
        displaySavedSuccessfullyMessageBox();
        
        PingTask.start( this );
    }
    
    private void displaySavedSuccessfullyMessageBox()
    {
        AlertDialog.Builder dlgAlert  = new AlertDialog.Builder(this);                      
        dlgAlert.setTitle("נשמר בהצלחה"); 
        dlgAlert.setMessage("המידע שהזנת נשמר בהצלחה, האפליקציה פעילה מעכשיו"); 
        dlgAlert.setPositiveButton("OK",new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int whichButton) {
                 finish(); 
            }
       });
        dlgAlert.setCancelable(true);
        dlgAlert.create().show();
    }
}
