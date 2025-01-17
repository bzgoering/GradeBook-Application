class Grade:
    totalPoints = 0
    totalCorrect = 0
    #constructor
    #parm: correct questions and total questions
    def __init__(self, correct, total):
         self.correct = correct
         self.total = total
         Grade.totalCorrect = Grade.totalCorrect + correct
         Grade.totalPoints = Grade.totalPoints + self.total
         self.percent = self.calcPercent()
         self.letter = self.calcLetter()

    #calculates letter grade based off percent
    def calcLetter(self):
        if self.percent < 60:
            return 'F'
        elif self.percent < 70:
            return 'D'
        elif self.percent < 80:
            return 'C'
        elif self.percent < 90:
             return 'B'
        elif self.percent < 100:
            return 'A'
        else:
            return ''

    #calculates percent based off user inputs
    def calcPercent(self):
        return self.correct / self.total * 100

#User choices
def printChoice():
    print("\n0. exit")
    print("1. add student")
    print("2. add student's grade")
    print("3. edit student's grade")
    print("4. delete student")
    print("5. delete student's grade")
    return input("Enter your choice: ")

def searchStudent(matrix, student):
    for index, x in enumerate(matrix):
        if x[0] == student:
            return index
    return -1

#display
print("Welcome to your Gradebook/nPlease select an option:")

#variables
gradeBook = []
done = False

# check if user entered a valid entry
while not(done):
    userInput = printChoice()

    if not (userInput == '0' or userInput == '1' or userInput == '2' or userInput == '3' or userInput == '4' or userInput == '5'):
        userInput = printChoice()

    #exit
    if userInput == '0':
        done = True

    #adds student
    elif userInput == '1':
        StudentName = input("Enter the student's name: ")
        gradeBook.append([StudentName])

    #adds student grade
    elif userInput == '2':
        studentName = input("Enter the student's name: ")
        studentIndex = searchStudent(gradeBook, studentName)
        if len(gradeBook) == 0 or studentIndex == -1:
            print("Student Not Found")
        else:
            try:
                correct = int(input("Enter number of correct questions: "))
                total = int(input("Enter total number of questions: "))
                gradeBook[studentIndex] = [Grade(correct, total)]
            except ValueError:
                print("Error - Invalid Input")
