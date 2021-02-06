from db.run_sql import run_sql
from models.munro import Munro
from models.climber import Climber

def save(munro):
    sql = "INSERT INTO munros(name, height, duration) VALUES ( %s, %s, %s ) RETURNING id"
    values = [munro.name, munro.category]
    results = run_sql( sql, values )
    munro.id = results[0]['id']
    return munro


def select_all():
    munros = []

    sql = "SELECT * FROM munros"
    results = run_sql(sql)

    for row in results:
        munro = Munros(row['name'], row['height'], row['id'])
        munros.append(munro)
    return munros


def select(id):
    munro = None
    sql = "SELECT * FROM munros WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        munro = Munros(result['name'], result['height'], result['id'] )
    return munro


def delete_all():
    sql = "DELETE FROM munros"
    run_sql(sql)

def climbers(munro):
    climbers = []
    
    sql = "SELECT climbers.* FROM climbers INNER JOIN bags ON bag.climber_id = climbers.id WHERE munro_id = %s"
    values = [munro.id]
    results = run_sql(sql, values)

    for row in results:
        climber = Climber(row['name'], row['id'])
        climbers.append(climber)
    return climbers