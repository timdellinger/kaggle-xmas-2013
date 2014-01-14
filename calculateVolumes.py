"""
Some analysis of the gift file: 
we begin by creating a list of the volumes of each gift, output to the file 'presentVolumes.csv'
as a file with each volume on a separate line

input is the presents.csv file from the challenge website


Tim Dellinger
Kaggle Santa Challenge, Christmas 2013

"""



from numpy import product, array
import csv

# first we read presents.csv into memory as a list of lists: [ [length1,width1,height1], ... ]
# I like the list instead of a dictionary since it preserves the original order

giftDimensions = []

with open('presents.csv', 'rb') as f:
    f.readline() # skip the header
    fcsv = csv.reader(f)
    for row in fcsv:
        giftDimensions.append(map(int,row[1:]))    # strip the first element (presentID), keep the dimensions as ints

        

volumes = []
# volume is simply length * width * height)
for dims in giftDimensions:
    volumes.append( product(dims))
    

with open('betterPresentVolumes.csv','w') as f:
    for v in volumes:
        f.write (str(v)+'\n')    # each line is a volume, then a newline character
                                 # if you have a peek at the output file, the last volume will have a newline
                                 # so you'll see a blank line afterwards.  This is actually useful since all
                                 # lines will end with a newline character (including the last), so the last
                                 # line won't have to be treated differently than the precending lines
        
    
