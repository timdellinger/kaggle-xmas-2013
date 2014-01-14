"""
calculates the total volume of all gifts,
taking as input presentVolumes.csv, a file with the volume of each gift on a separate line


Tim Dellinger
Kaggle Santa Challenge, Christmas 2014

"""


volumes =  []

with open('presentVolumes.csv','r') as f:
    for line in f:
        volumes.append( int(line[:-1]))     # strip the newline characters and convert to integers

        
print sum(volumes)
