'''
Script Owner: Dhamodaran Pandiyan
Contact: dhamodaranpandiyan@gmail.com
Script Overview: Fetching Covid vaccine slots information.
'''

import requests
import datetime
import logging


#Constants
PUBLIC_API = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

#Need to change logic here to get input from user
age = 46
pincode = "600000"
no_days = 2

#Adding logging
logging.basicConfig(format='%(asctime)s: %(name)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class VaccineData():
    def __init__(self, age, pincode, no_days):
        self.age = age
        self.pincode = pincode
        self.no_days = no_days
        logger.info("\n\nGiven Data: \nAge: {0}\nPin Code: {1}\nDays: {2}\n\n".format(self.age, self.pincode, self.no_days))

    def get_dates_from_days(self, days):
        today = datetime.datetime.today()
        date_obj_list = [today + datetime.timedelta(days=day) for day in range(days)]
        date_list = [date_obj.strftime("%d-%m-%Y") for date_obj in date_obj_list]
        return date_list

    def get_slot_data(self):
        logger.info("Fetching Covid vaccine slot information...")
        date_list = self.get_dates_from_days(self.no_days)
        for given_date in date_list:
            URL = PUBLIC_API.format(pincode, given_date)
            result = requests.get(URL, headers=HEADER)
            if result.ok:
                response_json = result.json()
                return True, response_json
            else:
                logger.info("No Response!")
                return False, {}

vaccine_obj = VaccineData(age, pincode, no_days)
response_status, response = vaccine_obj.get_slot_data()
if response_status:
    logger.info(response)
else:
    logger.info("No Data Found!!!")