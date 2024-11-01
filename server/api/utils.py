import logging
from functools import lru_cache
import json
import os

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'gita_api.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def load_gita_data():
    """Load Gita data with caching"""
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'Gita.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading Gita data: {e}")
        return None

def validate_chapter_num(chapter_num):
    """Validate chapter number"""
    return 1 <= chapter_num <= 18

def validate_verse_num(verse_num):
    """Validate verse number format"""
    try:
        num = int(verse_num)
        return 1 <= num <= 78  # Maximum verses in any chapter
    except ValueError:
        return False