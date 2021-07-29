# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:54:20 2016

@author: Brian
"""

'''
# Data is a list of dicts(of dicts)
# Each list item contains a dict with a single top-level key, which is the name of the exercise.
# The value for each exercise is it's own dict with keys like "Type", and "Main Muscles Worked" and so on. 
'''

import json
import csv
exercises = []
main_muscle = []
other_muscles = []
combo = []

with open("workout.json") as json_file:
    json_data = json.load(json_file)
   
# Extract the exercise names into excercises[] list
for i in range(len(json_data)):
    for key, value in json_data[i].iteritems():
        exercises.append(key)

# Extracts "Muscles" and "Other Muscles" used for each exercise
for i,val in enumerate(exercises):
    main_muscle.append(json_data[i][val]["Main Muscle Worked"])
    if 'Other Muscles' in json_data[i][val].keys():
        other_muscles.append(json_data[i][val]["Other Muscles"])
    else:
        other_muscles.append("none")

# Combine all the columns into a list of lists 
for i in range(len(exercises)):
    lst = [exercises[i], main_muscle[i], other_muscles[i]]
    combo.append(lst)


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(combo)