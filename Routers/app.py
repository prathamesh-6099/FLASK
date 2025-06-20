from flask import Flask

app = Flask(__name__)

@app.route("/home")
@app.route("/home/<username>")
def hello_world(username="guest"):
    # return render_template('index.html')
    return "hello "+ username

@app.route("/products/<int:product_no>")
def products(product_no):
    return "This is my product"+str(product_no)

if __name__=="__main__":
    app.run(debug=True, port=5001)