from flask import Flask,render_template
app=Flask(__name__)

@app.route('/querry')
def query_demo():
    return render_template('querry_demo.html')

@app.route('/take_data')
def take_data():
    return render_template('take_data.html')

if __name__=='__main__':
 app.run(debug=True)