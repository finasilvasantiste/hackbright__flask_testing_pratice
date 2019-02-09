from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    Game.query.delete()

    game_1 = Game(name="Taco", description="a cross-country train adventure")
    game_2 = Game(name="Cat", description="supply the most cities with power")

    # print(game_1)
    # db.session.add(game_1)
    db.session.add_all([game_1, game_2])
    db.session.commit()

    # FIXME: write a function that creates a game and adds it to the database.
    # print("FIXME")


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
