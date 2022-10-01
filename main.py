import json
import requests

'''print(json.dumps(data, indent=4, sort_keys=True))'''
'''print(data['TrackerHTTPS'])'''
'''print(json.dumps(data['TrackerHTTPS'], indent=4, sort_keys=True))'''
'''print(data['TrackerHTTPS']['Status'])'''

def main():
    '''main function'''
    api_list = 'https://ptp.trackerstatus.info/api/all/'

    data = get_api(api_list)

    if status_check(data) == 'down':
        downtime = current_downtime(data)
        print('PTP has been down for ' + str(downtime // 60) + ' hours')

def status_check(data):
    '''function to check status of tracker'''
    if data['TrackerHTTPS']['Status'] == '0':
        return 'down'
    elif data['TrackerHTTPS']['Status'] == '1':
        return 'up'

def current_downtime(data):
    '''function to check current downtime'''
    return int(data['TrackerHTTPS']['CurrentDowntime'])

def get_api(api_list):
    '''function to get api data'''
    response = requests.get(api_list)
    return json.loads(response.text)

if __name__ == '__main__':
    main()
