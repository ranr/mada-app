package com.mifmif.app;

import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Looper;
import android.util.Log;
import android.widget.EditText;
import android.widget.Spinner;

public class PingTask extends AsyncTask< Object, Integer, Integer > {
	private GPSTracker gpsTracker = null;
	private NotifyUserOfEvent notifyUserOfEvent = null;
	
	@Override
	protected Integer doInBackground( Object... parameters ) {
		Looper.prepare();
		Activity activity = (Activity) parameters[ 0 ];
		notifyUserOfEvent = new NotifyUserOfEvent( activity );
		SharedPreferences settings = activity.getSharedPreferences("userData", 0);
		gpsTracker = new GPSTracker( activity );
		
		HttpClient httpClient = new DefaultHttpClient();

		while ( true ) {
			sleep( 2000 );
			
			if ( gpsTracker.getLocation() == null )
				continue;
			
			JSONObject rendered = renderJSON( settings );
			//HttpResponse response = pingServer(httpClient, rendered);
			String response = fakeResponse();
			if ( response == null )
				continue;
			JSONObject json = parseJSON( response );
			if ( json == null )
				continue;
			parseResult( json );
		}
	}
	
	private void parseResult(JSONObject json) {
		try {
			JSONArray emergencies = json.getJSONArray( "events" );
			for ( int i = 0 ; i < emergencies.length() ; ++ i ) {
				JSONObject emergency = emergencies.getJSONObject( i );
				notifyUserOfEvent.notifyIfNew(	emergency.getString( "information" ),
												emergency.getString( "address" ),
												emergency.getDouble( "latitude" ),
												emergency.getDouble( "longitude"),
												emergency.getString( "timestamp" ) );
			}
		} catch ( Exception e ) {
			e.printStackTrace();
		}
	}

	private JSONObject parseJSON( String data )
	{
		try {
			return new JSONObject( data );
		} catch ( Exception e ) {
			e.printStackTrace();
			return null;
		}
	}
	
	private String pingServer(HttpClient httpClient, JSONObject rendered) {
		try {
			HttpPost request = new HttpPost("http://TODO/updateLocation");
			ArrayList<NameValuePair> pairs = new ArrayList<NameValuePair>(1);
			pairs.add(new BasicNameValuePair("data.json", rendered.toString()));
			request.setEntity(new UrlEncodedFormEntity(pairs));
			//request.addHeader("content-type", "application/x-www-form-urlencoded");
//			return httpClient.execute(request);
			return null;
		}catch (Exception ex) {
			ex.printStackTrace();
		}
		return null;
	}
	
	private String fakeResponse()
	{
		try {
			JSONObject emergency1 = new JSONObject();
			emergency1.put( "longitude", 32.0818 );
			emergency1.put( "latitude", 34.7736 );
			emergency1.put( "address", "somewhere over the rainbow" );
			emergency1.put( "information", "heart attack" );
			emergency1.put( "timestamp", "today!");
			JSONObject emergency2 = new JSONObject();
			emergency2.put( "longitude", 31.00 );
			emergency2.put( "latitude", 35.2167 );
			emergency2.put( "address", "somewhere over the rainbow 2" );
			emergency2.put( "information", "heart attack 2" );
			emergency2.put( "timestamp", "Later!");
			JSONArray list = new JSONArray();
			list.put( emergency1 );
			list.put( emergency2 );
			JSONObject result = new JSONObject();
			result.put( "events", list );		
			return result.toString();
		} catch ( Exception e ) {
			e.printStackTrace();
		}
		return null;
	}
	
	private void sleep( int interval ) {
		try {
			Thread.sleep(interval);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private JSONObject renderJSON(SharedPreferences settings) {
		JSONObject object = new JSONObject();
		try {
			Location location = gpsTracker.getLocation();
			object.put("rank", settings.getString( "rank", null ) );
			object.put("phoneNumber", settings.getString( "phoneNumber", null ) );
			object.put("name", settings.getString( "name", null ) );
			object.put("latitude", location.getLatitude() );
			object.put("longitude", location.getLongitude() );
		} catch (JSONException e) {
			e.printStackTrace();
			return object;
		}
		return object;
	}

	private static boolean threadAlreadyRunning = false;
	public static void start( Activity activity )
	{
		SharedPreferences settings = activity.getSharedPreferences("userData", 0);
		String phoneNumber = settings.getString( "phoneNumber", "" );
        if ( phoneNumber == "" )
        	return;

        if ( threadAlreadyRunning )
			return;
		threadAlreadyRunning = true;
        
		new PingTask().execute( activity );
	}	
}
