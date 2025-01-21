# Written by Joshua Fernandez
# Database for Scrumdogs
# Created 1/16/2025

import os
import Database
import csv
import pandas


# I am going to be creating a dictionary class

class Student_info:
    def __init__(self, name, speed, signs_seen):
        self.name = name
        self.speed = speed
        self.signs = signs_seen
        
Cadee = Student_info(name = 'Cadee', speed = 'speed', signs_seen=5)

def student_data(student):
    dicttest = {
        'name' : f'{student.name}',
        'speed' : f'{student.speed}',
        'signs seen' : f'{student.signs}'
    }
    

student_data(Cadee)


def dict_to_CSV(student,filename, csv_headers):

    data = []
    result = student_data(student)
    data.append(result)
    # with open(filename, encoding= 'utf-8') as strings:
    #     studentsdata = csv.reader(strings, delimiter = ',')
    #     next(studentsdata)
    #     for row in studentsdata:
    #         mylist.append(row)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)  # Write headers
        writer.writerows(data)       # Write the rows of data

filename = 'ScrumDatabase.csv'
csv_headers = ['name', 'speed', 'signs seen']
student = Cadee

dict_to_CSV(student, filename, csv_headers)

            

        

    
    





