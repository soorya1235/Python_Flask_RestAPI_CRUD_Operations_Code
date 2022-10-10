from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)

order = {
    "order1": {
        "size": "small",
        "toppings": "cheese",
        "crust": "thin crust"
    },
    "order2": {
        "size": "medium",
        "toppings": "tomato",
        "crust": "choppings"
    }
}


@app.route("/orders")
def get_order():
    response = make_response(jsonify(order), 200)
    return response


'''
Get Order details using orderid
'''


@app.route("/orders/<oid>")
def get_orderid(oid):
    if oid in order:
        response = make_response(jsonify(order[oid]), 200)
        return response

    return "Order ID Not found"

@app.route("/orders/<oid>/<items>")
def get_orderid_items(oid,items):
    items = order[oid].get(items)
    if items:
        response = make_response(jsonify(items),200)
        return response
    return "No Items Found"

@app.route("/orders/<oid>",methods=["post"]) # update or create new object.
def post_order_id(oid):
    data = request.get_json()
    if oid in order:
        response = make_response(jsonify({"error":"Orderid already exists"}))
        return response
    order.update({oid:data})
    return make_response(jsonify({"sucess":"OrderID created sucessfully"}))


@app.route("/orders/<oid>",methods=["put"]) # it will update all the attributes
def put_order_id(oid):
    data = request.get_json()
    if oid in order:
        order.update({oid: data})
        response = make_response(jsonify({"success":"Orderid updated sucssfully"}))
        return response
    order[oid]=request.get_json()
    return make_response(jsonify({"sucess":"Order Id Created...As part of put it was not found"}))

@app.route("/orders/<oid>",methods=["patch"]) # it will update only the specific attribute
def patch_order_id(oid):
    data = request.get_json()
    if oid in order:
        for k,v in data.items():
            order[oid][k]=v
        response = make_response(jsonify({"success":"Orderid updated sucssfully"}),200)
        return response
    order[oid]=request.get_json()
    return make_response(jsonify({"sucess":"Order Id Created...As part of put it was not found"}),201)


@app.route("/orders/<oid>",methods=["delete"]) # it will delete the records.
def delete_order_id(oid):
    del order[oid]
    response = make_response(jsonify({"message":"order deleted"}),204)
    return response
    response = make_response(jsonify({"error":"order does not already exists"}),404)
    return response

if __name__ == '__main__':
    app.run(debug=True)
