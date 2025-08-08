# Project 06 #AIAugustAppADay: Python Day! Keyword Extractor API

![Last Commit](https://img.shields.io/github/last-commit/davedonnellydev/ai-august-2025-06)

**📆 Date**: 08/Aug/2025  
**🎯 Project Objective**: Create an API endpoint that you can send text to, and get back main keywords (great for SEO, tagging, etc.)  
**🚀 Features**: Endpoints: /keywords (POST text); Returns: JSON: { "keywords": [...] }  
**🛠️ Tech used**: Python, Flask, OpenAI API  
**▶️ Live Demo**: *[https://ai-august-2025-06.onrender.com](https://ai-august-2025-06.onrender.com)*  

Above is just a landing page. The API should be called as a POST request to `/keywords`. As the API has bearer token authentication, you will need the correct token if you'd like to try it - email me for details at [davepauldonnelly@gmail.com](mailto:davepauldonnelly@gmail.com).  

# Project 06
## 🗒️ Summary

Python Day! This project was a great excuse to dust off my Python skills, though I spent a fair chunk of the day re-learning the mechanics and architecture of a Flask app. It’s been a few years since I last built one, so I found myself doing a lot of reading and firing questions into Cursor to refresh my memory on why Flask apps are structured the way they are.  

The project itself was simple: an API endpoint that accepts a `POST` request with text in the request body, sends that text to OpenAI’s Responses API, and returns a structured output — a string of keywords extracted for SEO purposes. Most of the core implementation came together quickly thanks to patterns I’ve been using all week, but the real time sink was revisiting some of those backend fundamentals, remembering how Python syntax works and the importance of API security/authentication. You can take a look at the basic flow diagram here: [ai-august-2025-06.drawio.png](./ai-august-2025-06.drawio.png).  

Along the way, I dusted off my Postman skills for testing the endpoint, used Render.com to host the Flask app, and experimented with Docker for the first time. Docker was a bit of a challenge — especially figuring out how to make changes and see them reflected in my dev environment — I'm keen to keep exploring it's uses!  

**Lessons learned**  
- Revisiting old skills takes time — be ready to slow down and re-learn the fundamentals before diving into code.  
- Postman remains a fantastic tool for quickly testing and iterating on API endpoints.  

**Final thoughts**  
While this wasn’t the most complex project of the challenge, it was a valuable refresher on Python, Flask and Postman, and a great opportunity to expand my toolset with Docker and Render.com.  

This project has been built as part of my AI August App-A-Day Challenge. You can read more information on the full project here: [https://github.com/davedonnellydev/ai-august-2025-challenge](https://github.com/davedonnellydev/ai-august-2025-challenge).


## Quick Start

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env.local file with your keys
   echo "OPENAI_API_KEY=your-openai-api-key-here" > .env.local
   echo "API_KEY=your-secure-api-key-here" >> .env.local
   echo "SECRET_KEY=your-flask-secret-key" >> .env.local
   ```

4. **Run the application (choose one):**
   - Flask CLI (recommended for dev):
     ```bash
     export FLASK_APP=run.py
     export FLASK_ENV=development
     flask run --host=0.0.0.0 --port=8000
     ```
   - Python directly:
     ```bash
     python run.py
     ```
   - Gunicorn (production-like):
     ```bash
     gunicorn -w 4 -b 0.0.0.0:8000 run:app
     ```

The application will be available at `http://localhost:8000`
Note: On macOS, port 5000 is often used by AirPlay Receiver. If you encounter "Address already in use" errors, use port 8000 or another available port.

## 🔧 Configuration

The application uses environment-based configuration:

- `SECRET_KEY` - Flask secret key (required)
- `FLASK_ENV` - Environment (development/testing/production)
- `LOG_LEVEL` - Logging level (DEBUG/INFO/WARNING/ERROR)
- `OPENAI_API_KEY` - Your OpenAI API key for keyword extraction
- `API_KEY` - Bearer token for API authentication

### API Endpoints

#### Keyword Extraction (Protected)
- `POST /keywords` - Extract keywords from text (requires authentication)

**Authentication:** Bearer token required in `Authorization` header
**Rate Limiting:** 10 requests per hour per IP address
**Input Formats:**
  - JSON: `{"text": "your text here"}` or `{"content": "your text here"}`
  - Raw text: Send as plain text body

**Example Request:**
```bash
curl -X POST http://localhost:8000/keywords \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is sample text for keyword extraction"}'
```

**Example Response:**
```json
{
  "keywords": ["sample", "text", "keyword", "extraction"]
}
```

#### Health Checks
- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health check with version info

#### Other Endpoints
- `POST /api/proxy` - Proxy endpoint for external API calls
- `GET /` - Welcome message

## 🔐 Authentication & Security

### Bearer Token Authentication
The `/keywords` endpoint is protected with bearer token authentication:

- **Header Format:** `Authorization: Bearer <your-api-key>`
- **Configuration:** Set `API_KEY` environment variable
- **Error Responses:** Clear JSON error messages for authentication failures

### Rate Limiting
Built-in rate limiting to prevent abuse:

- **Global Limits:** 200 requests per day, 50 per hour per IP
- **Endpoint Limits:** 10 requests per hour for `/keywords` endpoint
- **Storage:** Memory-based (resets on server restart)
- **Error Response:** HTTP 429 with JSON error message

### Error Handling
Comprehensive error handling with consistent JSON responses:

- **401 Unauthorized** - Missing or invalid bearer token
- **429 Too Many Requests** - Rate limit exceeded
- **400 Bad Request** - Invalid input data
- **500 Internal Server Error** - Server configuration or API errors

## 🎉 Deployment

### Production

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key
export API_KEY=your-secure-api-key
export OPENAI_API_KEY=your-openai-api-key
export LOG_LEVEL=WARNING
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### Docker

```bash
# Build image
docker build -t flask-starter .

# Run container
docker run -p 8000:8000 \
  -e FLASK_ENV=production \
  -e SECRET_KEY=your-secure-secret-key \
  -e API_KEY=your-secure-api-key \
  -e OPENAI_API_KEY=your-openai-api-key \
  -e LOG_LEVEL=WARNING \
  flask-starter
```

### Docker Compose

```bash
# Development (hot-reload via volume mount)
docker compose up web

# Production profile
docker compose --profile production up web-prod
```

## 📦 Developer Commands

### Tests & Coverage
```bash
pytest                      # runs tests with coverage threshold from pyproject.toml
pytest --cov=app            # explicit coverage
pytest --cov=app --cov-report=html  # HTML report in htmlcov/
```

### Code Quality
```bash
black .                     # format
black --check .             # verify formatting only
flake8 app tests            # lint
```

### Environment Setup
Create `.env.local` with your local secrets:
```bash
SECRET_KEY=dev-secret-key
FLASK_ENV=development
LOG_LEVEL=DEBUG
OPENAI_API_KEY=your-openai-api-key
API_KEY=your-secure-api-key
```

## 🧪 Testing

![CI](https://github.com/davedonnellydev/ai-august-2025-06/actions/workflows/ci.yml/badge.svg)  
*Note: Test suite runs automatically with each push/merge.*  

The test suite includes comprehensive coverage for:

- **Authentication** - Bearer token validation and error cases
- **Rate Limiting** - Configuration and decorator functionality
- **Keyword Extraction** - Input validation, OpenAI integration, error handling
- **Error Handling** - All HTTP error codes with proper JSON responses
- **API Endpoints** - All routes and their expected behaviors

**Test Coverage:** 92%+ with 31 tests covering all major functionality.

## 📜 License
![GitHub License](https://img.shields.io/github/license/davedonnellydev/ai-august-2025-06)
This project is licensed under the MIT License.
