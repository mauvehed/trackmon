import json
import requests

class Trackerstatus:
    def __init__(self, site):
        self.site = site
        self.api_list = 'https://{site}.trackerstatus.info/api/all/'.format(site=self.site)
        self.data = self.data = requests.get(self.api_list,timeout=15).json()

#    def get_api(self):
#        self.data = requests.get(self.api_list,timeout=15).json()
#        return self.data

    def status_check_web(self):
        if self.data['Website']['Status'] == '0':
            time = self.data['Website']['CurrentDowntime']
            output = f"The Website has been offline for {time} minutes"
        elif self.data['Website']['Status'] == '1':
            time = self.data['Website']['CurrentUptime']
            latency = self.data['Website']['Latency']
            output = f"The Website has been online for {time} hours with a latency of {latency}"
        elif self.data['Website']['Status'] == '2':
            time = self.data['Website']['CurrentUptime']
            output = f"The HTTPS Tracker has currently been in an unstable state for {time} minutes"
        return output

    def status_check_tracker(self):
        if self.data['TrackerHTTPS']['Status'] == '0':
            status = 'offline'
            time = self.data['TrackerHTTPS']['CurrentDowntime']
        elif self.data['TrackerHTTPS']['Status'] == '1':
            status = 'online'
            time = self.data['TrackerHTTPS']['CurrentUptime']
        elif self.data['TrackerHTTPS']['Status'] == '2':
            time = self.data['TrackerHTTPS']['CurrentUptime']
            output = f"The HTTPS Tracker has currently been in an unstable state for {time} minutes"
        return output
    
def main():
    ptp = Trackerstatus('ptp')
#    data = ptp.get_api()
    status_web = ptp.status_check_web()
    print(status_web)
    status_tracker = ptp.status_check_tracker()
    print(status_tracker)

# Uncomment to pretty print data
#    print(json.dumps(ptp.data, indent=4, sort_keys=True))

# run main() if this file is called directly
if __name__ == '__main__':
    main()
