import os
import pandas as pd

from flask import Flask
    
app = Flask(__name__)

datadir='/csv/'
datapath=os.getcwd()+datadir

def csv_to_json(table_name):
    df = pd.read_csv(datapath+'test.csv', delimiter='\t')

    # we could also just inject dataframes directly here by using a function factory (e.g. pass the name of the dataframe you want)
    return df.to_json(orient='records')

# route that allows us to read a date from the URL
@app.route('/table/<table_name>')
def table(table_name):
    return csv_to_json(table_name)

if __name__ == '__main__':
    app.run(debug=True)