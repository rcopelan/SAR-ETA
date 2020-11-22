import WazeRouteCalculator
import logging
import datetime
import math 

def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    return(sorted(sub_li, key = lambda x: x[1]))   


to_address = '1614 Devin Court, Stone Mountain, Ga'
region = 'US'    


#logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
#logger.setLevel(logging.DEBUG)
#handler = logging.StreamHandler()
#logger.addHandler(handler)
team = {"Beverly Benton": "5830 Wembley Drive Douglasville, GA 30135",
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

deploy_list = []
     
current_time = datetime.datetime.now()
if current_time.minute < 10:
    leading_zero = "0"
else:
    leading_zero = ""
print ("It is now:", str(current_time.hour) + ":" + leading_zero + str(current_time.minute) + "\n")
print ("Estimated travel time to:\n    ", to_address,"\n *** Calculating ***\n\n")

for member,addr in team.items(): 
    from_address = addr
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    try:
        result = route.calc_route_info()
        #print (member,":", result[0]," min " , (result[1]/1.609), "miles")
        #print ("{:<30} {:.0f} minutes  {:.0f} miles".format(member,math.ceil(result[0]),math.ceil(result[1]/1.609)))
        minutes = datetime.timedelta(minutes= math.ceil(result[0]))
        eta = current_time + minutes
        if eta.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        #print ("{:<30} {:^8} {:.0f} minutes  {:.0f} miles".format(member, str(eta.hour) + ":" + leading_zero + str(eta.minute), math.ceil(result[0]),math.ceil(result[1]/1.609)))
        this_member = [member,math.ceil(result[0]),math.ceil(result[1]/1.609)]
        deploy_list.append(this_member)
        #print ("ETA:", str(eta.hour) + ":" + leading_zero + str(eta.minute))
        #print ("\n")
    except WazeRouteCalculator.WRCError as err:
        print(err)
#print (deploy_list)
#print ("\n\n")
#print (Sort(deploy_list) )
for members in Sort(deploy_list):
    minutes = datetime.timedelta(minutes= math.ceil(members[1]))
    eta = current_time + minutes
    if eta.minute < 10:
        leading_zero = "0"
    else:
        leading_zero = ""
    print ("{:<30} {:^8} {:.0f} minutes  {:.0f} miles".format(members[0], str(eta.hour) + ":" + leading_zero + str(eta.minute), math.ceil(members[1]),math.ceil(members[2])))


#route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
#try:
#    all_routes = route.calc_all_routes_info()
#    print (all_routes)
#    #print (member,":", result[0]," min " , result[1]/1.609, "miles")
#except WazeRouteCalculator.WRCError as err:
#    print(err)
