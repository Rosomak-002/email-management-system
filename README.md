# Email Management System

A professional Flask-based CRUD (Create, Read, Update, Delete) application for managing email records with a modern web interface and RESTful API architecture.

## 🚀 Features

- **Complete CRUD Operations**: Create, Read, Update, and Delete email records
- **RESTful API Design**: Clean, standardized endpoints following REST principles
- **Professional Frontend**: Modern, responsive web interface with real-time feedback
- **Database Management**: SQLite database with proper schema and constraints
- **Error Handling**: Comprehensive error handling with meaningful user feedback
- **Input Validation**: Client-side and server-side validation for data integrity
- **Professional Logging**: Structured logging for debugging and monitoring
- **CORS Support**: Cross-Origin Resource Sharing for API accessibility

## 🛠 Technology Stack

### Backend
- **Flask**: Python web framework for API development
- **SQLite**: Lightweight, serverless database
- **Flask-CORS**: Cross-origin resource sharing support
- **Python Logging**: Professional logging implementation

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Professional styling with CSS Grid and Flexbox
- **Vanilla JavaScript**: Clean, dependency-free frontend logic
- **ES6+ Features**: Modern JavaScript with classes and async/await

## 📁 Project Structure

```
email-management-system/
├── app.py                      # Main Flask application
├── templates/
│   └── email_management.html   # Frontend interface
├── email_management.db         # SQLite database (auto-generated)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
└── docs/
    └── API.md                  # API documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/email-management-system.git
   cd email-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Web Interface: http://localhost:5002
   - API Base URL: http://localhost:5002/api/email-records

## 📚 API Documentation

### Base URL
```
http://localhost:5002/api/email-records
```

### Endpoints

#### Create Email Record
- **Method**: `POST`
- **URL**: `/api/email-records`
- **Body**: Form data or JSON
  ```json
  {
    "primary_email": "user@example.com",
    "secondary_email": "contact@example.com"
  }
  ```
- **Success Response**: `201 Created`
  ```json
  {
    "message": "Email record created successfully"
  }
  ```

#### Read Email Record
- **Method**: `GET`
- **URL**: `/api/email-records?primary_email=user@example.com`
- **Success Response**: `200 OK`
  ```json
  {
    "primary_email": "user@example.com",
    "secondary_email": "contact@example.com",
    "created_at": "2025-06-14 10:30:00",
    "updated_at": "2025-06-14 10:30:00"
  }
  ```

#### Update Email Record
- **Method**: `PUT`
- **URL**: `/api/email-records`
- **Body**: Form data or JSON
  ```json
  {
    "primary_email": "user@example.com",
    "secondary_email": "newemail@example.com"
  }
  ```
- **Success Response**: `200 OK`
  ```json
  {
    "message": "Email record updated successfully"
  }
  ```

#### Delete Email Record
- **Method**: `DELETE`
- **URL**: `/api/email-records`
- **Body**: Form data or JSON
  ```json
  {
    "primary_email": "user@example.com"
  }
  ```
- **Success Response**: `200 OK`
  ```json
  {
    "message": "Email record deleted successfully"
  }
  ```

### Error Responses

All endpoints return appropriate HTTP status codes with error messages:

```json
{
  "error": "Error description here"
}
```

Common status codes:
- `400 Bad Request`: Invalid input or missing required fields
- `404 Not Found`: Record not found
- `500 Internal Server Error`: Database or server errors

## 🗄 Database Schema

```sql
CREATE TABLE email_records (
    primary_email TEXT PRIMARY KEY,
    secondary_email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🧪 Testing

### Manual Testing
Use the web interface at `http://localhost:5002` to test all CRUD operations.

### API Testing with cURL

**Create a record:**
```bash
curl -X POST http://localhost:5002/api/email-records \
  -d "primary_email=test@example.com&secondary_email=contact@example.com"
```

**Read a record:**
```bash
curl "http://localhost:5002/api/email-records?primary_email=test@example.com"
```

**Update a record:**
```bash
curl -X PUT http://localhost:5002/api/email-records \
  -d "primary_email=test@example.com&secondary_email=updated@example.com"
```

**Delete a record:**
```bash
curl -X DELETE http://localhost:5002/api/email-records \
  -d "primary_email=test@example.com"
```

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `development` for debug mode
- `DATABASE_PATH`: Custom database file path (optional)

### Application Settings
- **Host**: `0.0.0.0` (accessible from all interfaces)
- **Port**: `5002`
- **Debug Mode**: Disabled in production

## 🛡 Security Considerations

- Input validation on both client and server sides
- SQL injection prevention using parameterized queries
- CORS configuration for secure cross-origin requests
- Error messages that don't expose sensitive information

## 📈 Future Enhancements

- [ ] User authentication and authorization
- [ ] Pagination for large datasets
- [ ] Advanced email validation
- [ ] Bulk operations support
- [ ] Export/Import functionality
- [ ] Rate limiting for API endpoints
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] API versioning
- [ ] Database migrations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- SQLite for the reliable embedded database
- Modern web standards for responsive design inspiration

---

*This project demonstrates proficiency in full-stack web development, RESTful API design, database management, and professional software development practices.*