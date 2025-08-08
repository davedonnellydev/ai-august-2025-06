# Project 06 #AIAugustAppADay: Python Day! Keyword Extractor API

![Last Commit](https://img.shields.io/github/last-commit/davedonnellydev/ai-august-2025-06)

**📆 Date**: 08/Aug/2025
**🎯 Project Objective**: Create an API endpoint that you can send text to, and get back main keywords (great for SEO, tagging, etc.)
**🚀 Features**: Endpoints: /keywords (POST text); Returns: JSON: { "keywords": [...] }
**🛠️ Tech used**: Python, Flask, OpenAI API
**▶️ Live Demo**: *[https://your-demo-url.com](https://your-demo-url.com)*
*(Link will be added after deployment)*

## 🗒️ Summary
**Lessons learned**
*A little summary of learnings*

**Blockers**
*Note any blockers here*

**Final thoughts**
*Any final thoughts here*


This project has been built as part of my AI August App-A-Day Challenge. You can read more information on the full project here: [https://github.com/davedonnellydev/ai-august-2025-challenge](https://github.com/davedonnellydev/ai-august-2025-challenge).

## 🧪 Testing

![CI](https://github.com/davedonnellydev/ai-august-2025-06/actions/workflows/ci.yml/badge.svg)
*Note: Test suite runs automatically with each push/merge.*

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

3. **Run the application (choose one):**
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

### API Endpoints
#### Health Checks

- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health check with version info

#### Proxy

- `POST /api/proxy` - Proxy endpoint for external API calls

#### Root

- `GET /` - Welcome message

## 🎉 Deployment

### Production

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key
export LOG_LEVEL=WARNING
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### Docker (Optional)

```bash
# Build image
docker build -t flask-starter .

# Run container
docker run -p 8000:8000 \
  -e FLASK_ENV=production \
  -e SECRET_KEY=your-secure-secret-key \
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
pytest
pytest --cov=app
pytest --cov=app --cov-report=html
```
The pytest configuration in `pyproject.toml` sets coverage thresholds and paths.

### Code Quality
```bash
black .
black --check .
flake8 app tests
```



## 📜 License
![GitHub License](https://img.shields.io/github/license/davedonnellydev/ai-august-2025-06)
This project is licensed under the MIT License.
