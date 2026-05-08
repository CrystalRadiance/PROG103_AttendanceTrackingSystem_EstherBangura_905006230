# ATTENDANCE TRACKING SYSTEM (ATS)
# PROG103 STRUCTURED PROGRAMMING ASSIGNMENT

attendance_records=[]

def mark_attendance():

    print("\n========== MARK ATTENDANCE ==========")

    name=input("Enter Student Name: ").strip()
    student_id=input("Enter Student ID: ").strip()
    department=input("Enter Department: ").strip()

    while True:

        status=input("Enter Attendance Status (Present/Absent): ").strip().lower()

        if status=="present" or status=="absent":
            break

        else:
            print("Invalid input. Enter Present or Absent.")

    record={
        "name": name,
        "student_id": student_id,
        "department": department,
        "status": status
    }

    attendance_records.append(record)

    print("\nAttendance Recorded Successfully!")

def view_records():

    print("\n========== ATTENDANCE RECORDS ==========")

    if len(attendance_records)==0:
        print("No attendance records found.")
        return

    for index, record in enumerate(attendance_records, start=1):

        print("\n-----------------------------------")
        print(f"Record Number : {index}")
        print(f"Name          : {record['name']}")
        print(f"Student ID    : {record['student_id']}")
        print(f"Department    : {record['department']}")
        print(f"Attendance    : {record['status'].title()}")
        print("-----------------------------------")

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    keyword=input("Enter Student ID: ").strip()

    found=False

    for record in attendance_records:

        if record['student_id']==keyword:

            print("\nStudent Found")
            print("-----------------------------------")
            print(f"Name        : {record['name']}")
            print(f"Department  : {record['department']}")
            print(f"Attendance  : {record['status'].title()}")
            print("-----------------------------------")

            found=True

    if not found:
        print("Student record not found.")

def update_attendance():

    print("\n========== UPDATE ATTENDANCE ==========")

    student_id=input("Enter Student ID to Update: ").strip()

    for record in attendance_records:

        if record['student_id']==student_id:

            while True:

                new_status=input("Enter New Status (Present/Absent): ").strip().lower()

                if new_status=="present" or new_status=="absent":
                    record['status']=new_status
                    break

                else:
                    print("Invalid input.")

            print("\nAttendance Updated Successfully!")
            return

    print("Student record not found.")

def delete_record():

    print("\n========== DELETE RECORD ==========")

    student_id=input("Enter Student ID to Delete: ").strip()

    for record in attendance_records:

        if record['student_id']==student_id:

            attendance_records.remove(record)

            print("\nRecord Deleted Successfully!")
            return

    print("Student record not found.")

def attendance_summary():

    print("\n========== ATTENDANCE SUMMARY ==========")

    if len(attendance_records)==0:
        print("No records available.")
        return

    total_students=len(attendance_records)

    present=0
    absent=0

    for record in attendance_records:

        if record['status']=="present":
            present+=1

        else:
            absent+=1

    print(f"Total Students : {total_students}")
    print(f"Present         : {present}")
    print(f"Absent          : {absent}")

def main():

    while True:

        print("\n================================================")
        print("       ATTENDANCE TRACKING SYSTEM (ATS)")
        print("================================================")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Search Student")
        print("4. Update Attendance")
        print("5. Delete Record")
        print("6. Attendance Summary")
        print("7. Exit System")
        print("================================================")

        choice=input("Enter Your Choice: ")

        if choice=='1':
            mark_attendance()

        elif choice=='2':
            view_records()

        elif choice=='3':
            search_student()

        elif choice=='4':
            update_attendance()

        elif choice=='5':
            delete_record()

        elif choice=='6':
            attendance_summary()

        elif choice=='7':

            print("\n========== FINAL SUMMARY ==========")

            total_students=len(attendance_records)

            present=0
            absent=0

            for record in attendance_records:

                if record['status']=="present":
                    present+=1

                else:
                    absent+=1

            print(f"Total Students : {total_students}")
            print(f"Present         : {present}")
            print(f"Absent          : {absent}")

            print("\nSystem Closed Successfully.")
            print("Thank you for using ATS.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
