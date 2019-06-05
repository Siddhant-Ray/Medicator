from flask import Flask, redirect , url_for, request, session, render_template
import json
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Oh So Secret'

@app.route('/')
def launcher():
    return render_template('login.html')


#Login System using Aadhar UID
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        uid = request.form['uid']
        session['uid'] = uid # Add UID to Session Variable List 
        return redirect(url_for('input'))
    else:
        uid = request.args.get('uid')
        session['uid'] = uid
        return redirect(url_for('input'))

@app.route('/success/<uID>')
def success(uID):
    return ("Registered UID : %s" % uID)

# Data Collector Node
@app.route('/input')
def input():
    return render_template('maintest.html')

@app.route('/data_tx', methods = ['POST', 'GET'])
def data_tx():
    if request.method == 'POST':
        c=request.form['btn']
        print(c)
        temp= c.split(",")
        d=[]
        for i in temp:
            d.append(i)
        #print(type(temp))
        #print(temp)
        #session['btn'] = uid # Add UID to Session Variable List

        
        diseases_set=pd.read_csv('test1.csv')

        dict={'Fever':0,'Cough':1,'Runny nose':2,'Headache':3,'Breathlessness':4,'Diarrhea':5,'Abdominal pain':6,'Vomiting':7,'Nosebleed':8,'Dizziness':9,'Insomnia':10,'Eye swelling':11,'Redness in eye':12,'Nausea':13,'Sweating':14,'Fatigue':15,'Joint pain':16} 

        dict1={'Influenza':['Relenza','After Breakfast 0 After Dinner'],'Swine Flu':['Symmetrel','After Breakfast After Lunch After Dinner'],'Cholera':['Ciprofloxacin','After Breakfast 0 After Dinner'],'Typhoid':['Azithromycin','After Breakfast After Lunch After Dinner'],'Sunstroke':['After Breakfastarbiturates','0 0 After Dinner'],'Common cold':['Ibuprufen','After Breakfast 0 After Dinner'],'Whooping Cough':['Erthromycin','After Breakfast 0 After Dinner'],'Gastroentritis':['Gelusil','After Breakfast 0 After Dinner'],'Conjunctivitus':['Romycin','After Breakfast 0 After Dinner'],'Dehydration':['ORS','After Breakfast After Lunch After Dinner'],'Asthama':['Terbutaline','After Breakfast After Lunch After Dinner'],'Cardiac arrest':['Adrenaline','After Breakfast 0 After Dinner'],'Malaria':['Doxycyline','B After Lunch After Dinner'],'Anaemia':['Hydroxyurea','After Breakfast 0 After Dinner'],'Pneumonia':['Ibuprofen','After Breakfast 0 After Dinner'],'Arthritis':['Lubrijoint 750','After Breakfast 0 After Dinner'],'Depression':['Sleeping Pills','After Breakfast After Lunch After Dinner'],'Food poisoning':['Norflox','After Breakfast 0 After Dinner'],'Migraine':['Crocin','After Breakfast 0 After Dinner'],'Insomnia':['Sleeping Pills','After Breakfast 0 After Dinner']}

        sim_list=[]

        inp= d

        if len(inp)<2:
            return str("Not enough symptoms to predict accuractely")

        #print(inp) ##### Input from the flask form part
        for i in range(0,17):
            sim_list.append(0);

        for i in range(len(inp)):
            key=dict.get(inp[i]);
            sim_list[key]=1;


        def similarity_score(a,b):
            sim=0
            for i in range(len(a)):
                sim=sim+a[i]*b[i]
            return sim

        similar=0
        temp1=0
        index=0
        a1=""
        for i in range(0,20): 
            a=[]
            for j in diseases_set.iloc[i]:
                a.append(j)
            similar=similarity_score(a[1:],sim_list)
            if(similar>temp1):
                a1=a[0]
                
                index=i
                temp1=similar
                



            
        #print(a1)      
        #print(index)
        #print(temp) 
        g=open("disease.txt","a+")
        #f=e.read()
        g.write(a1+"    ")
        g.close()
    
        a2=dict1.get(a1)
        
        a4=a2[0]
        a5=a2[1]
        print(a2)

 
        final="Probable disease:"+a1+"    "+"Medecine required:"+a4;

        return render_template("result.html",dis_name=a1,med_name=a4,dosage_times=a5)

    else:
        dat = request.args.get('btn')
        #session['uid'] = uid
        return redirect(url_for('input'))

if __name__=='__main__':
    app.run(debug=True)
