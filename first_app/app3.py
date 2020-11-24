from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)

df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
                       "Patient ID": [123, 456],
                       "Misc Data Point": [8, 53]})

@app.route('/', methods=("POST", "GET"))
def html_table():

    # link_column is the column that I want to add a button to
    return render_template("simple3.html", column_names=df.columns.values, row_data=list(df.values.tolist()),
                            link_column="Patient ID", zip=zip)


if __name__ == '__main__':
    app.run()