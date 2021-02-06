from db.run_sql import run_sql
from models.munro import Munro
from models.climber import Climber

def save(climber):
    sql = "INSERT INTO climbers( name ) VALUES ( %s ) RETURNING id"
    values = [climber.name]
    results = run_sql( sql, values )
    climber.id = results[0]['id']
    return climber


def select_all():
    climbers = []

    sql = "SELECT * FROM climbers"
    results = run_sql(sql)
    for row in results:
        climber = Climber(row['name'], row['id'])
        climbers.append(climber)
    return climbers


def select(id):
    climber = None
    sql = "SELECT * FROM climbers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        climber = Climber(result['name'], result['id'] )
    return climber


def delete_all():
    sql = "DELETE FROM climbers"
    run_sql(sql)

def munros(climber):
    munros = []

    sql = SELECT "munros.* FROM munros INNER JOIN bags ON bags.munro_id = munros.id WHERE climber_id = %s;"
    values = [climber.id]
    result = run_sql(sql, values)

    for row in results:
        munro = munros(row['name'], row['height'], row['id'])
        locations.append(location)
        
    return munros