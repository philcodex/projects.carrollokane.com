from flask import Flask, render_template
from config import Config
from models import db, HealthCheck

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    checks = HealthCheck.query.order_by(HealthCheck.checked_at.desc()).limit(50).all()
    return render_template("index.html", checks=checks)

if __name__ == "__main__":
    app.run(debug=True)
