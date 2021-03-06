<!--
  Title: Google Calender Script for Pimorini EInk PHAT Display
  Description: Google Calender Script for Pimorini EInk PHAT Display
  Author: emos
  -->
# Google Calender Script for Pimorini EInk PHAT Display

I have put together a little python script which lists your most recent events you have put on the Google Calendar.


Now some of this code is pulled from the quickstart.py program found on the Google Calendar Developers page at 
https://developers.google.com/calendar/quickstart/python . 
This program lists how to pull the events from your own Google Calendar. 
There is also a step listed (Called ENABLE GOOGLE CALENDAR API) here which you will need to carry out to produce your own credentials.json 
file. You will need this file later on.

The next step is to enable the Inky python library produced by Pimorini. 
This code uses the small EInk Display designed for the Raspberry PI.
It is designed for the Raspberry PI Zero but you can see from my screenshot that I use it on the full sized Raspberry PI 3. 
Now follow the instructions that are required to install this library detailed 
on https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat . 
There will be a few pip installs for various libraries but they have an shell installation script to guide you through this.

The next step is to download the code I have on github https://github.com/emomonkey/pimorini_inkygooglecalendar. 
Replace the blank credentials.json file with the one you generated earlier on.

To run the script type python quick_start.py and the small eink display will change every 30 seconds cycling through your next 10 events
you have listed on Google Calendar. The program will run forever. You may want to have it start on booting up your Raspberry PI so you 
would want to set up a cron job for this.

The script has also been updated to poll Google Calendar for any updates on a regular basis. These timeframes can be updated from within  the Script.

Further details on <a href="http://emomonkey.github.io">Blog</a>
