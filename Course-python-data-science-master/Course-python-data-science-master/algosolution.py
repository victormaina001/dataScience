"""Let say you are a teacher and you have different student
records containing id of a student and the marks list in each subject
where different students have taken different number of subjects. All
these records are in hard copy. You want to enter all the data in computer
and want to compute the average marks of each student and display"""

def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        marksList = input("Enter the marks by comma separted values: ")
        moreStudents = input('Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, "is already insterted")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D
        

studentData = getDataFromUser()

def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks


avgM = getAvgMarks(studentData)

avgM


for x in avgM:
    print("Student :",x,"got avg Marks as: ",avgM[x])

