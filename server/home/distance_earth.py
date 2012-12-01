import math

def distance_on_earth(lat1, long1, lat2, long2):
    """
    >>> 32.493 <= distance_on_earth(31.829149, 34.951973, 32.0865,34.7896) <= 32.494
    True
    >>> 0.275 <= distance_on_earth(32.064474,34.772083, 32.063015,34.769669) <= 0.285
    True
    """
    RADIUS_OF_EARTH_KM=6378
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    return arc * RADIUS_OF_EARTH_KM

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
