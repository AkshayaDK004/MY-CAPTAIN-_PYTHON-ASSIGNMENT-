
import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact","Department","Emai","District"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    student_num=1
    while (condition==True):
        student_info=input("Enter the student info for {} as(Name age contact Dept email district)".format(student_num))
        student_info_list=student_info.split(" ")
        print("Entered information is Name:{}\nAge:{}\nContact:{}\nDepartment:{}\nEmail:{}\nDistrict:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4],student_info_list[5]))
        choice_check=input("Is the enterted information correct(yes/no)\n")
        if choice_check=="yes":
            write_into_csv(student_info_list)
            condition_check=input("Enter(yes/no) if u want to enter the information of another student")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("Please re-enter the values!")
