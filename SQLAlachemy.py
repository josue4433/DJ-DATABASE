from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playlist.db'
db = SQLAlchemy(app)

class PLaylist(db.Model):
    id = db.Column(db.integer,primary_key=True)
    title = db.Column(db.String(100) , nullable=False)
    description = db.Column(db.String(1000), nullable=True)