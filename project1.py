import sys
import string
import re


regex =  '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[net]$' 
def emailanalyzer():
    def info():
        global classinfo
        global Section
        global Semester
        global written
        global Instructor
        classinfo = "Project 1 for CS 341"
        Section = "Section number: 006"
        Semester = "Semester: Spring 2021"
        written = "Written by Bishoy Kamel, BK274"
        Instructor = ""

    def question():

        
        global Γ
        global triangle
        global  Φ
        Γ = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        triangle = ['.']
        Φ = ['@']
        Σ = Γ.union(triangle, Φ)
        
        s1 = [Γ, Γ]
        s2 = [triangle,Γ, Γ]
        s3 = ['.net']
        
        L1 = [s1,Φ,s1,s3]
        l1 =  '^[a-z0-9]+[@]\w+[a-z0-9]+[.net]$'

        
        L2 = [s1,s2,Φ,s1,s2,s3]
        l2 =  '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[net]$' 

        #L = L1.union(L2)
        
        fact = True
        state = "q0"
        while fact:
            input1 = str(input(f'Would you like to enter a string? please enter  “y” for “yes”, or “n” for “no”\n'))
            print("")
            if input1 == "n":
                quit()
            elif input1 == "y":
                string1 = str(input(f' Please enter a string over Σ: \n'))

                if(re.search(l1,string1)):  
                    print("Valid Email")
                    print ("Current State: ", state)
                    print ("This input is L1\n")
                    
    

                else:  
                    print("Invalid Email")  
                














             
            elif input1 != "y":
                print('enter again')
        


        

        

    info()
    print(classinfo)
    print (Section)
    print (Semester)
    print (written)
    print (Instructor)
    question()

emailanalyzer()

