import os
import numpy as np
import pandas as pd
import pickle
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

from preprocessing import *

cwd = os.getcwd() # /preprocessing
parent_wd = cwd.replace('/preprocessing', '')
# hold_feature_path = parent_wd + '/raw_data/HoldFeature2016.xlsx'

# images
img_wd = parent_wd + '/images'
mb_2016_img_path = img_wd + '/mb_2016_img.jpeg'
mb_2016_img = cv2.imread(mb_2016_img_path)

def show_image():
    cv2.imshow("image", mb_2016_img)
    plt.imshow(cv2.cvtColor(mb_2016_img, cv2.COLOR_BGR2RGB))
    # plt.gcf().set_dpi(300)
    plt.axis('off')
    # plt.grid(alpha=0.2)
    plt.show()

def get_coor(hold):
    x, y = hold
    x_coor = 94 + x*51
    y_coor = 958 - y*51
    return (int(x_coor), int(y_coor))


def add_hold(hold, img, hold_type):
    """
    add hold to moonboard image
    """
    circle_color = {
        'start': (0,255,0),
        'mid': (255,0,0),
        'end': (0,0,255),
    }
    center = get_coor(hold)
    c = circle_color[hold_type]
    cv2.circle(img = img, center = center, radius = 28, color = c, thickness=5)

# main function:
def display_route(route):
    """
    display an entire route on an image
    """
    img = mb_2016_img.copy()
    for key, item in route.items():
        # key is hold type, item is list of holds
        for hold in item:
            add_hold(hold, img, key)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.gcf().set_dpi(150)
    plt.axis('off')
    plt.show()

# example:
# r = {'start': [[0,0]], 'mid': [[2,2], [6,6]], 'end': [[0,17],[4,17]]}
# display_route(r)

def draw_samples(data, n):
    """
    draw n samples of routes from data (dictionary)
    """
    samples = {}
    for item in random.sample(list(data.items()), n):
        samples[item[0]] = item[1]
    return samples

# hold types is a list of combination of 'start', 'mid', 'end'
def get_holds(item, hold_types):
    """
    get a list of holds from a route
    """
    route = []
    for t in hold_types:
        for hold in item[t]:
            route.append(hold)
    return route

def convert_matrix(list):
    """
    convert a list of holds to 11*18 matrix
    """
    matrix = np.zeros((11,18))
    for hold in list:
        x = hold[0]
        y = hold[1]
        matrix[x][y] = 1
    return matrix

def display_matrix(matrix):
    """
    flip the matrix to present as 18*11
    """
    return np.flip(matrix.T, 0)

def get_matrices(data, hold_types):
    """
    return a dictionary and a list of matrices for the data input (eg mb_2016)
    """
    d = {}
    l = []
    for key in data:
        route = get_holds(data[key], hold_types)
        d[key] = display_matrix(convert_matrix(route))
        l.append(display_matrix(convert_matrix(route)))
    return d, l

def heat_matrix(data, grades_list):
    """
    return heat matrix given a list of grades
    """
    d = {}
    for key, item in data.items():
        if item['grade'] in grades_list:
            d[key] = item
    matrix_list = get_matrices(d, ['mid'])[1]
    return sum(matrix_list)/len(matrix_list)
