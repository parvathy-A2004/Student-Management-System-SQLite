import csv
import sqlite3


connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id integer primary key,name text not null,course text not null)""")
connection.commit()
def create_student():
        try:
            student_id = int(input("Enter student id"))
        except ValueError:
            print("Enter valid input")
            return
        
            
        name = input("Enter student name")
        course = input("Enter course")

        try:
             cursor.execute(
                  "INSERT INTO students VALUES(? ,?, ?)",
                  (student_id, name, course)
             )
             connection.commit()
             print("Student added successfully")
        except sqlite3.IntegrityError:
            print("Duplicate student id")
        

def search_student():
    try:
        st_id = int(input("Enter student id"))
    except ValueError:
        print("Enter valid input")
        return

    cursor.execute("SELECT * FROM students WHERE student_id = ?",
                   (st_id ,)
                   )
    record = cursor.fetchone()
    if record:
        print("ID: ",record[0])
        print("Name: ",record[1])
        print("Course: ",record[2])
    else:
        print("Student not found")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name: ",name)
            print("Course: ",course)
    else:
        print("No student records")

def delete_student():
    try:
        stu_id = int(input("Enter student id"))
    except ValueError:
        print("Enter valid input")
        return
            
    cursor.execute("DELETE FROM students WHERE student_id = ?",
    (stu_id, )
    )
    
    if cursor.rowcount > 0:
            connection.commit()
            print("Deleted successfully")
                    
    else:
            print("No student in this id")

def update_student(): 
    try:
        stu_id = int(input("Enter student id"))
    except ValueError:
        print("Enter valid input")
        return
    
    try:
        new_id = int(input("Enter new student id"))
    except ValueError:
        print("Enter valid input")
        return
    
    cursor.execute("SELECT * FROM students WHERE student_id = ?",
                   (new_id, )
                   )
    if cursor.fetchone() and stu_id != new_id:
        print("ID already exist")
        return

    new_name = input("Enter new student name")
    new_course = input("Enter new course")
    cursor.execute("UPDATE students SET student_id = ?, name = ?, course = ? WHERE student_id = ?", 
                   (new_id, new_name, new_course, stu_id,)
                   )
    if cursor.rowcount > 0:
        connection.commit()
        print("Updated successfully")
    else:
        print("No student in this id")


                   
def count_students():
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    print("total student: ",count)
   

def count_students_by_course():
    stu_course = input("Enter course")
    cursor.execute("SELECT COUNT(*) FROM students WHERE course = ?",
                   (stu_course, ))
    count = cursor.fetchone()[0]
    if count > 0:
        print(f"Total number of students in {stu_course}:{count}")
    else:
        print(f"No student found in {stu_course}")

def search_by_name():
    stu_name = input("Enter student name")
    cursor.execute("SELECT * FROM students WHERE name = ? COLLATE NOCASE",
                   (stu_name, )
                   )
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name :",name)
            print("course: ",course)
            print()
    else:
        print("NO student found in this name")


def search_by_course():
    stu_course = input("Enter course ")
    cursor.execute("SELECT * FROM students WHERE course = ? COLLATE NOCASE",
                   (stu_course,)
                   )
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name: ",name)
            print("Course: ",course)
            print()
    else:
        print("No student found in this course")
    

def sort_by_id():
    
    cursor.execute("SELECT * FROM students ORDER BY student_id")
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("Id: ",student_id)
            print("Name: ",name)
            print("Course: ",course)
            print()
    else:
        print("No students")

def sort_by_name():
    cursor.execute("SELECT * FROM students ORDER BY name")
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name: ",name)
            print("Course: ",course)
            print()
    else:
        print("No students")

def sort_by_course():
    cursor.execute("SELECT * FROM students ORDER BY course")
    records = cursor.fetchall()
    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name: ",name)
            print("Course: ",course)
            print()
    else:
        print("No students")

def delete_student_by_name():
    stu_name = input("Enter student name")
    cursor.execute("DELETE FROM students WHERE name = ? COLLATE NOCASE",
                   (stu_name,)
                   )
    if cursor.rowcount > 0:
        connection.commit()
        print("Student(s) deleted successfully")
    
    else:
        print("No student found in this name")

def update_course():
    try:
        stu_id = int(input("Enter student id"))
    except ValueError:
        print("Enter valid input")
        return
    new_course = input("Enter new course")
    cursor.execute("UPDATE students SET course = ? WHERE Student_id = ?",
                   (new_course, stu_id, ))
    if cursor.rowcount > 0:
        connection.commit()
        print("Course updated successfully")

    else:
        print("No students found in this id")

def display_student_by_course():
    stu_course = input("Enter course")
    cursor.execute("SELECT * FROM students WHERE course = ? COLLATE NOCASE",
                    (stu_course, )
                    )
    records = cursor.fetchall()

    if records:
        for student_id, name, course in records:
            print("ID: ",student_id)
            print("Name: ",name)
            print("Course: ",course) 
            print()

    else:
        print("No student")

def course_wise_count(): 
    cursor.execute("SELECT course, COUNT(*) FROM students GROUP BY course ORDER BY course")
    records = cursor.fetchall()
    if records:
        for course,count in records:
            print(course,":",count)
    
    else:
        print("No students")


def save_to_file():
    cursor.execute("SELECT student_id, name, course FROM students")
    records = cursor.fetchall()
    if records:
        
        with open("stu_data.txt","w") as file:
            for student_id, name, course in records:
                file.write(f"{student_id},{name},{course}\n")
        print("Data saved successfully")
    else:
        print("No students found")
    
def load_from_file():
        try:
            cursor.execute("SELECT student_id FROM students")
            ids = set(row[0] for row in cursor.fetchall())
            with open("stu_data.txt","r") as file:
                
                for line in file:

                   
                    data = line.strip().split(",")
                    student_id = int(data[0])
                    if student_id not in ids:
                        cursor.execute("INSERT INTO students VALUES(?, ?, ?)",
                                    (student_id, data[1], data[2], )
                                    )
                        ids.add(student_id)
            connection.commit()
            print("Data loaded successfully")
        except FileNotFoundError:
            print("File not found")
    
def export_csv():
    cursor.execute("SELECT student_id, name, course FROM students")
    records = cursor.fetchall()
    if records:
    
        with open("students.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","NAME","COURSE"])
                
                
            for record in records:
                writer.writerow(record)
        print("Data exported successfully")
    else:
         print("No records found")

def import_csv():
    try:
        with open("students.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            cursor.execute("SELECT student_id FROM students")
            ids = cursor.fetchall()
            count = 0
        
            for student_id, name, course in reader:
                found = False
                for id in ids:
                    
                    if id[0] == int(student_id):
                        found = True
                        break
                if not found:
                    student_id = int(student_id)
                    cursor.execute("INSERT INTO students VALUES(?, ?, ?)",
                                (student_id, name, course, )
                                )
                    ids.append((student_id, ))
                    count += 1
            connection.commit()
            print(f"{count} student(s) imported successfully")
    except FileNotFoundError:
        print("File not found")
                
            
                

if __name__=="__main__":
    while True:
        print("1.Create student")
        print("2.View students")
        print("3.Search student")
        print("4.Delete student")
        print("5.Update student")
        print("6.Count Students")
        print("7.Count students by course")
        print("8.Search student by name")
        print("9.Search student by course")
        print("10.Sort by id")
        print("11.Sort by name")
        print("12.Sort by course")
        print("13.Delete student by name")
        print("14.Update course")
        print("15.Display student by course")
        print("16.Course wise count")
        print("17.Save to file")
        print("18.Load from file")
        print("19.Export to csv")
        print("20.Import from csv")
        print("21.Exit")
        try:
            choice = int(input("Enter your choice"))
        except ValueError:
            print("enter valid choice")
            continue

        if choice == 1:
            create_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            update_student()

        elif choice == 6:
            count_students()
        
        elif choice == 7:
            count_students_by_course()

        elif choice == 8:
            search_by_name()

        elif choice == 9:
            search_by_course()

        elif choice == 10:
            sort_by_id()
        
        elif choice ==11:
            sort_by_name()

        elif choice == 12:
            sort_by_course()

        elif choice == 13:
            delete_student_by_name()

        elif choice == 14:
            update_course()

        elif choice == 15:
            display_student_by_course()  

        elif choice == 16:
            course_wise_count()

        elif choice == 17:
            save_to_file()

        elif choice == 18:
            load_from_file()

        elif choice == 19:
            export_csv()

        elif choice == 20:
            import_csv()

        elif choice == 21:
            print("program ends")
            break

        else:
            print("invalid choice")
    
    connection.close()
