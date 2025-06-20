from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mycollege.db'


db=SQLAlchemy(app)

class student(db.Model):
          def __init__(self,name,addr,city,pin):
              self.name=name
              self.addr=addr
              self.city=city
              self.pin=pin

          id = db.Column('student_id', db.Integer, primary_key=True)
          name = db.Column(db.String(50))    # Fixed: db.string → db.String
          addr = db.Column(db.String(100))   # Fixed: db.string → db.String
          city = db.Column(db.String(50))    # Fixed: db.column → db.Column
          pin = db.Column(db.String(10))     # Fixed: db.strinng → db.String

@app.route('/insert')
def insert_student():
   return render_template('insert_student.html')

@app.route('/submit_student',methods=['POST'])
def submit_student():
  name=request.form.get('txtname')
  addr=request.form.get('txtaddr')
  city=request.form.get('txtcity')
  pin=request.form.get('txtpin')
  stud=student(name,addr,city,pin)

  db.session.add(stud)
  db.session.commit()
  msg="Record insserted suceessfulyy"
  return render_template('success.html',msg=msg)

@app.route('/querystudent')
def query_student():
    all_student=student.query.all()
    return render_template('liststudent.html',data=all_student)

if __name__=='__main__':
    with app.app_context():
      db.create_all()
    app.run(debug=True)