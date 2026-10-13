from flask import Flask, render_template
import pandas as pd
from pycparser.c_ast import Return

app = Flask("Website")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]
@app.route("/")
def home():
    return render_template("tutorial.html", data = stations.to_html())

@app.route("/Store/")
def store():
    return render_template("store.html")

@app.route("/About/")
def about():
    return render_template("about.html")

@app.route("/Contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/v1/<station>/<date>")
def weatherapi(station, date):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temp": temp
            }

@app.route("/api/v1/<station>")
def weatherapi_all(station):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    return df.to_dict('records')



@app.route("/api/v1/annual/<station>/<year>")
def weatherapi_year(station, year):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    return df[df['    DATE'].str.startswith(str(year))].to_dict('records')


app.run(debug=True)