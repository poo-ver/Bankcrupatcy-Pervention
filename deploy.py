from flask import Flask ,render_template, request
import pickle

app = Flask(__name__)
#load the model
model= pickle.load(open('bankruptcydata.sav','rb'))
@app.route('/')

def home():
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])

def predict():
    industrial_risk=float(request.form['industrial_risk'])
    management_risk=float(request.form['management_risk'])
    financial_flexibility=float(request.form['financial_flexibility'])
    credibility=float(request.form['credibility'])
    competitiveness=float(request.form['competitiveness'])
    operating_risk=float(request.form['operating_risk'])
    result = model.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
    return render_template('index.html',**locals())



if __name__=='__main__':
    
    app.run(debug=True)