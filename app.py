from flask import Flask, render_template
from flask_cors import CORS
from server.config import ProductionConfig, DevelopmentConfig
import os

def create_app(config_class=None):
    if config_class is None:
        config_class = DevelopmentConfig if os.environ.get('FLASK_ENV') == 'development' else ProductionConfig
    
    app = Flask(__name__, 
                static_folder='server/static',
                template_folder='server/templates')
    app.config.from_object(config_class)
    
    # Configure CORS
    cors_origins = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')
    CORS(app, resources={
        r"/api/*": {
            "origins": cors_origins,
            "methods": ["GET", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Register blueprints
    from server.api.routes import gita_bp
    app.register_blueprint(gita_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

app = create_app()