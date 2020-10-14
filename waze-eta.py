import WazeRouteCalculator
import logging

#logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
#logger.setLevel(logging.DEBUG)
#handler = logging.StreamHandler()
#logger.addHandler(handler)
team = {"Beverly Benton": "5830 Wembley drive Douglasville, GA 30135",
        "Gary Bonneau":   "4110 Night Sky Ln Cumming, GA 30041",
        "Robert Copelan": "5911 Jim Crow Road Flowery Branch, GA 30542",
		"Patrick Hislar": "3211 Katelyn Ct.  SW Liburn, GA 30047"
	   }
for member,addr in team.items(): 
    print (member,addr)

    from_address = addr
    to_address = '1261 Palmour Drive, Gainesville, GA 30501'
    region = 'US'
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    try:
        result = route.calc_route_info()
        print (member,":", result)
    except WazeRouteCalculator.WRCError as err:
        print(err)
