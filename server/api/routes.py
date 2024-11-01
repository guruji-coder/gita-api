from flask import Blueprint, jsonify, current_app
from .utils import load_gita_data, validate_chapter_num, validate_verse_num
import logging

logger = logging.getLogger(__name__)
gita_bp = Blueprint('gita', __name__)

@gita_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "gita-api",
        "version": "1.0.0"
    }), 200

@gita_bp.route('/gita/chapter/<int:chapter_num>', methods=['GET'])
def get_chapter(chapter_num):
    logger.info(f"Fetching chapter {chapter_num}")
    
    if not validate_chapter_num(chapter_num):
        logger.warning(f"Invalid chapter number requested: {chapter_num}")
        return jsonify({
            "error": "Invalid chapter number",
            "message": "Chapter number must be between 1 and 18"
        }), 400
        
    gita_data = load_gita_data()
    if not gita_data:
        logger.error("Failed to load Gita data")
        return jsonify({
            "error": "Data unavailable",
            "message": "Unable to load Gita data"
        }), 500
        
    for chapter in gita_data["contents"]:
        if chapter["chapter_number"] == chapter_num:
            logger.info(f"Successfully fetched chapter {chapter_num}")
            return jsonify(chapter)
    
    logger.warning(f"Chapter {chapter_num} not found")
    return jsonify({
        "error": "Not found",
        "message": f"Chapter {chapter_num} not found"
    }), 404

@gita_bp.route('/gita/verse/<int:chapter_num>/<string:verse_num>', methods=['GET'])
def get_verse(chapter_num, verse_num):
    logger.info(f"Fetching chapter {chapter_num}, verse {verse_num}")
    
    if not validate_chapter_num(chapter_num):
        return jsonify({
            "error": "Invalid chapter number",
            "message": "Chapter number must be between 1 and 18"
        }), 400
        
    gita_data = load_gita_data()
    if not gita_data:
        return jsonify({
            "error": "Data unavailable",
            "message": "Unable to load Gita data"
        }), 500
        
    for chapter in gita_data["contents"]:
        if chapter["chapter_number"] == chapter_num:
            for verse in chapter["verses"]:
                if verse["verse_number"] == verse_num:
                    logger.info(f"Successfully fetched verse {verse_num} from chapter {chapter_num}")
                    return jsonify(verse)
    
    logger.warning(f"Verse {verse_num} not found in chapter {chapter_num}")
    return jsonify({
        "error": "Not found",
        "message": f"Verse {verse_num} not found in chapter {chapter_num}"
    }), 404