from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)

# Configure SQLite database (for demo purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)



from routes import *

if __name__ == '__main__':
    app.run(debug=True)