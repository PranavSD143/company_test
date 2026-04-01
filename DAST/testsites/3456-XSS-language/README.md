# Vulnerable SQL Injection App

A Flask application demonstrating SQL injection vulnerability

## Setup & Execution Instructions

### VERSION COMPATIBILITY MATRIX
Component               | Version      | Compatible With
------------------------|--------------|------------------
Python                  | 3.11         | Flask 2.3
Flask                   | 2.3.3        | Python 3.11, PyMySQL 1.1
MySQL Server            | 8.0          | PyMySQL 1.1
PyMySQL                 | 1.1.0        | MySQL 8.0, Flask 2.3
Docker Base Image       | python:3.11-slim | Python 3.11
MySQL Docker Image      | mysql:8.0    | MySQL Server 8.0

### EXECUTION GUIDE

**A. Docker Setup (Recommended - Single Command)**

1. **Prerequisites**: 
   - Docker Engine 20.10+ 
   - Docker Compose V2 (or docker-compose 1.29+)
   - No other dependencies needed

2. **Quick Start**:
```bash
   # Create project directory
   mkdir vulnerable-app && cd vulnerable-app
   
   # Copy all files from the FILE CONTENTS section above
   
   # Start everything
   docker-compose up --build
   
   # Access application at: http://localhost:5000
   # Initialize database by visiting the page and submitting a query
```

3. **Stop Application**:
```bash
docker-compose down
   
   # To remove volumes (reset database):
docker-compose down -v
```

4. **Troubleshooting**:
   - View logs: `docker-compose logs -f`
   - Rebuild: `docker-compose up --build --force-recreate`
   - Check service status: `docker-compose ps`

**B. Local Setup (Alternative - Without Docker)**

1. **Prerequisites**: 
   - Python 3.11
   - MySQL Server 8.0 running locally
   - Flask 2.3.3
   - PyMySQL 1.1.0

2. **Project Setup**: 
   - Create directory and copy files
   - Create database: `mysql -uroot -p<password> -e "CREATE DATABASE vulnerable_db;"`

3. **Dependencies**: 
   ```bash
   pip install Flask==2.3.3 PyMySQL==1.1.0
   ```

4. **Configuration**: 
   - Set environment variables:
     ```bash
     export DATABASE_HOST=localhost
     export DATABASE_USER=root
     export DATABASE_PASSWORD=<your_password>
     export DATABASE_NAME=vulnerable_db
     ```
   - Initialize database schema (if needed)

5. **Build & Run**: 
   ```bash
   flask run
   ```

6. **Access**: 
   - URL: http://localhost:5000
   - Enter username to trigger SQL Injection

**C. Vulnerability Testing**

1. **Access Point**: Navigate to http://localhost:5000/
2. **Trigger**: 
   - Enter payload like: `' OR '1'='1`
   - Submit the form
3. **Expected Behavior**: 
   - The application should return all records from the users table
   - Error messages should display SQL syntax errors for invalid input