import os
import matplotlib.pyplot as plt

def print_menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph\n")
    return input("Enter your selection: ")

def main():
    students = []
    studentIDs = []
    with open("data/students.txt", "r") as file:
        for line in file:
            ID = line[0:3]
            name = line[3:].strip()
            students.append(name)
            studentIDs.append(ID)

    assignmentWeight = []
    assignmentIDs = []
    assignmentNames = []
    with open("data/assignments.txt", "r") as file:
        content = file.read().split("\n")
        content.pop()  # remove last empty line if any
        for i in range(0, len(content), 3):
            name = content[i]
            ID = content[i + 1]
            weight = int(content[i + 2])
            assignmentNames.append(name)
            assignmentIDs.append(ID)
            assignmentWeight.append(weight)

    submissionStudent = []
    submissionAssignment = []
    submissionScore = []
    for filename in os.listdir("data/submissions"):
        with open(f"data/submissions/{filename}", "r") as file:
            content = file.read().split("|")
            submissionStudent.append(content[0])
            submissionAssignment.append(content[1])
            submissionScore.append(content[2])

    option = print_menu()

    if option == "1":
        studentName = input("What is the student's name: ")
        if studentName not in students:
            print("Student not found")
        else:
            studentID = studentIDs[students.index(studentName)]
            total_weight = 0
            weighted_score_sum = 0
            for i in range(len(submissionStudent)):
                if studentID == submissionStudent[i]:
                    assignmentID = submissionAssignment[i]
                    score = float(submissionScore[i])
                    if assignmentID in assignmentIDs:
                        index = assignmentIDs.index(assignmentID)
                        weight = assignmentWeight[index]
                        total_weight += weight
                        weighted_score_sum += score * weight / 100
            final_score = round((weighted_score_sum / total_weight) * 100)
            print(f"{final_score}%")

    elif option == "2":
        assignmentName = input("What is the assignment name: ")
        if assignmentName not in assignmentNames:
            print("Assignment not found")
        else:
            assignmentID = assignmentIDs[assignmentNames.index(assignmentName)]
            scores = []
            for i in range(len(submissionAssignment)):
                if submissionAssignment[i] == assignmentID:
                    scores.append(float(submissionScore[i]))
            if scores:
                print(f"Min: {int(min(scores))}%")
                print(f"Avg: {int(sum(scores) / len(scores))}%")
                print(f"Max: {int(max(scores))}%")

    elif option == "3":
        assignmentName = input("What is the assignment name: ")
        if assignmentName not in assignmentNames:
            print("Assignment not found")
        else:
            assignmentID = assignmentIDs[assignmentNames.index(assignmentName)]
            scores = []
            for i in range(len(submissionAssignment)):
                if submissionAssignment[i] == assignmentID:
                    scores.append(float(submissionScore[i]))
            if scores:
                plt.hist(scores, bins=[0, 25, 50, 75, 100])
                plt.title(f"Histogram for {assignmentName}")
                plt.xlabel("Score Range")
                plt.ylabel("Number of Students")
                plt.show()

if __name__ == "__main__":
    main()
