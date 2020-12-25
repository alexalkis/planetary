import math
import ephem
from datetime import datetime
import time
import matplotlib.pyplot as plt
from ephem import Observer


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red = '\033[31m'  # red
    Green = '\033[32m'  # green


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


# class COORDS:
#     x = 0
#     y = 0


# def azaltConvert(az, alt):
#     res = COORDS()
#     res.x = 10
#     res.y = 100


localTime = datetime.now()
x = datetime.utcnow()
print(localTime)

# observer = ephem.Observer()
observer: Observer = ephem.city('Athens')
observer.date = ephem.Date(x).tuple()

# print observer.date

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

theta_plot = []
r_plot = []
labels = []

for planet in planets:
    planet.compute(observer)
    if planet.alt > 0:
        color = bcolors.Green
        theta_plot.append(planet.az)
        foo = 90 - (90 * (planet.alt / ephem.halfpi))
        r_plot.append(foo)
        labels.append(planet.name)
    else:
        color = bcolors.Red

    if planet.name == "Moon":
        print(color + "%s %s %s %s (Moon phase %.2f)" % (
            planet.name, planet.az, planet.alt, planet.mag, planet.moon_phase), end="")
    else:
        print(color + "%s %s %s %s (%.2fAU)" % (planet.name, planet.az, planet.alt, planet.mag, planet.earth_distance),
              end="")

    if planet.transit_time != None:
        print(" Transit time: %.2d:%.2d:%.2d" % (
        ephem.localtime(planet.transit_time).hour, ephem.localtime(planet.transit_time).minute,
        ephem.localtime(planet.transit_time).second))
    else:
        print("")

    if planet.name == "Moon":
        print(color + "Next new Moon: %s" % ephem.next_new_moon(x))
        print(color + "Next first quarter Moon: %s" % ephem.next_first_quarter_moon(x))
        print(color + "Next full Moon: %s" % ephem.next_full_moon(x))
        print(color + "Next last quarter Moon: %s" % ephem.next_last_quarter_moon(x))
        print(color + "Moon distance from earth: %.2f meters\n" % (planet.earth_distance * ephem.meters_per_au))
    if planet.name == "Sun":
        if planet.alt > 0:
            print("Sunset: %s" % (ephem.localtime(observer.next_setting(planet))))
        else:
            print("Sunset: %s" % (ephem.localtime(observer.previous_setting(planet))))
        print("Sunrise: %s" % (ephem.localtime(observer.previous_rising(planet))))
        print("")

print(bcolors.ENDC)

# from pprint import pprint
# pprint (vars(ephem))

try:
    # plot initialization and display
    ax = plt.subplot(111, polar=True)

    ax.set_theta_direction(-1)  # clockwise
    ax.set_theta_offset(math.pi / 2)  # put 0 degrees (north) at top of plot
    ax.yaxis.set_ticklabels(["80", "70", "60", "50", "40", "30", "20", "10"], fontsize=10)  # hide radial tick labels
    ax.grid(True)
    title = str(localTime)
    ax.set_title(title, va='bottom')
    ax.scatter(theta_plot, r_plot, picker=True)
    for label, xpt, ypt in zip(labels, theta_plot, r_plot):
        ax.text(xpt - 0.04, ypt, label)
        # fig.canvas.mpl_connect('pick_event', onpick)
    ax.set_rmax(90.0)
    plt.show()
except:
    print("Can't seem to open a window for sky chart")
