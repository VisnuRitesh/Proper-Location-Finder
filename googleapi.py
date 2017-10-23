import urllib.request,urllib.parse,urllib.error
import json
s=""
gserviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

def yninput():
    global s
    s=input('Do You want to continue | Yes or No\n')

def yesorno(a):
    if a == 'Yes' or a == 'yes' :
        return 1
    if a == 'No' or a == 'no' :
        return 0

while True:
    address=input('Enter location: ')
    if len(address)<1:
        print("Invalid Address")
        break

    url=gserviceurl+urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    urladd=urllib.request.urlopen(url).read().decode()
    try:
        js=json.loads(urladd)
    except:
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print('=====Failed to retrieve data=====')
        continue

    lat=js['results'][0]["geometry"]["location"]["lat"]
    lng=js['results'][0]["geometry"]["location"]["lng"]

    print('Latitude:', lat)
    print('Longitude:',lng)
    location=js["results"][0]["formatted_address"]
    print(location)
    yninput()
    if yesorno(s)==1:
        continue
    elif yesorno(s)==0:
        break
    else:
        print('Invalid.Print only Yes or No')
        yninput()
