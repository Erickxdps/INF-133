from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.dul_model import Dulce
from views import dul_view

# Importamos el decorador de roles
from utils.decorators import role_required

dulce_bp = Blueprint("dulce", __name__)

# Ruta para obtener la lista de dulces
@dulce_bp.route("/dulces")
@login_required
def list_dulces():
    dulces = Dulce.get_all()
    return dul_view.list_dulces(dulces)


@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_dulce():
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            dulce = Dulce(marca = marca, peso = peso, sabor = sabor, origen = origen)
            dulce.save()
            flash("Dulce creado exitosamente", "success")
            return redirect(url_for("dulce.list_dulces"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return dul_view.create_dulce()


@dulce_bp.route("/dulces/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Dulce no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            dulce.update(marca = marca, peso = peso, sabor = sabor, origen = origen)
            flash("Dulce actualizado exitosamente", "success")
            return redirect(url_for("dulce.list_dulces"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return dul_view.update_dulce(dulce)


@dulce_bp.route("/dulces/<int:id>/delete")
@login_required
@role_required("admin")
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Dulce no encontrado", 404
    if current_user.has_role("admin"):
        dulce.delete()
        flash("Dulce eliminado exitosamente", "success")
        return redirect(url_for("dulce.list_dulces"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
