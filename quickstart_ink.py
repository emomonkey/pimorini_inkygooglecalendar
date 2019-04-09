from __future__ import print_function
import datetime
import pickle
import os.path
import argparse
import time
from datetime import timedelta 

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky import InkyPHAT, InkyWHAT
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def getGoogleCalendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    return events_result.get('items', [])
    


def main():
    scale_size = 1
    padding = 0
    colour = "black"
    inky_display = InkyPHAT(colour)
    inky_display.set_border(inky_display.BLACK)
    # Top and bottom y-coordinates for the white strip
    y_top =  int(inky_display.HEIGHT * (1.0 / 10.0))
    y_bottom = y_top  + int(inky_display.HEIGHT * (1.0 / 10.0))

    imgclr = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))          
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    # Load the fonts

    intuitive_font = ImageFont.truetype(Intuitive, int(18 * scale_size))
    hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(19 * scale_size))
    
    name_y = y_top
   
    # find width. Calculate no lines
    # Split Text No Lines
    # print each line
    # when no lines gets to height display and sleep and set height to top
    # when finished start again
    name_x = 0
    i = 0
    polltime  = datetime.datetime.now() - timedelta(minutes=2)
    now = datetime.datetime.now()
    # Loop forever
    while i < 1:
      if polltime <  datetime.datetime.now():
           polltime = datetime.datetime.now() + timedelta(minutes=2)
           events = getGoogleCalendar()
           #print('while loop' + polltime.strftime("%H%M"))

 
      for event in events: 
         draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill='black', outline='black')
         name_w, name_h = intuitive_font.getsize(event['summary'])
         no_lines = round(name_w / inky_display.WIDTH) 
         no_left =  name_w % inky_display.WIDTH
                  
         draw.text((name_x, int(inky_display.HEIGHT * (0.5 / 10.0))),\
         now.strftime("%Y-%m-%d %H:%M"),inky_display.BLACK,font=hanken_medium_font)
         no_loop = no_lines
         if no_left > 0:
            no_loop = no_loop + 1
       
         curr = 0
         curr_x = 0 
         while curr < no_loop: 
            s = event['summary']
            
            if curr != no_lines:
               curr_line = s[curr_x : curr_x + 25]
               curr_x = curr_x + 25
            else:
               curr_line = s[curr_x : curr_x + no_left]
            name_y = name_y + name_h + padding
            draw.text((name_x, name_y), curr_line, inky_display.BLACK,\
               font=intuitive_font)
            if curr == no_lines or ((no_left > 0 and \
            no_lines == 0)  ):
               name_y = name_y + name_h + padding
               event_date = event['start'].get('dateTime')
               draw.text((name_x, name_y),event_date[0:10] + ' ' + event_date[11:16] ,inky_display.BLACK,font=hanken_medium_font )

               inky_display.set_image(img)
               inky_display.show()
               time.sleep(15)
               name_y = y_top
               curr = no_loop
               break
            else:
               curr = curr + 1

            
if __name__ == '__main__':
      main()
