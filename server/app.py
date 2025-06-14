from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # or your database URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Your models and routes here...

if __name__ == '__main__':
    app.run(debug=True)