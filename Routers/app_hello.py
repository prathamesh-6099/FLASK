from flask import Flask,render_template, redirect, url_for

app=Flask(__name__)

@app.route('/home',methods=["post",'get'])
def home():
 return render_template('home.html', curl_now="hello")

@app.route('/home_again')
def home_again():
   return redirect(url_for('home'))

@app.route('/search')
def search():
  return redirect("https://www.bing.com/")

@app.route('/details')
def view():
  return render_template('details.html')
if __name__=="__main__":
 app.run(debug=True)