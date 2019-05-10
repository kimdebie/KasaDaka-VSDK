from django_cron import CronJobBase, Schedule
import urllib.request
import json


class MonthlyCronJob(CronJobBase):
    API = 'http://api/monthly'    
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'weather.month_cron_job'    

    def do(self):
        webURL = urllib.request.urlopen(self.API)
        encoding = webURL.info().get_content_charset('utf-8')

        serialized_data = webURL.read()
        weather_data = json.loads(serialized_data.decode(encoding))
        print("MONTHLY: ", weather_data)


class WeeklyCronJob(CronJobBase):
    API = 'http://api/weekly'
    RUN_EVERY_MINS = 1 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'weather.weekly_cron_job'   

    def do(self):
        webURL = urllib.request.urlopen(self.API)
        encoding = webURL.info().get_content_charset('utf-8')

        serialized_data = webURL.read()
        weather_data = json.loads(serialized_data.decode(encoding))
        print("WEEKLY: ", weather_data)