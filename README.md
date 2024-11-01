# Bhagavad Gita API

REST API for the Bhagavad Gita, providing access to verses in Sanskrit, transliteration, and translation.

## Features

- 🚀 High-performance API endpoints
- 📚 Complete Bhagavad Gita text
- 🌍 Sanskrit, transliteration, and English translation
- ⚡ Optimized for quick response times
- 🔒 Rate limiting and security headers

## API Endpoints

### Health Check

```
GET /api/health
```

### Get Chapter

```
GET /api/gita/chapter/{chapter_number}
```

### Get Verse

```
GET /api/gita/verse/{chapter_number}/{verse_number}
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gita-api.git
   cd gita-api
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create .env file:
   ```
   env
   FLASK_ENV=development
   CORS_ORIGINS=http://localhost:3000,https://vijaygita.com
   ```

4. Run development server:
   ```
   bash
   python wsgi.py
   ```

## Deployment

This API is deployed on Render.com. To deploy:

1. Fork this repository
2. Connect to Render
3. Configure environment variables
4. Deploy

## Testing

Run tests with:
```
pytest
```

## License

MIT License
EOL
