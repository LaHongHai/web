from flask import Flask,render_template,redirect,request,url_for
from attraction_list import filter_region,filtering,filtered_name
from models.db import db

app=Flask(__name__)
@app.route("/")
def home_1():
    return render_template("home.html")
@app.route("/",methods=['POST'])
def home():
    region1=request.form.get('radio')

    
    return redirect('/filter_output/{0}'.format(region1))



@app.route('/filter_output/<place>')
def filtering2(place):
    data1=filter_region(place)
    # data1 = request.args['data1']
    # data1= session['data1']


    return render_template('screen3.html',data=data1)
@app.route('/details/<places>')
def details(places):

    data1=filtered_name(places)
    data2=data1[0]

    return render_template('screen4.html',data=data2)
@app.route('/iframe/<places>')
def iframe_detail(places):
    data1=filtered_name(places)
    data2=data1[0]
    return render_template('smallscreen4.html',data=data2)



@app.route('/filter_output/<place>',methods=['POST'])
def filtering1(place):
    season = request.form.get('season')
    region = request.form.get('region')
    geography = request.form.get('geography')
    data = filtering(region, season, geography)

    return render_template("screen3.html",data=data)
    
   

if __name__=="__main__":
    app.run(debug=True)