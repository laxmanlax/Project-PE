# QUESTION: 1
"""
---------
Question
---------
You will be supplied with two data files in CSV format. The  first file contains
statistics about various dinosaurs. The second file contains additional data.

Given the following formula,
-----
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)
-----

Write a program to read in the data files from disk, it must then print the
names of only the bipedal dinosaurs from fastest to slowest. Do not print any
other information.


dataset1.csv
-----------
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptor,2.62,bipedal

dataset2.csv
------------
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivor

"""

"""
Approach 1st
"""
from math import sqrt

fname1 = "dataset1.csv"
fname2 = "dataset2.csv"

g = 9.8

d1 = {}
d2 = {}

d3 = {}

with open(fname1, 'r') as file:
    next(file)
    for info in file:
        data = info.split(",")

        name = data[0]
        info1 = data[1]
        info2 = data[2][:-1]

        d1[data[0]] = [info1, info2]

with open(fname2, 'r') as file:
    next(file)
    for info in file:
        data = info.split(",")

        name = data[0]
        info1 = data[1]
        info2 = data[2][:-1]

        d2[data[0]] = [info1, info2]


for d in d1.keys():
    if d not in d2:
        continue

    if d2[d][1]!= "bipedal":
        continue

    leg = float(d1[d][0])
    stride = float(d2[d][0])
    speed = ((stride / leg) - 1) * sqrt(leg * g)
    d3[d] = speed

for name in sorted(d3.items(), key=lambda x:x[1], reverse=True):
    print (name)

"""
Approach 2nd
"""
import csv
from math import sqrt

filenames = ['dataset2.csv','dataset1.csv']
g = 9.8
dino_info = {}

for fname in filenames:
    with open(fname, 'r') as re:
        csv_data = csv.DictReader(re)

        for data in csv_data:
            name = data["NAME"]

            if "STANCE" in data:
                if data["STANCE"] == "bipedal":
                    if name not in dino_info:
                        dino_info[name] = data
                    else:
                        dino_info[name].update(data)
            else:
                if name in dino_info:

                    dino_info[name].update(data)
result = {}
for name, info in dino_info.items():
    if "LEG_LENGTH" not in info:
        continue

    print (name, info)
    STRIDE_LENGTH = float(info["STRIDE_LENGTH"])
    LEG_LENGTH = float(info["LEG_LENGTH"])

    speed = speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
    result[name] = speed


for dino in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print (dino)
