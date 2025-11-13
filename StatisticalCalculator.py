#Joao Classio   #10/29/2025     #statisticalCalculator
'''
I build this program during my statistical classes in order to practice both python
and statistics. It might receive some updates in the future.
'''
import math

#Constants
MEAN = 1 ; MEDIAN = 2 ; MODE = 3 ; VARIANCE = 4 ; STANDARD_DEVIATION = 5
ROUND_COEFFICIENT = 10

userEntryList = [] 

def main():
    userChoiceList = displayMenu()
    if MEAN in userChoiceList:
        meanCalculator()
    if MEDIAN in userChoiceList:
        medianCalculator() #TODO
    if MODE in userChoiceList:
        modeCalculator() #TODO
    if VARIANCE in userChoiceList:
        varianceCalculator() #TODO
    if STANDARD_DEVIATION in userChoiceList:
        standardDeviationCalculator() #TODO

def userEntry():
    '''
    This method receives the user numeric data input that will be used for the calculation
    and it returns a list of these numbers
    '''
    entry = "y"
    while entry != "":
        try:
            entry = input("Enter a numeric value for the list or ENTER to finish the list")
            if entry != "":
                userEntryList.append(float(entry))
        except():
            print("Invalid value")
    return userEntryList

def displayMenu():
    '''
    This method will be used to display the options for the user, so he can decided wich 
    operations the program will execute and display the results.
    It returns a list containing the option's numbers.
    '''
    choice = 0
    measuresSelected = []
    while choice <1 or choice >5:
        print('''\n    Select the measures you want to display
        ----------------------------------------------------
        1. Mean
        2. Median
        3. Mode
        4. Variance
        5. Standard Deviation
        6. Continue...
        ''')
        if measuresSelected:
            print("Your selection --> " + " ".join(str(num) for num in measuresSelected))
        try:
            choice=int(input('Enter 1,2,3,4,5 or 6  '))
            if choice == 6:
                break
            if choice >= 1 and choice <= 5 and not choice in measuresSelected:
                measuresSelected.append(choice)
                
        except:
            input('\n\nINVALID SELECTION - PRESS ENTER & TRY AGAIN ')
            choice=0
        
        choice = 0

def meanCalculator(valuesList):
    '''
    This function calculates the mean, it receives a list of numbers and returns a numeric value
    '''
    numSum = 0.0
    counter = 0
    for num in valuesList:
        numSum += num
        counter += 1
    return numSum / counter

def medianCalculator(valuesList):
    '''
    This function calculates the median, it receives a list of numbers and returns value from the list
    '''
    if len(valuesList) % 2 == 0:
        value1 = len(valuesList) // 2
        median = (valuesList[value1] + valuesList[value1 - 1]) / 2
    else:
        value1 = len(valuesList) // 2
        median = valuesList[value1]
        
    return median

'''
Functions that still need to be implemented in the future...
'''

#def modeCalculator(valuesList):
    
    #TODO - implementation
    
def varianceCalculator(valuesList, mean):
    
    accumulator = 0
    
    for i in valuesList:
        accumulator += pow(i - mean, 2)
        
    return accumulator / (len(valuesList) - 1)

    
def standardDeviationCalculator(variance):

    stDev = pow(variance, 0.5)
    
    return stDev
    
def coeficientOfVariation(standardDeviation, mean):

    cv = standardDeviation / mean
    
    return cv

def zScoreCalculator(xNumber, mean, standardDeviation):
    
    zScore = (xNumber - mean) / standardDeviation
    
    return zScore

def firstQuartileCalculator(valuesList):
    
    firstQuartilePosition = len(valuesList) * 0.25
    
    if firstQuartilePosition % 2 == 0:
        return valuesList[firstQuartilePosition - 1] #I need to do it -1 because lists start on 0
    else:
        oddFirstQuartile = int(firstQuartilePosition) #It was suposed to be rounded to the next value, but lists start on 0
        return valuesList[oddFirstQuartile]
       
myList = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(myList)):
    print(f'{myList[i]} " ---> " {i}')

print(f'\n\nThe median is: {medianCalculator(myList)}')

mean = meanCalculator(myList)
print(f'\nThe mean is: {mean}')

variance = varianceCalculator(myList,mean)
print(f'\nThe variance is: {variance}')

stDev = standardDeviationCalculator(variance)
print(f'\nThe standard deviation is: {stDev}')

cv = coeficientOfVariation(stDev, mean)
print(f'\nThe coeficient of variation is: {cv}')

zScore = zScoreCalculator(3, mean, stDev)
print(f'\nThe Z-Score for "num - 3" is: {zScore}')

firstQuartile = firstQuartileCalculator(myList)
print(f'\nThe Q1 is: {firstQuartile}')