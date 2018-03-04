import sched
import time
import requests
import subprocess
import datetime
from requests.exceptions import ConnectionError

# This script work for all pools in nanopool ETH, ETC, SIA, ZEC, XMR, PASC, ETN  
# Url for hash rate history. More info  https://etc.nanopool.org/api#api-Miner-HashrateHistory
# Put your url address

url = 'https://api.nanopool.org/v1/etc/hashrate/0x5b184fa7e6bae0a7e2a8701e826d002829644399'


first_check_time_after_start = 300 #sec.
repeat = 60
repeat_after_connection_error = 15 
min_hash_for_rebooting = 10
max_connection_error_before_rebooting = 10

class Reboot(object):
    def __init__(self, url):
        self.url = url
        self.net_error_count = 0

        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(first_check_time_after_start, 1, self.get_hash_rate, (self.s,))
        self.s.run()

    def get_hash_rate(self, sc):
        print("Try To Get Data From Nanopool")
        try:
            r = requests.get(self.url)
            json = r.json()

            status = False
            hash_rate = 0

            if "status" in json.keys():
                status = json["status"]
            if "data" in json.keys():
                hash_rate = json["data"]

            print(status)
            print(hash_rate)
            
            if not status:
                self.reboot_if_needed(sc)
            else:
                self.net_error_count = 0
                if hash_rate <= min_hash_for_rebooting:
                    self.force_reboot()

                self.s.enter(repeat, 1, self.get_hash_rate, (sc,))
        except ConnectionError as e:
            print("except net error")
            self.reboot_if_needed(sc)
    
    def force_reboot(self):
        #save info in reboot.txt before rebooting.
        now = datetime.datetime.now()
        time_info = "rebooting -->  month = " + str(now.month) + ", day = " + str(now.day) + ", hour = " + str(now.hour) + ", minute = " + str(now.minute) + "\n"
        with open("reboot.txt", "a") as f:
            f.write(time_info)
        time.sleep(1)
        subprocess.run("shutdown -r", shell=True)

    def reboot_if_needed(self, sc):
        self.net_error_count += 1
        if self.net_error_count >= max_connection_error_before_rebooting:
            self.force_reboot()

        self.s.enter(repeat_after_connection_error, 1, self.get_hash_rate, (sc,))
        print("Internet connection error count == " + str(self.net_error_count))
		

obj = Reboot(url)
