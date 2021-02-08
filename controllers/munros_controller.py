from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.munro import Munro
import repositories.munro_repository as munro_repository

munros_blueprint = Blueprint("munros", __name__)

@munros_blueprint.route("/munros")
def munros():
    munros = munro_repository.select_all()
    return render_template("munros/index.html", munros = munros)

@munros_blueprint.route("/munros/<id>")
def show(id):
    munro = munro_repository.select(id)
    climber = munro_repository.climbers(munro)
    return render_template("munros/show.html", munro=munro, climber=climber)