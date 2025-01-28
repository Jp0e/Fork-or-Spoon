# Written by Joshua Fernandez
# Database for Scrumdogs
# Created 1/27/2025


import csv


# The class for our database. 
class Database:
    def __init__(self,file = None)->None:
        # self.file is the only required attribute for this class.
        self.file = file


    # This method allows us to input any list of dictionaries into our Scrumabase. 
    def excel(self, studentlist)->None:
        """ This method will take a list of dictionary items and
        write each dictionary item into a row in a CSV File.
        
        Takes 1 argument. Requires a list of dictionary items.
        """

        file = self.file

        # This bit of code opens the file math in the mode we need as well as the character style encoding.
        with open(file, mode= 'w', newline = '', encoding = 'utf-8') as file:
            # writer is a variable for the csv.DictWriter function that creates a csv file and takes an argument for th file and the fieldnames.
            writer = csv.DictWriter(file, fieldnames= studentlist[0].keys())
            # This is a method from the csv library DictWriter Class.
            writer.writeheader()
            # Method to write multiple rows of dictionary items.
            writer.writerows(studentlist)


    # This bit of code allows to to extract the information from the csv into a list of dictionaries.
    def csv_to_dict(self)-> None:
        """
        This function takes each row in a CSV file and makes dictionaries.

        Does not need to take in any arguments. 
        """
        file = self.file

        with open(file, mode='r', encoding='utf-8') as file:
            # The "DictReader" class automatically uses the Headers of the CSV files as keys.
            csv_reader = csv.DictReader(file)
            data = [dict(row) for row in csv_reader]  # Convert each row into a dictionary
        
        return print(data)



