import argparse
import csv
from datetime import datetime
from astropy.coordinates import SkyCoord, EarthLocation, get_moon
from astropy.time import Time
import astropy.units as u
from astroplan import Observer, FixedTarget, is_always_observable
from astroplan import AltitudeConstraint, TargetAlwaysUpWarning
from astroplan.constraints import AltitudeConstraint

def get_info_of_target(target, *args, **kwargs):
    ra=target.ra
    dec=target.dec
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
    print(target.name, rise_time_IST ,set_time_IST, sep)