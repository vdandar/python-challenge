# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:03:15 2020

@author: Valerie
"""

import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
length = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(udemy_csv, newline='',encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
       
        rse_title= row[1]
        course_price= row[4]
        course_subs= row[5]
        course_reviews= row[6]
        course_length = row[9]

	 # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])

        # Add amount of reviews
        reviews.append(row[6])
        
      
        length.append(row[9])
      
# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, length)

# Set variable for output file
output_file = os.path.join("web_final_vmd.csv")

#%%

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
