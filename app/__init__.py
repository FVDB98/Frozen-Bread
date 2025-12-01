from flask import Flask
from flask_login import LoginManager
from .database import get_db, close_db
from .models import User

def create_app():
    app = Flask(__name__)
    app.secret_key = "replace-this-secure-key"

    # Database cleanup
    app.teardown_appcontext(close_db)

    # Login manager setup
    login_manager = LoginManager()
    login_manager.login_view = "auth.login_page"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        db = get_db()
        row = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

        if row is None:
            return None

        return User(
            row["id"],
            row["name"],
            row["email"],
            row["password_hash"],
            row["address_line1"],
            row["address_line2"],
            row["city"],
            row["postcode"],
            row["country"],
            row["created_at"],
            row["is_admin"]
        )

    # Register blueprints
    from .routes.main import main
    from .routes.auth import auth
    from .routes.account import account

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(account)

    return app
