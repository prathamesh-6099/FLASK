from flask import Flask,render_template,request,make_response,session,url_for,redirect
app=Flask(__name__)
app.secret_key="sfdas@#23331"
count=0

@app.route('/get_profile')
def get_profile():
  uname= session.get('uname')
  if uname==None:
    # uname= "Guest"
   return redirect(url_for('login'))
   # Initialize or increment user's session visit count
  session['visit_count'] = session.get('visit_count', 0) + 1
  count = session['visit_count']
  return f"Welcome {uname}, this is your visit number: {count}"

  

@app.route('/login', methods=['POST','GET'])
def login():
   if request.method=='POST':
     session['uname']=request.form.get('username')
     session['visit_count'] = 0
     return render_template('get_profile.html')
   if "uname" in session :
     return """ <h1> U have Already login  <a href="get_profile"> Go to ur profile </a><h1/>"""
     
   return render_template('login.html')

@app.route('/logout')
def logout():
   if "uname" in session:
     session.pop('uname')
     session.pop('visit_count', None)
   return """<h1>U have Sucessfully Log Out , See u Soon..........<a href="/login"> Re-Login</a></h1>"""

if __name__=='__main__':
 app.run(debug=True)