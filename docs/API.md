# Email Management System API Documentation

## Overview

The Email Management System is a professional CRUD (Create, Read, Update, Delete) application built with Flask that manages email records using SQLite database. It provides a RESTful API for managing primary and secondary email address pairs.

**Author:** rosomak  
**Version:** 2025  
**Base URL:** `http://localhost:5002`  
**Database:** SQLite (`email_management.db`)

## Architecture

### Components
- **Flask Web Application** - Main application server
- **SQLite Database** - Data persistence layer
- **RESTful API** - HTTP endpoints for CRUD operations
- **Web Interface** - HTML/CSS/JavaScript frontend
- **CORS Support** - Cross-origin resource sharing enabled

### Database Schema

**Table:** `email_records`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `primary_email` | TEXT | PRIMARY KEY | Primary email address (unique identifier) |
| `secondary_email` | TEXT | NOT NULL | Secondary email address |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation timestamp |
| `updated_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Last update timestamp |

## API Endpoints

### Base URL
```
http://localhost:5002/api/email-records
```

---

### 1. Create Email Record

**Endpoint:** `POST /api/email-records`

Creates a new email record with primary and secondary email addresses.

#### Request

**Content-Type:** `application/x-www-form-urlencoded`

**Form Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `primary_email` | string | Yes | Primary email address (must be unique) |
| `secondary_email` | string | Yes | Secondary email address |

#### Example Request
```http
POST /api/email-records HTTP/1.1
Host: localhost:5002
Content-Type: application/x-www-form-urlencoded

primary_email=user@example.com&secondary_email=contact@example.com
```

#### Response

**Success (201 Created):**
```json
{
  "message": "Email record created successfully",
  "error": null
}
```

**Error (400 Bad Request):**
```json
{
  "message": null,
  "error": "Primary email already exists"
}
```

**Error (400 Bad Request - Validation):**
```json
{
  "message": null,
  "error": "Primary email is required"
}
```

---

### 2. Read Email Record

**Endpoint:** `GET /api/email-records`

Retrieves an email record by primary email address.

#### Request

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `primary_email` | string | Yes | Primary email address to search for |

#### Example Request
```http
GET /api/email-records?primary_email=user@example.com HTTP/1.1
Host: localhost:5002
```

#### Response

**Success (200 OK):**
```json
{
  "primary_email": "user@example.com",
  "secondary_email": "contact@example.com",
  "created_at": "2025-06-14 10:30:00",
  "updated_at": "2025-06-14 10:30:00"
}
```

**Error (404 Not Found):**
```json
{
  "error": "Email record not found"
}
```

**Error (400 Bad Request):**
```json
{
  "error": "Primary email is required"
}
```

---

### 3. Update Email Record

**Endpoint:** `PUT /api/email-records`

Updates the secondary email address for an existing record.

#### Request

**Content-Type:** `application/x-www-form-urlencoded` or `application/json`

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `primary_email` | string | Yes | Primary email address (identifier) |
| `secondary_email` | string | Yes | New secondary email address |

#### Example Request (Form Data)
```http
PUT /api/email-records HTTP/1.1
Host: localhost:5002
Content-Type: application/x-www-form-urlencoded

primary_email=user@example.com&secondary_email=newemail@example.com
```

#### Example Request (JSON)
```http
PUT /api/email-records HTTP/1.1
Host: localhost:5002
Content-Type: application/json

{
  "primary_email": "user@example.com",
  "secondary_email": "newemail@example.com"
}
```

#### Response

**Success (200 OK):**
```json
{
  "message": "Email record updated successfully",
  "error": null
}
```

**Error (404 Not Found):**
```json
{
  "message": null,
  "error": "Email record not found"
}
```

---

### 4. Delete Email Record

**Endpoint:** `DELETE /api/email-records`

Deletes an email record by primary email address.

#### Request

**Content-Type:** `application/x-www-form-urlencoded` or `application/json`

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `primary_email` | string | Yes | Primary email address to delete |

#### Example Request (Form Data)
```http
DELETE /api/email-records HTTP/1.1
Host: localhost:5002
Content-Type: application/x-www-form-urlencoded

primary_email=user@example.com
```

#### Example Request (JSON)
```http
DELETE /api/email-records HTTP/1.1
Host: localhost:5002
Content-Type: application/json

{
  "primary_email": "user@example.com"
}
```

#### Response

**Success (200 OK):**
```json
{
  "message": "Email record deleted successfully",
  "error": null
}
```

**Error (404 Not Found):**
```json
{
  "message": null,
  "error": "Email record not found"
}
```

---

## Error Handling

### HTTP Status Codes

| Code | Description | When Used |
|------|-------------|-----------|
| 200 | OK | Successful GET, PUT, DELETE operations |
| 201 | Created | Successful POST operation |
| 400 | Bad Request | Invalid input data or validation errors |
| 404 | Not Found | Record not found or invalid endpoint |
| 500 | Internal Server Error | Database connection issues or server errors |

### Error Response Format

All error responses follow this format:
```json
{
  "error": "Error message describing what went wrong"
}
```

### Common Error Messages

- `"Primary email is required"`
- `"Secondary email is required"`
- `"Primary email format is invalid"`
- `"Secondary email format is invalid"`
- `"Primary email already exists"`
- `"Email record not found"`
- `"Database connection failed"`
- `"Endpoint not found"`
- `"Internal server error"`

## Validation Rules

### Email Format Validation
- Must contain `@` symbol
- Must contain at least one `.` (dot)
- Cannot be empty or contain only whitespace

### Input Requirements
- **Create Operation:** Both primary and secondary emails required
- **Read Operation:** Only primary email required
- **Update Operation:** Both primary and secondary emails required
- **Delete Operation:** Only primary email required

## Web Interface

### Frontend Features
- Responsive design with modern CSS
- Real-time form validation
- Loading states and user feedback
- Error and success message display
- Professional styling with animations

### Default Values
The web interface includes default values for testing:
- Primary Email: `user@example.com`
- Secondary Email: `contact@example.com`

## Installation & Setup

### Prerequisites
```bash
pip install flask flask-cors
```

### Running the Application
```bash
python app.py
```

The application will start on `http://localhost:5002`

### Database Initialization
The SQLite database (`email_management.db`) is automatically created on first run.

## Configuration

### Application Settings
- **Host:** `0.0.0.0` (accepts connections from any IP)
- **Port:** `5002`
- **Debug Mode:** `False` (production ready)
- **Database Timeout:** `10` seconds
- **CORS:** Enabled for all origins

### File Structure
```
project/
├── app.py                    # Main Flask application
├── email_management.db       # SQLite database (auto-created)
├── templates/
│   └── email_management.html # Web interface
└── static/                   # Static files (if any)
```

## Logging

The application includes comprehensive logging:
- **Level:** INFO
- **Format:** `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
- **Events Logged:**
  - Database connections
  - CRUD operations
  - Validation errors
  - Server errors

## Security Considerations

- Input validation and sanitization
- SQL injection prevention using parameterized queries
- CORS policy (configure for production)
- No authentication implemented (add as needed)
- HTTPS recommended for production

## Performance Features

- Connection pooling with timeout
- Efficient database queries
- Proper connection cleanup
- Optimized frontend with caching

## Browser Compatibility

The web interface supports:
- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## API Testing Examples

### Using curl

**Create Record:**
```bash
curl -X POST http://localhost:5002/api/email-records \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "primary_email=test@example.com&secondary_email=backup@example.com"
```

**Read Record:**
```bash
curl -X GET "http://localhost:5002/api/email-records?primary_email=test@example.com"
```

**Update Record:**
```bash
curl -X PUT http://localhost:5002/api/email-records \
  -H "Content-Type: application/json" \
  -d '{"primary_email":"test@example.com","secondary_email":"updated@example.com"}'
```

**Delete Record:**
```bash
curl -X DELETE http://localhost:5002/api/email-records \
  -H "Content-Type: application/json" \
  -d '{"primary_email":"test@example.com"}'
```

## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check file permissions
   - Ensure directory is writable
   - Verify SQLite installation

2. **Port Already in Use**
   - Change port in `app.run()` call
   - Kill existing processes on port 5002

3. **CORS Issues**
   - Verify CORS configuration
   - Check browser console for errors

4. **Email Validation Errors**
   - Ensure proper email format
   - Check for whitespace characters

## License

This is a demonstration application. Please review and modify security settings before production use.