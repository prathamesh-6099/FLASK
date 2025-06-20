from flask import render_template,Flask,request,abort,redirect,url_for
from http import HTTPStatus
app=Flask(__name__)
@app.route('/redirected_page')
def redirected_page():
    print("Request Argument agian from redirect page", request.args)
    return "this is redirected page"

@app.route('/redirectdemo')
def redirectdemo():
    print("Request Argument from demo", request.args)
    res=redirected_page()
    return redirect('http://google.com')
if __name__=='__main__':
    app.run(debug=True)
