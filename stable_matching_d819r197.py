import sys

class Person:
    def __init__(self, i, interests, gen):
        self.id = i
        self.gender = gen
        #Initally Set all Men to be Free
        self.engagedTo = None
        self.interestRanking = interests
        self.proposedTo = []

class PersonPairing:
    def __init__(self,  filePath):
        file = open(filePath, "r")
        fileLines = file.readlines()
        self.size = int(fileLines[0])

        rowsImported = 0
        gender = "Male"
        interestMatrix = []
        intPersonInterest = []
        self.freeManQueue = []
        #Iterate through the lines
        for line in fileLines[1:]:
            #Exclude Lines with Nonuseful data
            if line != "" and line != "\n":
                #Split the line into array
                strPersonInterest = line.split(',')
                #Make a list of Interest for each Person
                for interest in strPersonInterest:
                    intPersonInterest.append(int(interest))
                #Make a List of People for a given gender
                interestMatrix.append(Person(rowsImported, intPersonInterest, gender))
                rowsImported += 1
                intPersonInterest = []
                #Bind Interest Matrix to maleInterestMatrix
                if rowsImported == self.size and gender == "Male":
                    self.maleInterestMatrix = interestMatrix
                    interestMatrix = []
                    rowsImported = 0
                    gender = "Female"
                #Bind Interest Matrix to femaleInterestMatrix
                elif rowsImported == self.size and gender == "Female":
                    self.femaleInterestMatrix = interestMatrix
        #Populate the Queue with all Men
        for man in self.maleInterestMatrix:
            self.freeManQueue.append(man)

    def showInterestMatrices(self):
        print("Male Interests: ")
        for male in self.maleInterestMatrix:
            print(male.interestRanking)
        print("\n", end = '')
        print("Female Interests: ")
        for woman in self.femaleInterestMatrix:
            print(woman.interestRanking)

    def showPairs(self):
        print("Resulting Pairs of Couples: ")
        print("[", end = '')
        for male in self.maleInterestMatrix:
            if male.engagedTo != None:
                print("(" + str(male.id) + "," + str(male.engagedTo.id) + ") ", end = '')
            else:
                print("(Male " + str(male.id) +" is not engaged to anyone)")
        print("]")

    def stableMatch(self):
        #While there is a free man who hasnt propose to everyone
        while(len(self.freeManQueue) != 0):
            #Choose Such a Man
            man = self.freeManQueue.pop(0)
            print("Running with Man: " + str(man.id))
            if man.engagedTo == None and len(man.proposedTo) != self.size:
                #Let W be the highest ranked woman for the given man in mans preference list to whom he hasnt proposed
                for interest in man.interestRanking:
                    #Define current woman
                    woman = self.femaleInterestMatrix.pop(interest)
                    self.femaleInterestMatrix.insert(interest, woman)
                    #W is free for marriage
                    if man.proposedTo == [] or woman not in man.proposedTo:
                        #W is not currently Engaged
                        if woman.engagedTo == None:
                            #Engage the Man and Woman
                            man.engagedTo = woman
                            #Add woman to list of proposed woman for the given man
                            man.proposedTo.append(woman)
                        #W is currently engaged to M'
                        else:
                            #W prefers M' to M
                            if interest.interestRanking.index(man) < interest.interestRanking.index(interest.engagedTo):
                                #Then Push M back on to the queue
                                self.freeManQueue.append(man)
                            #W prefers M to M'
                            else:
                                notM = interest.engagedTo
                                #M and W become engaged
                                man.engagedTo = interest
                                #M' is Pushed back on Queue
                                self.freeManQueue.append(notM)


def main():
    personPair = PersonPairing(sys.argv[1])
    personPair.showInterestMatrices()
    personPair.stableMatch()
    #personPair.showPairs()

if __name__ == "__main__":
    main()
