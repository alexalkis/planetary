import ephem
from datetime import datetime
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red  = '\033[31m' # red
    Green  = '\033[32m' # green

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset



class COORDS:
    x=0
    y=0


def azaltConvert(az, alt):
    res = COORDS()
    res.x = 10
    res.y = 100
    


l = datetime.now()
x = datetime.utcnow()
print(l)

observer = ephem.Observer()
observer = ephem.city('Athens')
observer.date = ephem.Date(x).tuple()

#print observer.date

planets = [
    ephem.Sun(),
    ephem.Moon(),
    ephem.Mercury(),
    ephem.Venus(),
    ephem.Mars(),
    ephem.Jupiter(),
    ephem.Saturn(),
    ephem.Neptune(),
    ephem.Uranus(),
    ephem.Pluto()

    ]

for planet in planets:
    planet.compute(observer)
    if planet.alt > 0 :
        color = bcolors.Green
    else:
        color = bcolors.Red

    if planet.name=="Moon":
        print(color+"%s %s %s %s (Moon phase %.2f)" % (planet.name, planet.az, planet.alt, planet.mag, planet.moon_phase), end="")
    else:
        print(color+"%s %s %s %s (%.2fAU)" % (planet.name, planet.az, planet.alt, planet.mag, planet.earth_distance), end="")
    print(" Transit time: %.2d:%.2d:%.2d" % (ephem.localtime(planet.transit_time).hour, ephem.localtime(planet.transit_time).minute, ephem.localtime(planet.transit_time).second))

    if planet.name=="Moon":
        print(color+"Next new Moon: %s" % ephem.next_new_moon(x))
        print(color+"Next first quarter Moon: %s" % ephem.next_first_quarter_moon(x))
        print(color+"Next full Moon: %s" % ephem.next_full_moon(x))
        print(color+"Next last quarter Moon: %s" % ephem.next_last_quarter_moon(x))
        print(color+"Moon distance from earth: %.2f meters\n" % (planet.earth_distance * 1.496e11))
    
    if planet.name=="Sun":
        if planet.alt>0:
            print("Sunset: %s" % (ephem.localtime(observer.next_setting(planet))))
        else:
            print("Sunset: %s" % (ephem.localtime(observer.previous_setting(planet))))
        print("Sunrise: %s" % (ephem.localtime(observer.previous_rising(planet))))
        print("")
              
print(bcolors.ENDC)


# from pprint import pprint
# pprint (vars(ephem))
