from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

@app.route('/', methods=[ 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        name = request.form['username']
        if is_palindrome(name):
            result = f"'{name}' is a palindrome!"
        else:
            result = f"'{name}' is not a palindrome."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
