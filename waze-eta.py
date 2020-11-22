import WazeRouteCalculator
import logging

#logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
#logger.setLevel(logging.DEBUG)
#handler = logging.StreamHandler()
#logger.addHandler(handler)
team = {"Beverly Benton": "5830 Wembley drive Douglasville, GA 30135",
        "Gary Bonneau":   "4110 Night Sky Ln Cumming, GA 30041",
        "Robert Copelan": "5911 Jim Crow Road Flowery Branch, GA 30542",
	    "Patrick Hislar": "3211 Katelyn Ct.  SW Liburn, GA 30047",
        "Stephan Keech": "490 Lindbergh PL NE Apt. 540 Atlanta, GA 30324",
        "Jennifer Kingsley": "4190 Everett Springs Rd. NE Armuchee, GA 30105",
        "Cheryl Knieriemen": "138 Courtland Circle Powder Springs, GA  30127",
        "Heidi Morris-Taylor": "5373 Zachery Drive Stone Mountain, GA 30083",
        "Hilary Nickerson": "315 Oxford Meadow Run Alpharetta, GA 30004",
        "Pam Nyberg": "2705 Diamond Head Court Decatur, GA 30033",
        "Tony Polizzi": "3031 Andora Drive SW Marietta, GA 30064",
        "Phil Schillinger": "281 Mallard Dr Carrollton, GA 30116",
        "Sherri Schwartz": "4703 Cambridge Drive Dunwoody, GA 30338",
        "Jennifer/Maddy Sheppard": "1702 Frazier Park Drive Decatur, GA 30033",
        "Tim Ward": "4300 Hwy 411 NE Rydal, GA 30171",
        "Dawn Welch": "5175 Hwy 41 South Buena Vista, GA 31803"
       }
print (team)
for member,addr in team.items(): 
    #print (member,addr)

    from_address = addr
    to_address = '1261 Palmour Drive, Gainesville, GA 30501'
    to_address = '1614 Devin Court, Stone Mountain, Ga'
    region = 'US'
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    try:
        result = route.calc_route_info()
        print (member,":", result[0]," min " , result[1]/1.609, "miles")
    except WazeRouteCalculator.WRCError as err:
        print(err)

    print ("\n\n")
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    try:
        route.calc_all_routes_info()
        #print (member,":", result[0]," min " , result[1]/1.609, "miles")
    except WazeRouteCalculator.WRCError as err:
        print(err)
