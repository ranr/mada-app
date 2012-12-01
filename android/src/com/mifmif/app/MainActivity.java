package com.mifmif.app;

import android.os.Bundle;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.TabActivity;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TabHost;
import android.widget.TabHost.TabSpec;

public class MainActivity extends TabActivity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		TabHost tabHost = getTabHost();

		TabSpec registerTab = tabHost.newTabSpec("Register");
		registerTab.setIndicator( "הרשם" );
		Intent photosIntent = new Intent(this, RegisterActivity.class);
		registerTab.setContent(photosIntent);

		TabSpec statusTab = tabHost.newTabSpec("Status");
		statusTab.setIndicator( "סטטוס" );
		Intent statusIntent = new Intent(this, StatusActivity.class);
		statusTab.setContent(statusIntent);

		tabHost.addTab(registerTab);
		tabHost.addTab(statusTab);

		if( hasPhoneNumber() )
			tabHost.setCurrentTab( 1 );

		PingTask.start( this );
	}

	private boolean hasPhoneNumber()
	{
		SharedPreferences settings = getSharedPreferences("userData", 0);
		String phoneNumber = settings.getString( "phoneNumber", "" );
		return phoneNumber != "";
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.activity_main, menu);
		return true;
	}

}
