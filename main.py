students = []
def add_students(stu_id, name, grade):
    student_details = {
           'ID' : stu_id,
           'Name': name,
           'Grade': grade
       }
    students.append(student_details)
    print("Next------>")


n = int(input("enter the number of students: "))

for i in range(n):
    while True:
        stu_id = int(input("Enter Student Id: "))
        duplicate = False

        for boys in students:
            if boys['ID'] == stu_id:
                print(f"Student ID {stu_id} already exists")
                duplicate = True
                break
        if not duplicate:
             name = input("Enter student name: ")
             grade = input("Enter student Grade: ")

             add_students(stu_id, name, grade)
             break


print("ID            Name          Grade")
for i in students:
    print(f"{i['ID']}          {i['Name']}               {i['Grade']}")