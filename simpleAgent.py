import random
import sys


class Environment(object):
    def __init__(self):
        # create inital values for location and clean status
        # there are only two locations: A and B
        # 0 = clean, 1 = dirty
        self.locationCondition = {'A': '0', 'B': '0'}

        # randomize the conditions for each location
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)

        print(self.locationCondition)

        if(self.locationCondition['A'] == 0 and self.locationCondition['B'] == 0):
            print("Both Rooms are clean, so no need to vacuum.")
            print("Ending program")
            sys.exit()
        elif(self.locationCondition['A'] == 0 and self.locationCondition['B'] == 1):
            print("Room A is clean, but Room B is dirty so it needs to be cleaned.")
        elif(self.locationCondition['A'] == 1 and self.locationCondition['B'] == 0):
            print("Room A is dirty, but Room B is clean so it needs to be cleaned.")
        elif(self.locationCondition['A'] == 1 and self.locationCondition['B'] == 1):
            print("Both Rooms are dirty and need to be cleaned.")
        else:
            print("There was an error initializing the rooms status")
            print("Ending program")
            sys.exit()


class SimpleReflexAgent(Environment):

    def __init__(self, Environment):

        # instantiate performance measurement
        # pMeasure = 0
        # place the vacuum at a random location
        # 0 = location A, 1 = location B
        initVacuumLocation = random.randint(0, 1)
        currentVacuumLocation = initVacuumLocation

        if(initVacuumLocation == 0):
            print("The vacuum is starting in Room A")
        else:
            print("The vacuum is starting in Room B")

        if(Environment.locationCondition['A'] == 0 and
           Environment.locationCondition['B'] == 1 and
           currentVacuumLocation == 0):
            # move to room B and clean then exit
            print("Moving the vacuum from Room A to B")
            currentVacuumLocation = 1
            print("The vacuum is now in Room B")
            print("NOW CLEANING Room B")
            Environment.locationCondition['B'] = 0
            print("Room B is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        elif(Environment.locationCondition['A'] == 0 and
             Environment.locationCondition['B'] == 1 and
             currentVacuumLocation == 1):
           # clean room B then exit
            print("NOW CLEANING Room B")
            Environment.locationCondition['B'] = 0
            print("Room B is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        elif(Environment.locationCondition['A'] == 1 and
             Environment.locationCondition['B'] == 0 and
             currentVacuumLocation == 0):
           # clean room A then exit
            print("NOW CLEANING Room A")
            Environment.locationCondition['A'] = 0
            print("Room A is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        elif(Environment.locationCondition['A'] == 1 and
             Environment.locationCondition['B'] == 0 and
             currentVacuumLocation == 1):
           # move to room A and clean then exit
            print("Moving the vacuum from Room B to A")
            currentVacuumLocation = 1
            print("The vacuum is now in Room A")
            print("NOW CLEANING Room A")
            Environment.locationCondition['A'] = 0
            print("Room A is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        elif(Environment.locationCondition['A'] == 1 and
             Environment.locationCondition['B'] == 1 and
             currentVacuumLocation == 0):
           # clean room A then move to room b and clean then exit
            print("NOW CLEANING Room A")
            Environment.locationCondition['A'] = 0
            print("Room A is now clean")
            print("Moving the vacuum from Room A to B")
            currentVacuumLocation = 1
            print("The vacuum is now in Room B")
            print("NOW CLEANING Room B")
            Environment.locationCondition['B'] = 0
            print("Room B is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        elif(Environment.locationCondition['A'] == 1 and
             Environment.locationCondition['B'] == 1 and
             currentVacuumLocation == 1):
           # clean room B and move to room A and clean then exit
            print("NOW CLEANING Room B")
            Environment.locationCondition['B'] = 0
            print("Room B is now clean")
            print("Moving the vacuum from Room B to A")
            currentVacuumLocation = 0
            print("The vacuum is now in Room A")
            print("NOW CLEANING Room A")
            Environment.locationCondition['A'] = 0
            print("Room A is now clean")
            print("The status of the rooms are now:")
            print(Environment.locationCondition)
            print("Ending the program")
            sys.exit()
        else:
            print("There was an error when cleaning the rooms")
            print("Ending the program")
            sys.exit()


vacuumEnvironment = Environment()
vacuumAgent = SimpleReflexAgent(vacuumEnvironment)
