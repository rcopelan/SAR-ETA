import logging
import datetime
import math 

import PySimpleGUI as sg
import WazeRouteCalculator
from progress.bar import Bar
bar = Bar('Loading')

#
# set defaults and initialize variables
#
#sg.theme('DarkAmber')
error_msg = ""
win1_event = ""
end_program = False

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
team = {"Angelo Capozzoli": "140 Ketton Way, Alpharetta, GA 30005",
        "Barry Bozeman": "303 Cross Pointe Way, Hiram, GA 30141",
        "Beverly Benton": "5830 Wembley Drive Douglasville, GA 30135",
        "Cheryl Knieriemen": "138 Courtland Circle Powder Springs, GA  30127",
        "Dawn Welch": "5175 Hwy 41 South Buena Vista, GA 31803",
        "Gary Bonneau":   "4110 Night Sky Ln Cumming, GA 30041",
        "Heidi Morris-Taylor": "5373 Zachery Drive Stone Mountain, GA 30083",
        "Hilary Nickerson": "315 Oxford Meadow Run Alpharetta, GA 30004", 
        "James Martin": "790 Huff Road Atlanta, GA 30318",     
        "Jennifer Kingsley": "4190 Everett Springs Rd. NE Armuchee, GA 30105",
        "Jennifer/Maddy Sheppard": "1702 Frazier Park Drive Decatur, GA 30033",
        "Joel Barrett": "3458 Dunlin Shore Court, Peachtree Corners, GA 30092",
        "Nina Kozlova": "92 Regency Rd Alpharetta, GA 30022",
        "Pam Nyberg": "2705 Diamond Head Court Decatur, GA 30033",
	 "Patrick Hislar": "3211 Katelyn Ct.  SW Liburn, GA 30047",
        "Phil Schillinger": "281 Mallard Dr Carrollton, GA 30116",
        "Robert Copelan": "5911 Jim Crow Road Flowery Branch, GA 30542",
        "Sherri Schwartz": "4703 Cambridge Drive Dunwoody, GA 30338",
        "Stephan Keech": "490 Lindbergh PL NE Apt. 540 Atlanta, GA 30324",
        "Tim Ward": "4300 Hwy 411 NE Rydal, GA 30171",
        "Tony Polizzi": "3031 Andora Drive SW Marietta, GA 30064",
        "Orby Taylor": "4225 Brass Trail Austell, GA 30105",
        "James Martin": "790 Huff Rd NW, Atlanta, GA 30318"
       }

layout_a = [[sg.Text('select deploying members')]] 
layout_error = [sg.Text(error_msg)]    
layout_buttons = [sg.Button('Calculate ETA'), sg.Button('Clear'), sg.Button('Repeat'), sg.Button('Exit')]

text_lines = ""
col = [sg.Text(text_lines, text_color='white', background_color='blue',size=(50,10))]
win1_event = "Clear"
first_time = True
while (True):
  print ("first_time:",first_time,"\nwin1_event:",win1_event,"\n")
  if first_time == False:
      print ("First time is FALSE") 
      win1.Close()
      layout2 = []
  first_time = False
  if win1_event == "Clear":
      key_array = []
      layout_lines = []       
      recid = 0
      for member,addr in team.items():
          test_line = []
          key_array.append(member)
          test_line.append(sg.Checkbox(member))
          layout_a.append(test_line)
          recid += 1
      col = [sg.Text('', text_color='white', background_color='blue',size=(50,10))]
      layout_top = layout_a
      layout_b = layout_a
      layout_b.append([sg.Input("",size=(40,1))])
      if (error_msg):
          layout_b.append(layout_error)
      layout_b.append(layout_buttons)
      layout2 = layout_b
  print ("key_array:",key_array)

  #while (True):
  if (end_program):
        print("process to end program")
        break
  if win1_event == "Repeat":
     win1_values = old_win1_values
     win1_event = "Calculate ETA"
     print ("Repeat: ",win1_values,"\n",win1_event)
     #win1.Close()
     repeat = True
  else: 
     repeat = False
  if win1_event == "Calculate ETA":
    old_win1_values = win1_values
    print (len(win1_values))
    to_address = win1_values[len(win1_values)-1]
    print ("New To address is:", to_address)
    layout2 = []
    deploy_list = []
    layout_top2 = layout_top 
    current_time = datetime.datetime.now()
    if current_time.minute < 10:
        leading_zero = "0"
    else:
        leading_zero = ""
    print ("It is now:", str(current_time.hour) + ":" + leading_zero + str(current_time.minute) + "\n")
    print ("Estimated travel time to:\n    ", to_address,"\n *** Calculating ***\n\n")
    indx = 0
    while indx < len(win1_values)- 1:
        bar.next()
        if win1_values[indx]:
            #for member,addr in team.items(): 
            from_address = team[key_array[indx]]
            member = key_array[indx]
            #from_address = addr
            try:
                route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
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
        indx += 1
    bar.finish()
    print (deploy_list)
        #print ("\n\n")
        #print (Sort(deploy_list) )
    if current_time.minute < 10:
        leading_zero = "0"
    else:
        leading_zero = ""
    text_lines_str = to_address + "  " + str(current_time.hour) + ":" + leading_zero + str(current_time.minute) + "\n"
    num_deploying = 0
    total_minutes = 0 
    for members in Sort(deploy_list):
        minutes = datetime.timedelta(minutes= math.ceil(members[1]))
        num_deploying += 1
        total_minutes  = total_minutes + (minutes.total_seconds() / 60)    
        eta = current_time + minutes
        if eta.minute < 10:
            leading_zero = "0"
        else:
            leading_zero = ""
        print ("{:<30} {:^8} {:.0f} minutes  {:.0f} miles".format(members[0], str(eta.hour) + ":" + leading_zero + str(eta.minute), math.ceil(members[1]),math.ceil(members[2])))
        text_lines_str = text_lines_str + "{:<25} {:^8} {:.0f} minutes  {:.0f} miles".format(members[0], str(eta.hour) + ":" + leading_zero + str(eta.minute), math.ceil(members[1]),math.ceil(members[2])) + "\n"
#       text_lines_str = text_lines_str + members[0] + " " +  str(eta.hour) + ":" + leading_zero + str(eta.minute) + "  " + str(math.ceil(members[1])) + " minutes  " + str(math.ceil(members[2])) + " miles\n"
    text_lines_str = text_lines_str + "Average Travel Time: " + str(total_minutes / num_deploying) + " minutes"
    layout2.append([sg.Text(text_lines_str, text_color='white', background_color='blue',size=(80,30))])
    layout2.append([sg.Button('Calculate ETA'), sg.Button('Clear'), sg.Button('Repeat'), sg.Button('Exit')])
    win1.Close()
    
  win1 = sg.Window('SAR Deploy' + " 001", layout2,resizable=True, font='Courier 9')     
  win1_event, win1_values = win1.Read()
   
  print("\nAfter Win1 Read, event: ", win1_event,"\nvalues: ", win1_values)
  if win1_event == sg.WIN_CLOSED or win1_event == 'Exit':
      end_program = True
  indx = 0
  while indx < len(win1_values)-1:
      if win1_values[indx]:
          print (key_array[indx],team[key_array[indx]])
      indx += 1


