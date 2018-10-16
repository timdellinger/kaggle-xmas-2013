kaggle-xmas-2013
================

Python code for Kaggle's Christmas 2013 Challenge ( http://www.kaggle.com/c/packing-santas-sleigh )

(update 2018: this code is quite outdated, and pre-dates a lot of the modern python plotting and data
 manipulation libraries.  In other words, it does a number of things by hand (the hard way) that are
 simple one-liners today.  It gets the job done, though!)
 
Tim Dellinger



calculateVolumes.py - reads presents.csv, spits out a file with the volume of
    each present on a separate line (presentVolumes.csv)
 
totalVolume.py - sums the volumes of all presents

makeVolumeWeightedBarCart.py - reads in presentVolumes.py, makes a histogram of the sizes (namely, the volumes)
    of the gifts in the dataset - here by Volume not by number, i.e the value on the y-axis is the total *volume*
    of all gifts of that size, not the total *number* of gifts of that size.  ralue on the x-axis the size of the gift.
    
volumeWeightedBarChart.png - result of makeVolumeWeightedBarChart.py    
       
makeHistograms.py - make histograms of the sizes (specifically, the volumes) of the gifts in the dataset
    input is  presentVolumes.csv  (one volume on each line, with order preserved).  note that the small gifts
    dominate the y-axis when the full dataset is plotted.  code that only plots subsets of the data is commented
    out... uncomment to plot that subset
