import json
import operator

class Prioritizer:
    def prioritize(self, path):
        with open("result.json", "r") as json_file:
            list_of_books = json.load(json_file)
            list_of_books.sort(key=lambda x: (x['format'], x['size']), reverse=True)
            output_file = open('sorted_json_file.json', 'w')
            json.dump(list_of_books, output_file)
            
           
            