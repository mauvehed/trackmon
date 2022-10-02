import json
import requests

class Trackerstatus:
    def __init__(self,latency,uptime,downtime):
        self.api_list = {
            'latency': latency,
            'uptime': uptime,
            'downtime': downtime,
        }
        self.data = {}

    def get_api(self):
        for key, value in self.api_list.items():
            self.data[key] = requests.get(value,timeout=15).json()
        return self.data

    def status_check(self, data):
        if data['TrackerHTTPS']['Status'] == '0':
            return 'down'
        elif data['TrackerHTTPS']['Status'] == '1':
            return 'up'

    def get_uptime(self, data):
        return int(data['TrackerHTTPS']['Uptime'])

    def current_downtime(self, data):
        return int(data['TrackerHTTPS']['CurrentDowntime'])

def main():
    ptp = Trackerstatus('https://ptp.trackerstatus.info/api/latency/', 'https://ptp.trackerstatus.info/api/uptime/', 'https://ptp.trackerstatus.info/api/downtime/')
    data = ptp.get_api()
    print(json.dumps(data, indent=4, sort_keys=True))

# run main() if this file is called directly
if __name__ == '__main__':
    main()
