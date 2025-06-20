from flask import render_template,Flask,request,abort
from http import HTTPStatus
app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html',context={'error':error}),404
@app.route('/printstatus')
def print_status():
    print(list(HTTPStatus))
    username=request.args.get("uname")
    if username== 'admin':
     return render_template('print_status.html', statuses=list(HTTPStatus))
    else:
     abort(500)
if __name__=='__main__':
    app.run(debug=True)