from flask import Flask

from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    from models.user import User
    db.create_all()

@app.route("/")
def home():
    return "Academic Insight Portal Running"

if __name__ == "__main__":
    app.run(debug=True)