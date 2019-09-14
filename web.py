from flask import Flask,render_template,redirect,request,url_for
from attraction_list import filter_region,filtering,filtered_name
from models.db import db

app=Flask(__name__)
@app.route("/")
def home_1():
    return render_template("home.html")
@app.route("/",methods=['POST'])
def home():
    region1=request.form['radio']

    data1=filter_region(region1)
    session['data1'] = data1
    return redirect(url_for('.filtering2', data1 = data1))

@app.route('/filter_output')
def filtering2():
    data1 = request.args['data1']
    data1= session['data1']
    return render_template('screen3.html')
@app.route('/detail/<places>')
def details(places):
    data=filtered_name(places)
    return render_template('screen4.html',data=data)



@app.route('/filter_output',methods=['POST'])
def filtering1():
    season = request.form.get('season')
    region = request.form.get('region')
    geography = request.form.get('geography')
    data = filtering(season, region, geography)
    return render_template('index.html', data = data )
    
   

if __name__=="__main__":
    app.run()