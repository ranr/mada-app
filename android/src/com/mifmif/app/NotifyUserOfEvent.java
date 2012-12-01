package com.mifmif.app;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import android.app.Activity;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.TaskStackBuilder;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.support.v4.app.NotificationCompat;

public class NotifyUserOfEvent {
	public NotifyUserOfEvent(Activity activity) {
		_context = activity;
		notificationId=0;
	}

	private Context _context;
	private int notificationId; 
	
	private class Event {
		public String information;
		public String address; 
		public Double latitude; 
		public Double longitude; 
		public String timestamp;
		public Date firstSeen;
		public int notificationID;

		public boolean isEqual( Event other ) {
			if (address == null) {
				if (other.address != null)
					return false;
			} else if (!address.equals(other.address))
				return false;
			if (information == null) {
				if (other.information != null)
					return false;
			} else if (!information.equals(other.information))
				return false;
			if (latitude == null) {
				if (other.latitude != null)
					return false;
			} else if (!latitude.equals(other.latitude))
				return false;
			if (longitude == null) {
				if (other.longitude != null)
					return false;
			} else if (!longitude.equals(other.longitude))
				return false;
			if (timestamp == null) {
				if (other.timestamp != null)
					return false;
			} else if (!timestamp.equals(other.timestamp))
				return false;
			return true;
		}
	};
	
	List< Event > eventCache = new ArrayList< Event >();
	
	public void notifyIfNew( String information,
							String address, 
							Double latitude, 
							Double longitude, 
							String timestamp )
	{
		Event event = new Event();
		event.information = information;
		event.address = address;
		event.latitude = latitude;
		event.longitude = longitude;
		event.timestamp = timestamp;
		event.firstSeen = new Date();
		
		for ( int i = 0 ; i < eventCache.size() ; ++ i )
			if ( event.isEqual( eventCache.get( i ) ) )
				return;
		
		eventCache.add( event );
		
		cleanupStale();
	
		notifyUser( event );
	}

	private void cleanupStale() {
		while ( eventCache.size() > 40 ) {
			cancelNotification( eventCache.get( 0 ) );
			eventCache.remove( 0 );
		}
			
		Calendar expiration = Calendar.getInstance();
		expiration.add( Calendar.MINUTE, -15 );
		Date expirationDate = expiration.getTime();
		while ( eventCache.size() > 0 && eventCache.get( 0 ).firstSeen.before( expirationDate ) ) {
			cancelNotification( eventCache.get( 0 ) );
			eventCache.remove( 0 );
		}
	}

	private void cancelNotification( Event event )
	{
		NotificationManager mNotificationManager =
			    (NotificationManager) _context.getSystemService(Context.NOTIFICATION_SERVICE);
		mNotificationManager.cancel( event.notificationID );
	}
	
	private void notifyUser( Event event )
	{
		final Uri sound = Uri.parse("android.resource://com.mifmif.app/raw/siren");
		long pattern[] = { 0, 3000, 2000, 3000, 2000, 3000 };
		NotificationCompat.Builder mBuilder =
		        new NotificationCompat.Builder(_context)
				.setSound(sound)
				.setVibrate(pattern)
		        .setSmallIcon(R.drawable.redstar)
		        .setContentTitle(event.information)
		        .setContentText(event.address);
		// Creates an explicit intent for an Activity in your app
		Uri uri = 	Uri.parse("geo:0,0?q="+event.latitude+","+event.longitude+"("+event.address+")");
		Intent resultIntent = new Intent(android.content.Intent.ACTION_VIEW, uri);
			

		PendingIntent pendingIntent = PendingIntent.getActivity(_context, 0, resultIntent, 0);
		
		mBuilder.setContentIntent(pendingIntent);
		NotificationManager mNotificationManager =
		    (NotificationManager) _context.getSystemService(Context.NOTIFICATION_SERVICE);
		// mId allows you to update the notification later on.
		mNotificationManager.notify(notificationId, mBuilder.build());
		event.notificationID = notificationId;
		++notificationId;
	}
}
