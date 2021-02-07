from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.bag import Bag
import repositories.bag_repository as bag_repository
import repositories.climber_repository as climber_repository
import repositories.munro_repository as munro_repository

bags_blueprint = Blueprint("bags", __name__)

@bags_blueprint.route("/bags")
def bags():
    bags = bag_repository.select_all() # NEW
    return render_template("bags/index.html", bags = bags)

# NEW
# GET '/bags/new'
@bags_blueprint.route("/bags/new", methods=['GET'])
def new_task():
    climbers = climber_repository.select_all()
    munros = munro_repository.select_all()
    return render_template("bags/new.html", climbers = climbers, munros = munros)

# CREATE
# POST '/visits'
@bags_blueprint.route("/bags",  methods=['POST'])
def create_task():
    climber_id = request.form['climber_id']
    munro_id = request.form['munro_id']
    review = request.form['review']
    climber = climber_repository.select(climber_id)
    munro = munro_repository.select(munro_id)
    bag = Bag(climber, munro, review)
    bag_repository.save(bag)
    return redirect('/bags')


# DELETE
# DELETE '/visits/<id>'
@bags_blueprint.route("/bags/<id>/delete", methods=['POST'])
def delete_task(id):
    bag_repository.delete(id)
    return redirect('/bags')