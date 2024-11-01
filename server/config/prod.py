class ProductionConfig:
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    
    # Security settings
    PROPAGATE_EXCEPTIONS = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    PREFERRED_URL_SCHEME = 'https'
    
    # CORS settings
    CORS_ORIGINS = [
        "https://vijaygita.com",
        "https://www.vijaygita.com",
        "http://localhost:3000"
    ]
    