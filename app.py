"""
Flask Email Management System API

A professional CRUD application for managing email records with SQLite database.
Demonstrates RESTful API design patterns and proper error handling.

Author: rosomak
Date: 2025
"""

import os
import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Enable CORS for cross-origin requests
CORS(app)

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'email_management.db')
DATABASE_TIMEOUT = 10

# Database table and column names
TABLE_NAME = 'email_records'
COLUMN_PRIMARY_EMAIL = 'primary_email'
COLUMN_SECONDARY_EMAIL = 'secondary_email'


class DatabaseManager:
    """Handles all database operations for the email management system."""
    
    @staticmethod
    def get_connection() -> Optional[sqlite3.Connection]:
        """
        Establish a connection to the SQLite database.
        
        Returns:
            sqlite3.Connection or None: Database connection object
        """
        try:
            connection = sqlite3.connect(DATABASE_PATH, timeout=DATABASE_TIMEOUT)
            connection.row_factory = sqlite3.Row
            logger.info("Database connection established successfully")
            return connection
        except sqlite3.Error as error:
            logger.error(f"Database connection failed: {error}")
            return None
    
    @staticmethod
    def initialize_database() -> bool:
        """
        Initialize the database and create the email_records table if it doesn't exist.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return False
                
            cursor = connection.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    {COLUMN_PRIMARY_EMAIL} TEXT PRIMARY KEY,
                    {COLUMN_SECONDARY_EMAIL} TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            connection.commit()
            connection.close()
            logger.info(f"Database initialized successfully at {DATABASE_PATH}")
            return True
        except sqlite3.Error as error:
            logger.error(f"Database initialization failed: {error}")
            return False


class EmailRecordService:
    """Service class for handling email record operations."""
    
    @staticmethod
    def create_email_record(primary_email: str, secondary_email: str) -> Dict[str, Any]:
        """
        Create a new email record in the database.
        
        Args:
            primary_email (str): Primary email address
            secondary_email (str): Secondary email address
            
        Returns:
            Dict[str, Any]: Response with success/error status
        """
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return {"error": "Database connection failed", "status": 500}
                
            cursor = connection.cursor()
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} ({COLUMN_PRIMARY_EMAIL}, {COLUMN_SECONDARY_EMAIL}) 
                VALUES (?, ?)
            ''', (primary_email, secondary_email))
            
            connection.commit()
            connection.close()
            
            logger.info(f"Email record created successfully for {primary_email}")
            return {"message": "Email record created successfully", "status": 201}
            
        except sqlite3.IntegrityError:
            logger.warning(f"Attempt to create duplicate record for {primary_email}")
            return {"error": "Primary email already exists", "status": 400}
        except sqlite3.Error as error:
            logger.error(f"Error creating email record: {error}")
            return {"error": str(error), "status": 500}
    
    @staticmethod
    def get_email_record(primary_email: str) -> Dict[str, Any]:
        """
        Retrieve an email record from the database.
        
        Args:
            primary_email (str): Primary email address to search for
            
        Returns:
            Dict[str, Any]: Email record data or error message
        """
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return {"error": "Database connection failed", "status": 500}
                
            cursor = connection.cursor()
            cursor.execute(f'''
                SELECT * FROM {TABLE_NAME} WHERE {COLUMN_PRIMARY_EMAIL} = ?
            ''', (primary_email,))
            
            record = cursor.fetchone()
            connection.close()
            
            if record:
                logger.info(f"Email record retrieved successfully for {primary_email}")
                return {"data": dict(record), "status": 200}
            else:
                logger.info(f"No email record found for {primary_email}")
                return {"error": "Email record not found", "status": 404}
                
        except sqlite3.Error as error:
            logger.error(f"Error retrieving email record: {error}")
            return {"error": str(error), "status": 500}
    
    @staticmethod
    def update_email_record(primary_email: str, secondary_email: str) -> Dict[str, Any]:
        """
        Update an existing email record in the database.
        
        Args:
            primary_email (str): Primary email address (identifier)
            secondary_email (str): New secondary email address
            
        Returns:
            Dict[str, Any]: Response with success/error status
        """
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return {"error": "Database connection failed", "status": 500}
                
            cursor = connection.cursor()
            cursor.execute(f'''
                UPDATE {TABLE_NAME} 
                SET {COLUMN_SECONDARY_EMAIL} = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE {COLUMN_PRIMARY_EMAIL} = ?
            ''', (secondary_email, primary_email))
            
            if cursor.rowcount == 0:
                connection.close()
                logger.info(f"No email record found to update for {primary_email}")
                return {"error": "Email record not found", "status": 404}
            
            connection.commit()
            connection.close()
            
            logger.info(f"Email record updated successfully for {primary_email}")
            return {"message": "Email record updated successfully", "status": 200}
            
        except sqlite3.Error as error:
            logger.error(f"Error updating email record: {error}")
            return {"error": str(error), "status": 500}
    
    @staticmethod
    def delete_email_record(primary_email: str) -> Dict[str, Any]:
        """
        Delete an email record from the database.
        
        Args:
            primary_email (str): Primary email address to delete
            
        Returns:
            Dict[str, Any]: Response with success/error status
        """
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return {"error": "Database connection failed", "status": 500}
                
            cursor = connection.cursor()
            cursor.execute(f'''
                DELETE FROM {TABLE_NAME} WHERE {COLUMN_PRIMARY_EMAIL} = ?
            ''', (primary_email,))
            
            if cursor.rowcount == 0:
                connection.close()
                logger.info(f"No email record found to delete for {primary_email}")
                return {"error": "Email record not found", "status": 404}
            
            connection.commit()
            connection.close()
            
            logger.info(f"Email record deleted successfully for {primary_email}")
            return {"message": "Email record deleted successfully", "status": 200}
            
        except sqlite3.Error as error:
            logger.error(f"Error deleting email record: {error}")
            return {"error": str(error), "status": 500}


def validate_email_input(primary_email: str, secondary_email: str = None) -> Optional[str]:
    """
    Validate email input parameters.
    
    Args:
        primary_email (str): Primary email address
        secondary_email (str, optional): Secondary email address
        
    Returns:
        Optional[str]: Error message if validation fails, None otherwise
    """
    if not primary_email or not primary_email.strip():
        return "Primary email is required"
    
    if secondary_email is not None and (not secondary_email or not secondary_email.strip()):
        return "Secondary email is required"
    
    # Basic email validation (you might want to use a more robust solution)
    if '@' not in primary_email or '.' not in primary_email:
        return "Primary email format is invalid"
    
    if secondary_email and ('@' not in secondary_email or '.' not in secondary_email):
        return "Secondary email format is invalid"
    
    return None


# Initialize database on startup
if not DatabaseManager.initialize_database():
    logger.error("Failed to initialize database. Application may not function properly.")


@app.route('/')
def index():
    """Serve the main application page."""
    logger.info("Serving main application page")
    return render_template('email_management.html')


@app.route('/api/email-records', methods=['POST'])
def create_email_record():
    """
    Create a new email record.
    
    Expected form data:
        - primary_email: Primary email address
        - secondary_email: Secondary email address
    """
    primary_email = request.form.get('primary_email', '').strip()
    secondary_email = request.form.get('secondary_email', '').strip()
    
    # Validate input
    validation_error = validate_email_input(primary_email, secondary_email)
    if validation_error:
        logger.warning(f"Validation failed for create operation: {validation_error}")
        return jsonify({"error": validation_error}), 400
    
    # Create email record
    result = EmailRecordService.create_email_record(primary_email, secondary_email)
    return jsonify({"message": result.get("message"), "error": result.get("error")}), result["status"]


@app.route('/api/email-records', methods=['GET'])
def get_email_record():
    """
    Retrieve an email record by primary email.
    
    Query parameters:
        - primary_email: Primary email address to search for
    """
    primary_email = request.args.get('primary_email', '').strip()
    
    # Validate input
    validation_error = validate_email_input(primary_email)
    if validation_error:
        logger.warning(f"Validation failed for read operation: {validation_error}")
        return jsonify({"error": validation_error}), 400
    
    # Get email record
    result = EmailRecordService.get_email_record(primary_email)
    if result["status"] == 200:
        return jsonify(result["data"]), 200
    else:
        return jsonify({"error": result["error"]}), result["status"]


@app.route('/api/email-records', methods=['PUT'])
def update_email_record():
    """
    Update an existing email record.
    
    Expected JSON or form data:
        - primary_email: Primary email address (identifier)
        - secondary_email: New secondary email address
    """
    data = request.json if request.is_json else request.form
    
    primary_email = data.get('primary_email', '').strip()
    secondary_email = data.get('secondary_email', '').strip()
    
    # Validate input
    validation_error = validate_email_input(primary_email, secondary_email)
    if validation_error:
        logger.warning(f"Validation failed for update operation: {validation_error}")
        return jsonify({"error": validation_error}), 400
    
    # Update email record
    result = EmailRecordService.update_email_record(primary_email, secondary_email)
    return jsonify({"message": result.get("message"), "error": result.get("error")}), result["status"]


@app.route('/api/email-records', methods=['DELETE'])
def delete_email_record():
    """
    Delete an email record.
    
    Expected JSON or form data:
        - primary_email: Primary email address to delete
    """
    data = request.json if request.is_json else request.form
    primary_email = data.get('primary_email', '').strip()
    
    # Validate input
    validation_error = validate_email_input(primary_email)
    if validation_error:
        logger.warning(f"Validation failed for delete operation: {validation_error}")
        return jsonify({"error": validation_error}), 400
    
    # Delete email record
    result = EmailRecordService.delete_email_record(primary_email)
    return jsonify({"message": result.get("message"), "error": result.get("error")}), result["status"]


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {error}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    logger.info("Starting Email Management System API")
    app.run(host='0.0.0.0', port=5002, debug=False)