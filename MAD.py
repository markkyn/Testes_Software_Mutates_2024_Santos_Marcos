import math

def MeanAbsDeviation(valueArray):
    NumberofValues = len(valueArray)

    # Calculate the mean
    Mean = 0
    for val in list(valueArray):
        Mean += val
    Mean /= NumberofValues
    print ("Program Mean: " + str(Mean))


    # Calculate MAD
    MAD = 0
    diff = 0
    for val in list(valueArray):
        diff = val - Mean
        if diff < 0:
            diff *= (-1)
        MAD += diff

    MAD /= NumberofValues
    print("Program MAD: " + str(MAD))



        





MeanAbsDeviation([-1, 1, 3])















