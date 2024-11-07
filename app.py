from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from routes import routes
from utils import wait_for_db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

wait_for_db(app)

app.register_blueprint(routes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)