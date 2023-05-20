import platform
import requests
# Set up API credentials
api_key = '774990ac82b72039c7d936663b5b56fa'

# Define function to get location details for a single IP
def get_location(ip):
    url = f'http://api.ipapi.com/{ip}?access_key={api_key}'
    response = requests.get(url)
    data = response.json()
    try:
        city = data['city']
        latitude = data['latitude']
        longitude = data['longitude']        
        state = data['region_name']
        country = data['country_name']
        country_flag = data['location']['country_flag']
    except KeyError as a:
        latitude, longitude, city, state, country = 0, 0, None, None, None
    return (ip, latitude, longitude, city, state, country, country_flag)

def get_locations(ip_list):
    locations = []
    for ip in ip_list:
        location = get_location(ip)
        locations.append(location)
    return locations


def getMyLoc():
    '''
    return: MyIP, lon,lat,city
    '''
    url = 'https://ipapi.co/json/' 
    response = requests.get(url)
    data = response.json()
    print(data)
    try:
        myIP = data['ip']
        lon =data['longitude']
        lat = data['latitude']
        city = data['city']
        state = data['region']
        country = data['country_name']
    except KeyError as a:
        print(f'Error: {a} Not Found')
        lat, lon, city, state, country = 0, 0, None, None, None
    return ([myIP, lat, lon, city, state, country])

def getTargetLoc(IP):
    '''
    input: IP
    return: lon,lat,city
    '''
    url = f'https://ipapi.co/{IP}/json/'
    response = requests.get(url)
    data = response.json()
    try:
        lon =data['longitude']
        lat = data['latitude']
        city = data['city']
        state = data['region']
        country = data['country_name'] 
    except KeyError as a:
        lat, lon, city, state, country = 0, 0, None, None, None
    return ([IP, lat, lon, city, state, country])