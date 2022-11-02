from app import app
from app import db
import views
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')


if __name__ == "__main__":
    app.run()
