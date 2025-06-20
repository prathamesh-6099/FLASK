from flask import Flask,render_template,request
app=Flask(__name__)

# @app.route('/querry')
# def query_demo():
#     return render_template('querry_demo.html')

@app.route('/take_data')
def take_data():
    return render_template('take_data_post.html')

@app.route('/fetch_data',methods=['POST'])
def fetch_data():
  print(request.form)
  return "request form is printed"

if __name__=='__main__':
 app.run(debug=True)