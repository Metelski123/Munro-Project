from flask import Flask, render_template

from controllers.bag_controller import bags_blueprint
from controllers.munro_controller import munros_blueprint
from controllers.climber_controller import climbers_blueprint

app = Flask(__name__)

app.register_blueprint(bags_blueprint)
app.register_blueprint(munros_blueprint)
app.register_blueprint(climbers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)