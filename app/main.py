import os
from flask import Flask
from dotenv import load_dotenv
from app.email.controllers import email_bp

# load env from instance/.env 
def create_app(config_name: str = None):
    app = Flask(__name__, instance_relative_config=True)

    # load instance/.env if exists
  
    
    # Primero intenta cargar instance/.env
    env_instance = os.path.join(app.instance_path, ".env")
    if os.path.exists(env_instance):
        load_dotenv(env_instance)
        print("Ingresa")
        print(app.config.get('DB_HOST'))
        app.config['DB_HOST'] = os.getenv("DB_HOST", app.config.get('DB_HOST'))
        app.config['DB_PORT'] = os.getenv("DB_PORT", app.config.get('DB_PORT'))
        app.config['DB_SERVICE'] = os.getenv("DB_SERVICE", app.config.get('DB_SERVICE'))
        app.config['DB_USER'] = os.getenv("DB_USER", app.config.get('DB_USER'))
        app.config['DB_PASSWORD'] = os.getenv("DB_PASSWORD", app.config.get('DB_PASSWORD'))
        app.config['ORACLE_CLIENT_PATH'] = os.getenv("ORACLE_CLIENT_PATH", app.config.get('ORACLE_CLIENT_PATH'))

    else:
        # fallback a raíz
        load_dotenv()


    # config selection (keeps previous pattern)
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    if config_name == 'production':
        from app.config.production import ProductionConfig as Config
    elif config_name == 'testing':
        from app.config.testing import TestingConfig as Config
    else:       
        from app.config.development import DevelopmentConfig as Config
    
    app.config.from_object(Config)

    # initialize extensions
    from app.extensions.db import init_db_pool
    from app.extensions.cors_ext import cors
    from app.exceptions.handlers import register_error_handlers

    init_db_pool(app)   # create pool on startup
    cors.init_app(app)

    # register blueprints   
    app.register_blueprint(email_bp, url_prefix='/api/send_email')
    register_error_handlers(app)

    @app.route('/')
    def index():
        return {'status': 'ok', 'env': config_name}

    return app

