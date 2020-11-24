from flask import Flask, render_template 
import pandas as pd

app = Flask (__name__)

@ app.route ('/')
def index ():
    df = pd.DataFrame ({'key': ['A', 'B', 'C', 'D', 'E', 'F'],
                       'val': [0.09,0.1,0.8,0.2,0.7,0.1]})
    return render_template("simple.html", table = df.to_html (header = 'true'))

if __name__ == '__main__':
    app.run ()