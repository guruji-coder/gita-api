class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    # Add other development settings
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    CORS_ORIGINS = [
        "http://localhost:5000",
        "http://localhost:3000",
        "http://127.0.0.1:8000",
        "http://0.0.0.0:5000"
    ]