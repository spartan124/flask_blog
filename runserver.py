from app import create_app
from app.config.config import config_dict

app = create_app(config=config_dict['dev'])

if __name__ == '__main__':
    app.run(
        port=5500, debug=True
    )