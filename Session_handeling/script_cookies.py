from flask import Flask,render_template,request,make_response
app=Flask(__name__)

@app.route('/get_profile')
def get_profile():
   name=request.cookies.get('userId')
   if name==None:
      name="guest"
   return f"Welcome {name}"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
       res=make_response(render_template('get_profile.html'))
       res.set_cookie("userId",request.form.get('username'))
       return res
       
    return render_template('login.html')

@app.route('/logout')
def logout():
   res=make_response(render_template('get_profile.html'))
   res.delete_cookie('userId')
   return res

if __name__=='__main__':
 app.run(debug=True)