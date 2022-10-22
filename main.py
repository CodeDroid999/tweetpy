#______________________________________________
#   
#    CIS 612 Lab Assignment 3 
#
#        Author: 
#______________________________________________ 

#import libraries
import pymongo
from pymongo import MongoClient
import json
import tweepy
import twitter
from pprint import pprint
import configparser
import pandas as pd
import sys

def run_scripts():
    print "error in running_scripts"

if __name__ == '__main__':
    # executed as script
    print 'script successfully executed, proceeding to next'
    run_scripts()


import streamlistener
import mongodb_util
import sql_util
import configparse

def service_func():
    print 'service func'

if __name__ == '__main__':
    service_func()
    run_scripts.run1-4()


# run the scraping for one hour
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def MyStreamListener()

t = Timer(secs, MyStreamListener)
t.start()


y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)

