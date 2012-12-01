package com.mifmif.app;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

public class UserOpenedNotificationActivity extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		Intent intent= getIntent();
		int notificationID = intent.getIntExtra("eventNotificationID", -1 );
		if ( notificationID == -1 )
			return;
		NotifyUserOfEvent.Event event = NotifyUserOfEvent.findAndCancelEventByNotificationID( notificationID );
		if ( event == null )
			return;
		startActivity( geoIntent( event ) );
	}

	private Intent geoIntent( NotifyUserOfEvent.Event event )
	{
		Uri uri = Uri.parse("geo:0,0?q="+event.latitude+","+event.longitude+"("+event.address+")");
		Intent resultIntent = new Intent(android.content.Intent.ACTION_VIEW, uri);
		return resultIntent;
	}
} 