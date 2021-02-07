from db.run_sql import run_sql
from models.bag import Bag
import repositories.climber_repository as climber_repository
import repositories.munro_repository as climber_repository

def save(bag):
    sql = "INSERT INTO bags ( climber_id, munro_id, review ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [bag.climber.id, bag.munro.id, bag.review]
    results = run_sql( sql, values )
    bag.id = results[0]['id']
    return bag


def select_all():
    bags = []

    sql = "SELECT * FROM bags"
    results = run_sql(sql)

    for row in results:
        climber = climber_repository.select(row['climber_id'])
        munro = munro_repository.select(row['munro_id'])
        bag = Bag(climber, munro, row['review'], row['id'])
        bags.append(bag)
    return bags


def delete_all():
    sql = "DELETE FROM bags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)