from flask import Blueprint,request,jsonify
from views.store_view import render_product_list,render_product_detail
from utils.decorators import jwt_required,roles_required
from models.store_model import Product

product = Blueprint("product",__name__)

@product.route("/products",methods=["GET"])
@jwt_required
@roles_required(roles=["admin"])
def get_products():
    products=Product.get_all()
    return jsonify(render_product_list(products))

@product.route("/products/<int:id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error":"Producto no encontrada"}),404
    return jsonify(render_product_detail(product))

@product.route("/products",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_product():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    if not name or description is None or not price or not stock:
        return jsonify({"error":"Faltan atributos requeridos"}),400
    
    product=Product(name, description, price, stock)
    product.save()
    return jsonify(render_product_detail(product)),201

@product.route("/products/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error":"Producto no encontrada"}),404
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")


    product.update(name, description, price, stock)
    return jsonify(render_product_detail(product)),200

@product.route("/products/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_product(id):
    product=Product.get_by_id(id)
    if not product:
        return jsonify({"Error":"Producto no encontrada"}),404
    
    product.delete()
    return "", 204