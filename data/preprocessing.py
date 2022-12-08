import os
import pickle
import random

from helper import *

cwd = os.getcwd() # /preprocessing
# parent_wd = cwd.replace('/preprocessing', '')
main_wd = '/content/capstone_moonboard'
raw_data_path = main_wd + '/raw_data/moonGen_scrape_2016_final'

def get_grade_map():
    """
    Defines a mapping of Fontainebleau grades to integer values
    """
    grade_map = {
        '6B': 0,  # V4
        '6B+': 0, # V4
        '6C': 1,  # V5
        '6C+': 1, # V5
        '7A': 2,  # V6
        '7A+': 3, # V7
        '7B': 4,  # V8
        '7B+': 4, # V8
        '7C': 5,  # V9
        '7C+': 6, # V10
        '8A': 6,  # V11
        '8A+': 6, # V12
        '8B': 6,  # V13
    }
    return grade_map
grade_map = get_grade_map()

# get raw data
with open(raw_data_path, 'rb') as f:
    MoonBoard_2016_raw = pickle.load(f)
print('Number of routes after scraping:', len(MoonBoard_2016_raw))

# clean data
mb_2016 = {}
fields = ['start', 'mid', 'end', 'grade', 'user_grade', 'is_benchmark', 'repeats', 'url']
legal_routes = []

for key, item in MoonBoard_2016_raw.items():
    if (item['grade'] in grade_map) and (item['user_grade'] in grade_map or item['user_grade']==None) and (len(item['start']) <= 2) and (len(item['end']) <= 2) and (item['repeats'] > 0):
        legal_routes.append(key)

for key in legal_routes:
    mb_2016[key] = {}
    for f in fields:
        mb_2016[key][f] = MoonBoard_2016_raw[key][f]
    for f in ['grade', 'user_grade']:
        if mb_2016[key][f] != None:
            mb_2016[key][f] = grade_map[mb_2016[key][f]]
print('Number of routes after cleaning:', len(mb_2016))
