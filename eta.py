import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDYlX2y46XDcPcEIlPN7Kd0lbKz3NbQZuo')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


team = {"Beverly Benton": "5830 Wembley drive Douglasville, GA 30135",
        "Gary Bonneau":   "4110 Night Sky Ln Cumming, GA 30041",
        "Robert Copelan": "5911 Jim Crow Road Flowery Branch, GA 30542",
		"Patrick Hislar": "3211 Katelyn Ct.  SW Liburn, GA 30047"
	   }
print (team)
for member,addr in team: 
    print (member,addr)
