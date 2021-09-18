from sartopo_python import SartopoSession
import time
import json
import logging
import WazeRouteCalculator
import datetime
import math

import PySimpleGUI as sg

map_id = "E0BA"   #test map
#map_id = ""

def pucb(*args):
    print("Property Updated: pucb called with args "+str(args))
    
def gucb(*args):
    #print("@@@@@: gucb called with args "+str(args))
    if args[0] in enroutes.keys():
        point = args[1]
        coordinates = point['coordinates'][0]
    
        from_address = str(coordinates[1]) + "," + str(coordinates[0])
        #print ("@@@@@:",from_address, to_address)
        from_coordinates = [coordinates[1],coordinates[0]]
        if args[0] in enroute_coordinates.keys():
            enroute_coordinates[args[0]] = from_coordinates
        else:
            enroute_coordinates[args[0]] = from_coordinates
        #print ("@@@@@:",enroute_coordinates)        
            
    
         
        
    else:
        print ("@@@@@: Not a AppTrack",args[0]) 

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
handler = logging.StreamHandler()
logger.addHandler(handler)
        
from_address = ""
to_address = ""   
enroutes = {}
enroute_coordinates = {} 
error_msg = "error line"
text_lines = "this would be output"
layout = [
         [sg.Text(text_lines,font='Courier 20', text_color='white',key='-Output-', background_color='blue',size=(70,2))],
         [sg.Button('Dump'), sg.Button('Clear'), sg.Button('Repeat'), sg.Button('Exit')],
         [sg.Text(error_msg)] 
         ]
          

sts2=SartopoSession(
    "sartopo.com",
    map_id,
    sync=True,
    #syncDumpFile='rnc_sync_dump.txt',
    #propUpdateCallback=pucb,
    geometryUpdateCallback=gucb,
    configpath="eta.cfg",
    account="robert@atsar.org")

region = "US"
run_loop = True
from_address = "34.2183,-83.9337"
to_address = "34.1805,-83.9102"
win1 = sg.Window('SAR ETA', layout,resizable=True, font='Courier 15')     
win1_event, win1_values = win1.Read(timeout=100)
previous_time_run = datetime.datetime.now() - datetime.timedelta(seconds = 30)
while run_loop:
    current_time_run = datetime.datetime.now()
    time_diff = current_time_run - previous_time_run
    if time_diff.total_seconds() > 15:
        previous_time_run = current_time_run
        markers = sts2.getFeatures("Marker")
        for marker in markers:
           if marker["properties"]["title"] == "Rally Point":
               #print ("***** IC FOUND:")
               to_address = str(marker["geometry"]["coordinates"][1]) + "," + str(marker["geometry"]["coordinates"][0])
               #print ("      to_address:",to_address)
        apptracks = sts2.getFeatures("AppTrack")
        #print ("Apptracks:",apptracks)
        if apptracks[0]:
         for apptrack in apptracks: 
            #print ("\n\n**** Properties:",apptrack["id"], apptrack["properties"]["title"])
            if apptrack["id"] not in enroutes:
                enroutes[apptrack["id"]] = apptrack["properties"]["title"] 
            
        #print ("**************enroutes: ",enroutes,"\n**************","\n**************","\n**************")
        #print ("**************enroute_coordinates: ",enroute_coordinates,"\n**************","\n**************","\n**************")
    output_line = ""
    #print ("enroute_coords Items:",enroute_coordinates.items())
    #print ("list enroute_coords Items:",list(enroute_coordinates.items()))
    enroute_coordinates_copy = tuple(enroute_coordinates.keys())
    print ("@@@@")
    for id in enroute_coordinates_copy: 
       print ("$:",id,enroute_coordinates[id])
       from_address = str(enroute_coordinates[id][0]) + "," + str(enroute_coordinates[id][1])
       try:
        print ("  #Waze, from:",from_address, " to:", to_address, " region:",region)     
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
        print ("  ##Waze Route:",route)
        result = route.calc_route_info()
        print ("  ###Waze Result:",result,"\n")
        minutes = datetime.timedelta(minutes= math.ceil(result[0]))
        current_time = datetime.datetime.now()
        if current_time.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        #print ("It is now:", str(current_time.hour) + ":" + leading_zero + str(current_time.minute) + "\n")
        eta = current_time + minutes
        if eta.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        #print ("{:<30} {:^8} {:.1f} minutes  {:.1f} miles".format("person", str(eta.hour) + ":" + leading_zero + str(eta.minute), result[0],result[1]/1.609))
        #print ("\n\n")
        strETA = " ETA:" + str(eta.hour) + ":" + leading_zero + str(eta.minute)
        output_line +=  "{:<20}{:<12} {:.1f} minutes".format(enroutes[id],strETA,result[0]) + "  {:.1f} miles".format(result[1]/1.609) + "\n"
        #output_line += enroutes[id] + " ETA:" + str(eta.hour) + ":" + leading_zero + str(eta.minute) + " {:.1f} minutes".format(result[0]) + "  {:.1f} miles".format(result[1]/1.609) + "\n"
        #win1['-Output-'].update("from: " + from_address + " ETA:" + str(eta.hour) + ":" + leading_zero + str(eta.minute) + " {:.1f} minutes".format(result[0]) + "  {:.1f} miles".format(result[1]/1.609) )
       except WazeRouteCalculator.WRCError as err:
        print("Waze error:",err)
       print ("$$$$$\n")
    print ("@@@@@")
    win1['-Output-'].update(output_line)
    #print ("Output Line:\n",output_line)    
    win1_event, win1_values = win1.Read(timeout=100)
    if win1_event == "Dump":
        print ("**************enroutes: ",enroutes,"\n**************","\n**************","\n**************")
        print ("**************enroute_coordinates: ",enroute_coordinates,"\n**************","\n**************","\n**************")
    if win1_event == sg.WIN_CLOSED or win1_event == 'Exit':
       end_program = True
       run_loop = False 
       print ("Program stopped")
       quit()

