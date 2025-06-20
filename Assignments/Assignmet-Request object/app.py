from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/take_name')
def take_name():
    print("Enter ur name ")
    return render_template('input.html')

@app.route('/result_name', methods=['POST'])
def result_name():
   name=request.form.get('name')
#    if(name == name[::-1]):
#     #   return "name is pallindrome"
#    else:
#     #   return "name is not pallindrome "
   return render_template('result.html', name=name)

if __name__=='__main__':
 app.run(debug=True)