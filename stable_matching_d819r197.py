import sys


class Person:
    def __init__(self, interests, gen):
        self.gender = gen
        self.engagedTo = None
        self.interestRanking = interests

class PersonPairing:
    def __init__(self,  filePath):
        file = open(filePath, "r")
        fileLines = file.readlines()
        size = int(fileLines[0])
        rowsImported = 0
        gender = "Male"
        interestMatrix = []
        intPersonInterest = []
        for line in fileLines[1:]:
            if line != "" and line != "\n":
                strPersonInterest = line.split(',')
                for interest in strPersonInterest:
                    intPersonInterest.append(int(interest))
                interestMatrix.append(Person(intPersonInterest, gender))
                rowsImported += 1
                intPersonInterest = []
                if rowsImported == size and gender == "Male":
                    self.maleInterestMatrix = interestMatrix
                    interestMatrix = []
                    rowsImported = 0
                    gender = "Female"
                elif rowsImported == size and gender == "Female":
                    self.femaleInterestMatrix = interestMatrix

    def showInterestMatrices(self):
        print("Male Interests: ")
        for male in self.maleInterestMatrix:
            print(male.interestRanking)
        print("\n", end = '')
        print("Female Interests: ")
        for woman in self.femaleInterestMatrix:
            print(woman.interestRanking)

def main():
    personPair = PersonPairing(sys.argv[1])
    personPair.showInterestMatrices()


if __name__ == "__main__":
    main()
