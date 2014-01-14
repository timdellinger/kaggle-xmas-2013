"""
make histograms of the sizes (specifically, the volumes) of the gifts in the dataset
input is  presentVolumes.csv  (one volume on each line, with order preserved)

note that the small gifts dominate the y-axis when the full dataset is plotted.
code that only plots subsets of the data is commented out below... uncomment to plot that subset

Tim Dellinger
Kaggle Santa Challenge, Christmas 2013

"""

from numpy import array
import pylab as P

numberOfBins = 100

volumes =  []

with open('twentyPresentVolumes.csv','r') as f:
    for line in f:
        volumes.append( int(line[:-1]))     # strip the newline characters and convert to integers
        


# if you only want to plot a subset:
# volumes = [ i for i in volumes if i > 400000 ]    
# volumes = [ i for i in volumes if 500 < i < 400000 ]
# volumes = [ i for i in volumes if i < 1250 ] 

volumes = array(volumes)   # plotting requires conversion to an array

P.hist(volumes,numberOfBins)
P.show()
