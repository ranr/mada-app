package com.mifmif.app;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class StatusActivity extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_status);

		final TextView text = (TextView) findViewById( R.id.text_status );
		text.setText( "האפליקציה עובדת\nבזמן האחרון..." );
	}
}
