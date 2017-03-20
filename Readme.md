# Planetary #

It's a testbed for learning both astronomy libraries (pyephem) and/or python.


python3.5 planetary.py runs on my machine.  No promises if you try it on your own.

Ubuntu setup
------------

On ubuntu I had to do the following before actually being able to run it.

    sudo apt install python3-pip
    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install setuptools
    sudo apt install python3-dev
    sudo -H pip3 install pyephem


Sample Output
-------------

    python3.5 planetary.py 
    2017-03-20 23:35:53.947787
    Sun 337:50:22.0 -49:40:47.6 -26.8 (1.00AU) Transit time: 12:32:32
    Sunset: 2017-03-20 18:37:16
    Sunrise: 2017-03-20 06:28:26
    
    Moon 95:23:39.0 -25:23:54.6 -11.74 (Moon phase 0.48) Transit time: 06:09:50
    Mercury 325:09:50.0 -40:00:47.6 -1.13 (1.18AU) Transit time: 13:19:15
    Venus 337:55:59.4 -38:30:50.0 -3.89 (0.28AU) Transit time: 12:48:19
    Mars 308:41:09.0 -20:20:20.2 1.42 (2.16AU) Transit time: 14:52:39
    Jupiter 137:51:27.8 35:49:36.5 -2.28 (4.51AU) Transit time: 01:48:19
    Saturn 101:36:12.3 -21:49:46.9 0.46 (9.95AU) Transit time: 06:22:59
    Neptune 4:16:58.6 -59:38:51.4 7.96 (30.90AU) Transit time: 11:29:04
    Uranus 316:59:59.0 -33:05:38.8 5.91 (20.85AU) Transit time: 13:58:31
    Pluto 87:06:28.2 -39:31:59.4 14.3 (33.60AU) Transit time: 07:55:40


In a terminal bodies under the horizon are colored red, while when above the horizon are colored green.
