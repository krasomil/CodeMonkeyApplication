import csv
import sys
import logging
import random

class DatabaseHandler():
    """
        Database handler class

        Raises -- sys.exit if the database .csv is not found
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.data = self.populate_database_from_file("../database/QuestionDB.csv")
        
    def populate_database_from_file(self, file_path="../database/QuestionDB.csv"):
        """
        Get the data from the csv and put it in the database

        Keyword Args:
          file_path path to the csv file
        """
        data = []
        try:
            # open the file
            with open(file_path) as file:
                # read the file
                reader = csv.reader(file, delimiter=',')
                # parse the row
                for row in reader: 
                    try:
                        # append the array
                        data.append({ "question": row[0], "correct": row[1], "incorrect": row[2].split(','), "color": row[3] })
                    except Exception:
                        self.logger.error("Error parsing row: {0}".format(row))
        except FileNotFoundError:
            # no point in having a game with no questions
            sys.exit()
        return data

    def select_color_question(self, color):
        """
        select a question from a particular color group

        Keyword Args:
          color - the color to select

        Return - the selected question
        """
        filtered_questions = [question for question in self.data if question ['color'] in color]
        return filtered_questions[random.randint(0, len(filtered_questions) - 1)]

    
