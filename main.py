from flask import Flask,render_template,request,make_response,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello kottae kuttqea"

@app.route("/soorya")
def soorya_world():
    return "Hello Soorya!!!"

@app.route("/html")
def get_html():
    return render_template("index.html")

@app.route("/qs")
def get_qs():
    if request.args:
        req=request.args
        return "".join(f"{k}:{v}" for k,v in req.items())
    return "No Query Parameters Passed"

order = {
    "order1":{
        "size":"small",
        "toppings":"cheese",
        "crust":"thin crust"
    }
}

@app.route("/orders")
def get_order():
    response = make_response(jsonify(order),200)
    return response


if __name__ == '__main__':
    app.run(debug=True)

