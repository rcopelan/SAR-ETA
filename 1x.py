from sartopo_python import SartopoSession
import time
import json
import logging
import WazeRouteCalculator
import datetime
import math

import PySimpleGUI as sg

region = "US"
from_address = "34.21832822,-83.93392227"
to_address = "34.18022802678225,-83.91033661928626"

try:
        print ("before waze, from:",from_address, " to:", to_address, " region:",region)
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
        result = route.calc_route_info()
 
        minutes = datetime.timedelta(minutes= math.ceil(result[0]))
        current_time = datetime.datetime.now()
        if current_time.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        print ("It is now:", str(current_time.hour) + ":" + leading_zero + str(current_time.minute) + "\n")
        eta = current_time + minutes
        if eta.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        print ("{:<30} {:^8} {:.1f} minutes  {:.1f} miles".format("person", str(eta.hour) + ":" + leading_zero + str(eta.minute), result[0],result[1]/1.609))
        print ("\n\n")
        output_line += enroutes[id] + " ETA:" + str(eta.hour) + ":" + leading_zero + str(eta.minute) + " {:.1f} minutes".format(result[0]) + "  {:.1f} miles".format(result[1]/1.609) + "\n"
        #win1['-Output-'].update("from: " + from_address + " ETA:" + str(eta.hour) + ":" + leading_zero + str(eta.minute) + " {:.1f} minutes".format(result[0]) + "  {:.1f} miles".format(result[1]/1.609) )
except WazeRouteCalculator.WRCError as err:
        print("error:",err)
 