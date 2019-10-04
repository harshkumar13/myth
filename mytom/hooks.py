import argparse
import csv
import os
from datetime import datetime
from astropy.coordinates import SkyCoord, EarthLocation, get_moon
from astropy.time import Time
import astropy.units as u
from astroplan import Observer, FixedTarget, is_always_observable
from astroplan import AltitudeConstraint, TargetAlwaysUpWarning
from astroplan.constraints import AltitudeConstraint
from slackclient import SlackClient

slack_token = os.environ.get('slack_bot_token')
sc = SlackClient(slack_token)


def message_grbs(slackmessage, channel="#test_git_bbc"):
    sc.api_call(
                "chat.postMessage",
                channel=channel,
                text=slackmessage
                )


def get_info_of_target(target, created):
    ra=target.ra
    dec=target.dec
    sunrise_horizon=-12
    horizon=20
    coords = SkyCoord(ra=ra,dec=dec,unit=(u.degree,u.degree))
    hanle = EarthLocation(lat=32.77889*u.degree,lon=78.96472*u.degree,height=4500*u.m)
    iao = Observer(location=hanle, name="GIT", timezone="Asia/Kolkata")
    twilight_prime = iao.sun_rise_time(Time(datetime.utcnow()),which="next",horizon = sunrise_horizon*u.degree) - 12*u.hour
    targets_rise_time = iao.target_rise_time(twilight_prime,coords,which="nearest",horizon=horizon*u.degree)
    targets_set_time = iao.target_set_time(targets_rise_time,coords,which="next",horizon=horizon*u.degree)
    rise_time_IST = (targets_rise_time + 5.5*u.hour).isot
    set_time_IST = (targets_set_time + 5.5*u.hour).isot
    tend = targets_set_time
    mooncoords = get_moon(tend,hanle)
    sep = mooncoords.separation(coords)
    slackmessage="A new target is created target={}: It will rise at {} and set at {} and has moon seperation {}".format(target.name, rise_time_IST ,set_time_IST, sep)
    message_grbs(slackmessage)
    print('Target info has been sent')
    print(target.name, rise_time_IST ,set_time_IST, sep)