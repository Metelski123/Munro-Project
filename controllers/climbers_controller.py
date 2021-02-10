from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.climber import Climber
import repositories.climber_repository as climber_repository

climbers_blueprint = Blueprint("climbers", __name__)

@climbers_blueprint.route("/climbers")
def climbers():
    climbers = climber_repository.select_all()
    return render_template("climbers/index.html", climbers = climbers)

@climbers_blueprint.route("/climbers/<id>")
def show(id):
    climber = climber_repository.select(id)
    munros = climber_repository.munros(climber)
    return render_template("climbers/show.html", climber=climber, munros=munros)

@climbers_blueprint.route("/climbers/new")
def new_climber():
    return render_template("climbers/new.html")

@climbers_blueprint.route("/climbers",  methods=['POST'])
def create_climber():
    name = request.form['name']
    climber = Climber(name)
    climber_repository.save(climber)
    return redirect('/climbers')
