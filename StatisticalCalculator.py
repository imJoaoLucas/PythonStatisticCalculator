#Joao Classio   #10/29/2025     #statisticalCalculator
'''
I build this program during my statistical classes in order to practice both python
and statistics. It might receive some updates in the future.
'''
import math

userEntryList = [] 

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

displayMenu()
