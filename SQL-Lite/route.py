
from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

conn = sqlite3.connect("mycollege.db")
cur = conn.cursor()
cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='student'")
    
if cur.fetchone()[0] == 1:
        print("Table already exists")
else:
        conn.execute("CREATE TABLE student(name TEXT, addr TEXT, city TEXT, pin TEXT)")
        print("Table Created")
    
conn.close()

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/addstudent')
def add_student():
       return render_template('add_student.html')

@app.route('/savestudent',methods=['GET','POST'])
def save_student():
 msg=''
 if(request.method=='POST'):
       try:
              name=request.form.get('studname')
              addr=request.form.get('studaddr')
              city=request.form.get('studcity')
              pin=request.form.get('studpin')
              
              with sqlite3.connect('mycollege.db') as conn:
                     cur=conn.cursor()
                     cur.execute("INSERT INTO student (name,addr,city,pin) values(?,?,?,?)",(name,addr,city,pin))
                     conn.commit()
                     msg="Data inserted Successfully"
       
       except:
              conn.rollback()
              msg="Could not insert data"
 return render_template('success.html',msg=msg)

@app.route('/liststudent')
def list_student():
       conn=sqlite3.connect("mycollege.db")
       conn.row_factory=sqlite3.Row
       cur=conn.cursor()

       cur.execute('SELECT * FROM student')
       rows=cur.fetchall()

       return render_template('view.html',rows=rows)
@app.route('/deletestudent',methods=['POST'])
def delete_student():
      student_name=request.form.get('txtname')
      try:
            with sqlite3.connect('mycollege.db') as conn:
                  my_query="DELETE FROM student WHERE name='"+student_name+"';"
                  conn.execute(my_query)
                  conn.commit()
                  msg="Total Rows Deleted are: "+ str(conn.total_changes)
      except:
            conn.rollback()
            msg="Could not Delete any records"
      finally:
            conn.close()
      return render_template('success.html',msg=msg)
@app.route('/deleteinput')
def delete_input():
   return render_template('delete_input.html')

if __name__=="__main__":
    app.run(debug=True)