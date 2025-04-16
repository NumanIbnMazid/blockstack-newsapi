# NewsAPI Backend

A secure, containerized FastAPI application providing token-based authentication and a suite of RESTful endpoints for news aggregation and delivery.

---

## Project Overview

This backend service offers:

- **OAuth2** authentication with JWT tokens.
    
- **Dockerized** environment for consistent deployment.
    
- **PEP-8** compliance with integrated linting tools.
    
- **Automated testing** using `pytest` and `coverage`.
    
- **Comprehensive API** with endpoints for token generation, news retrieval, and more.
    
---

## Setup Instructions

### Prerequisites

- Docker
    
- Docker Compose
    
- Unix-like shell environment (e.g., Bash)
    
### Installation Steps

1. **Clone the Repository**
    
    ```bash
    git clone https://github.com/NumanIbnMazid/blockstack-newsapi && cd blockstack-newsapi
    ```
    
2. **Configure Environment Variables**
    
    Create a `.env` file in the root directory using `env.sample`:
    
3. **Build and Run the Docker Containers**
    
    ```bash
    docker compose build && docker-compose up -d
    ```

	The application will be accessible at `http://localhost:8000`.

---

## Running Tests and Linting

A `run.sh` script is provided to automate linting and testing within the Docker container.

### Usage

```bash
chmod +x run.sh && ./run.sh
```

This script performs the following:

- **Builds** and starts the Docker containers.
    
- **Runs** `flake8` for PEP-8 compliance checks.
    
- **Executes** tests using `pytest` with coverage reporting.


---

## Docker Usage

### Building the Docker Image

```bash
docker compose build
```

### Starting the Containers

```bash
docker compose up -d
```

### Stopping the Containers

```bash
docker compose down -v
```

---

## Authentication

### Obtaining an Access Token

Send a POST request to the `/token` endpoint with your `client_id` and `client_secret`:

```bash
curl -X POST http://localhost:8000/token \   -F 'client_id=your_client_id' \   -F 'client_secret=your_client_secret'
```

Response:

```json
{
	"access_token": "your_jwt_token",
	"token_type": "bearer"
}
```

### Accessing Secured Endpoints

Include the obtained token in the `Authorization` header:

```bash
curl -H "Authorization: Bearer your_jwt_token" http://localhost:8000/protected-endpoint
```

---

## API Endpoints

A detailed FAST API provided API Documentation can be found at `http://127.0.0.1:8000/docs`.

### 1. **`POST /token`**

- **Description**: Generates a JWT access token using OAuth2 client credentials grant.​
    
- **Parameters**:
    
    - `client_id` (form data)​
        
    - `client_secret` (form data)​
        
- **Response**:
    
    - `access_token`: JWT token​
        
    - `token_type`: "bearer"​
        

### 2. **`GET /news`**

- **Description**: Retrieves a paginated list of news articles from NewsAPI.​
    
- **Headers**:
    
    - `Authorization`: Bearer token​
        
- **Query Parameters**:
    
    - `page`: Page number (optional)​
        
    - `page_size`: Number of articles per page (optional)​
        
- **Response**:
    
    - List of news articles in JSON format.​
        

### 3. **`POST /news/save-latest`**

- **Description**: Fetches the latest news from NewsAPI and saves the top 3 articles into the database.​
    
- **Headers**:
    
    - `Authorization`: Bearer token​
        
- **Response**:
    
    - Details of the saved articles in JSON format.​
        

### 4. **`GET /news/headlines/country/{country_code}`**

- **Description**: Fetches top headlines by country from NewsAPI.​
    
- **Parameters**:
    
    - `country_code`: Two-letter country code (e.g., 'us', 'de').​
        
- **Headers**:
    
    - `Authorization`: Bearer token​
        
- **Response**:
    
    - List of top headlines for the specified country in JSON format.​
        

### 5. **`GET /news/headlines/source/{source_id}`**

- **Description**: Fetches top headlines by source from NewsAPI.​
    
- **Parameters**:
    
    - `source_id`: News source identifier (e.g., 'bbc-news').​
        
- **Headers**:
    
    - `Authorization`: Bearer token​
        
- **Response**:
    
    - List of top headlines for the specified source in JSON format.​
        

### 6. **`GET /news/headlines/filter`**

- **Description**: Fetches top headlines from NewsAPI filtered by various criteria.​
    
- **Headers**:
    
    - `Authorization`: Bearer token​
        
- **Query Parameters**:
    
    - `country`: Two-letter country code (optional).​
        
    - `source`: News source identifier (optional).​
        
    - `category`: News category (e.g., 'business', 'technology') (optional).​
        
- **Response**:
    
    - List of top headlines matching the specified filters in JSON format.​
        

---

## Code Review Suggestions

To further enhance the codebase:

- **Database Integration**: Transition from SQLite storage to a robust database system like PostgreSQL for efficient data management.
    
- **Logging**: Integrate a structured logging system to facilitate debugging and monitoring.
