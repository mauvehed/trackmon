import json
import requests

class Trackerstatus:
    '''
        "ptp": {
        "Description": "two services unstable and three of six services offline",
        "Details": {
            "IRCServer": "0",
            "IRCTorrentAnnouncer": "0",
            "IRCUserIdentifier": "0",
            "TrackerHTTP": "2",
            "TrackerHTTPS": "2",
            "Website": "1"
        },
        "Services": {
            "offline": 3,
            "online": 1,
            "unstable": 2
        },
        "Status": "unstable",
        "URL": "https://ptp.trackerstatus.info",
        "tweet": {
            "date": "17th of June 2018",
            "message": "The website as of many hours ago is online and working correctly.",
            "unix": "1529298117"
        }
    },
    '''
    def __init__(self, site):
        self.api_list = 'https://trackerstatus.info/api/list/'
        self.site = site
#        self.data = {}

    def get_api(self):
        self.data = requests.get(self.api_list,timeout=15).json()
        return self.data

    def status_check_web(self, data):
        if data[self.site]['Details']['Website'] == '1':
            return 'online'
        elif data[self.site]['Details']['Website'] == '2':
            return 'unstable'
        elif data[self.site]['Details']['Website'] == '0':
            return 'offline'

    def status_check_tracker(self, data):
        if data[self.site]['Details']['TrackerHTTPS'] == '1':
            return 'online'
        elif data[self.site]['Details']['TrackerHTTPS'] == '2':
            return 'unstable'
        elif data[self.site]['Details']['TrackerHTTPS'] == '0':
            return 'offline'

def main():
    ptp = Trackerstatus('ptp')
    data = ptp.get_api()
    status_web = ptp.status_check_web(data)
    print(f'Website status: {status_web}')
    status_tracker = ptp.status_check_tracker(data)
    print(f'Tracker status: {status_tracker}')

# Uncomment to pretty print data['ptp']
#    print(json.dumps(data['ptp'], indent=4, sort_keys=True))

# run main() if this file is called directly
if __name__ == '__main__':
    main()
