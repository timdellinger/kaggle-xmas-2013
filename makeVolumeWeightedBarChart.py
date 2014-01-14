"""
make a histogram of the sizes (namely, the volumes) of the gifts in the dataset - here by Volume not by number
i.e the value on the y-axis is the total *volume* of all gifts of that size, not the total *number* of gifts
of that size


previous code spit these volumes out as the file presentVolumes.csv 
(one volume on each line, with order preserved)

Tim Dellinger
Kaggle Santa Challenge, Christmas 2013

"""

from numpy import array, linspace
import matplotlib.pyplot as plt  

numberOfBins = 100   # number of bins in the plot

print numberOfBins

# read in the data
volumes =  []
with open('presentVolumes.csv','r') as f:
    for line in f:
        # print line
        volumes.append( int(line[:-1]))     # strip the newline characters and convert to integers

        
# create bins

highestVolume = max(volumes)    #  we'll use this again when plotting
myBins = linspace(0, highestVolume, num=numberOfBins)

# tally up the total volume (not the total number) in each bin


myYValues = []

for i in range(len(myBins)-1):       #grab the lower bound of each bin
    myYValues.append( sum (j for j in volumes if (j >= myBins[i] and j < myBins[i+1]) ) )
    # note: this traverses all million gifts once for each bin (I like the plot with ~100 bins).
    # There's likely a more efficient way.
    

print myYValues

plt.bar( myBins[1:], myYValues, width = highestVolume / numberOfBins)

plt.show()
