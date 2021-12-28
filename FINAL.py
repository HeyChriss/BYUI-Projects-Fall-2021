#I called the libraires here 
import json
import random

def main ():
#These are the options where the user will be able to choose 
    print ('Choose the correct decision: ')
    print ('Enter 1 to add a person in the system')
    print ('Enter 2 to look for a person in the system ')
    print ('Enter 3 to show students in the system  ')
    print ('Enter 4 to exit the program. ')
    decision = int(input('What would you like to do? '))
    for decision in range(0,4,1):
        if decision == 1:
            append_new_student()
        elif decision == 2:
            look_for_student()
        elif decision == 3:
            print_list()
        elif decision == 4:
            print ('Thank you for using the program! ') 

#This function helps to read the json document located in the computer.
#WHen I opened in my computer the program ran correctly, we just have to make sure 
#the path is the correct and it must be located in the same project
#the path is path = 'c:\Users\USUARIO\Desktop\Fall Semester\Programming with funtions\Project\student.json' so a new 
#variable must be called path to openstudents = read_students(path), otherwise the program will not find the document and the error will show up. 
def read_students(filename):
    try:    
        file = open(filename)
        read_file = file.read()
        file.close()
        json_object = json.loads(read_file)
        return json_object
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.") 
    except (KeyError) as error:
        print(error)
        print(f"Error: line is formatted incorrectly.") 

#This funciton looks for a student. First the readstudents file opens the file and then and the user can 
#type the I number, the if statement looks for the asnwer in the file and shows the name or if theres not a student with that i number 
def look_for_student():

    try:
        students = read_students("student.json") 
        i_numbers = students['I-number']
        length = len(i_numbers)-1
        random_index = random.randint(0,length)
        Answer = students["I-number"][random_index]
        Answer = input('Please enter an I-Number: ')
        Name = students['names']
        if Answer in i_numbers: 
            index = i_numbers.index(Answer)
            print(Name[index])
        else:
            print('No such student')
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.") 
    except (KeyError) as error:
        print(error)
        print(f"Error: line is formatted incorrectly.") 


#This fucntion adds a person in the file. A ramdom I numnber is assigned and the system will ask for a name. 
#BOth of them pass to a string and they are saved in the file using the file write command. 
def append_new_student ():
    try:
        name = input('What is the name of the student? ')
        students = read_students("student.json")
        i_number = random.randint(111111111,999999999)
        i_number = str(i_number)
        i_numbers = students['I-number']
        Name = students['names']
        Name.append(name)
        i_numbers.append(i_number)
        with open("student.json", "w") as file:
            board_json = {}
            board_json['I-number'] = i_numbers
            board_json['names'] = Name
            updated = json.dumps(board_json)
            file.write(updated)
        print ('The Name was successfully saved. ')
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.") 
    except (KeyError) as error:
        print(error)
        print(f"Error: line is formatted incorrectly.") 

#this function prints the file inlcuding the names and i numbers added in the list. 
def print_list ():
    try:   
        students = read_students("student.json")
        i_numbers = students['I-number']
        Name = students['names']
        length = len(i_numbers)
        for x in range(0,length,1):
            print(Name[x], i_numbers[x])
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.") 
    except (KeyError) as error:
        print(error)
        print(f"Error: line is formatted incorrectly.") 


main()
    