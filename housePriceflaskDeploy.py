from flask import Flask, request, render_template
import json
import pickle

model = pickle.load(open('housePriceMOdel.pkl', "rb"))

app = Flask(__name__)

@app.route('/streamlit_deploy')
def streamlit_deploy():
    return render_template('housePrice.py')


@app.route('/input_form', methods=['GET'])
def input_form():
    return render_template('index.html')


@app.route('/deployer', methods = ['POST', 'GET'])
def deployer():
    lots = float(request.form['LotFrontage'])
    # LotFrontage = float(request.form['LotFrontage'])
    LotArea = float(request.form['LotArea'])
    BsmtUnfSF = float(request.form['BsmtUnfSF'])
    GrLivArea = float(request.form['GrLivArea'])
    MSSubClass = float(request.form['MSSubClass'])
    TotalBsmtSF = float(request.form['TotalBsmtSF'])
    BsmtFinSF1 = float(request.form['BsmtFinSF1'])

    input_variables = [lots, LotArea, BsmtUnfSF, GrLivArea, MSSubClass,
       TotalBsmtSF, BsmtFinSF1]
    
    predicts = model.predict([input_variables])
    outted = round(predicts[0], 2)

    return f'Your Predicted Profit is: {outted}'



if __name__ == "__main__":
    app.run(debug = True)