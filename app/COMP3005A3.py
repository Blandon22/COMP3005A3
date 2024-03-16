import os
import psycopg2
from CRUD import *

#Prints all the choices the user has and returns their selection
def menu():
    while True:
        #Prints all options
        print("0: Exit Program")
        print("1: Create new Student")
        print("2: See all Student")
        print("3: Update a Student")
        print("4: Delete a Student")


        #Takes in input and validates it
        choice = int(input("Please select an option: "))
        if choice < 0 or choice > 4:
            print("\nInvalid input. Please enter a number between 0 and 4.\n ")
        else:
            return choice
    
#Calls the appropriate CRUD function based on the user's choice
def executeChoice(choice,cur):
    match(choice):
        case 0:
            print("Connection Closed")
        case 1:
            addStudent(cur)
        case 2:
            getAllStudents(cur)
        case 3:
            updateStudentEmail(cur)
        case 4:
            deleteStudent(cur)
            
#Main Control Flow. Repeatedly prints the menu for user to choose an option from.
def main():
    database_url= "postgresql://pythonApp:py123@localhost:5432/A3"
    #Attempts to connect to database
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        print("Connected to database")
        
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

    #Control Flow, prints the seleciton menu and commits changes to the database 
    choice=-1
    while choice!=0:
        choice = menu()
        executeChoice(choice,cur)
        conn.commit()
    cur.close()
    conn.close()
    
main()


