"""
This module contains functions for calculating the position
of the sun at a given date and time.
Created for NST 1 AST Observation project
Author: Alan Xu
"""
import Observer
from astropy.time import Time
from astropy.coordinates import EarthLocation

def get_sun_position(dates, times, longitudes, latitudes):
    """
    Get the position of the sun at a given date and time.

    Parameters
    ----------
    dates : list of str
        List of dates in ISO format (YYYY-MM-DD).
    times : list of str
        List of times in ISO format (HH:MM:SS).
    longitudes : list of float
        List of longitudes in degrees.
    latitudes : list of float
        List of latitudes in degrees.

    Returns
    -------
    list of tuple
        A list of tuples containing the altitude and azimuth of the sun at each location.
    """
    for date, time, longitude, latitude in zip(dates, times, longitudes, latitudes):
        # Create an EarthLocation instance for the given longitude and latitude
        location = EarthLocation.from_geodetic(longitude, latitude)

        # Create an Observer instance for the given location
        observer = Observer(location=location)

        # Combine date and time into a single string, and convert it into a Time instance
        datetime_str = f"{date}T{time}"
        datetime = Time(datetime_str)

        # Get the altazimuth coordinate frame for the given datetime
        altaz = observer.sun_altaz(datetime)

        # Print the altitude and azimuth
        print(f"Date: {date}, Time: {time}, Altitude: {altaz.alt.deg}, Azimuth: {altaz.az.deg}")

# Input observation data
dates = ['2023-10-09', '2023-10-02', '2023-09-20', '2023-10-13']
times = ['17:51:09', '17:55:03', '18:26:24', '17:44:57']
longitudes = [-71.26575556, -71.26577778, -71.26574722, -71.26578611]
latitudes = [42.29589722, 42.29591111, 42.295925, 42.29589167]

get_sun_position(dates, times, longitudes, latitudes)