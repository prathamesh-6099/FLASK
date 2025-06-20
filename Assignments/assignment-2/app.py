from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def list():
   client=[34,134,235,5254,234]
   return render_template('list.html',client=client)

if __name__=='__main__':
    app.run(debug=True)