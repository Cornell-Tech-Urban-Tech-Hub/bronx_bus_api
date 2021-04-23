import os
import json
import sys
import csv

from flask import Flask
    
app = Flask(__name__)

datadir='/csv/'
datapath=os.getcwd()+datadir

def csv_to_json(table_name):

    data = dict()
    with open(datapath+table_name+'.csv') as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter='\t')
        for n, row in enumerate(csvReader):
            data[str(n)] = row

    container = {'table_name':table_name,
                 'table_data': data

    }

    return json.dumps(container, indent=4)



# route that allows us to read a date from the URL
@app.route('/table/<table_name>')
def table(table_name):
    return csv_to_json(table_name)

if __name__ == '__main__':
    app.run(debug=True)