# Project [00] #AIAugustAppADay: [Project name]

![Last Commit](https://img.shields.io/github/last-commit/davedonnellydev/flask-python-starter)  

**📆 Date**: *[Project build date here]*  
**🎯 Project Objective**: *[Write up any project objectives here]*  
**🚀 Features**: *[Main features for MVP]*  
**🛠️ Tech used**: *[Main tech used, including links to libraries/APIs]*  
**▶️ Live Demo**: *[https://your-demo-url.com](https://your-demo-url.com)*  
*(Link will be added after deployment)*  

**🏁 Starter repo**: [Flask Python starter](https://github.com/davedonnellydev/flask-python-starter)  

## 🗒️ Summary
**Lessons learned**  
*A little summary of learnings*  

**Blockers**  
*Note any blockers here*  

**Final thoughts**  
*Any final thoughts here*  


This project has been built as part of my AI August App-A-Day Challenge. You can read more information on the full project here: [https://github.com/davedonnellydev/ai-august-2025-challenge](https://github.com/davedonnellydev/ai-august-2025-challenge).  

## 🧪 Testing

![CI](https://github.com/davedonnellydev/flask-python-starter/actions/workflows/ci.yml/badge.svg) *[Link should be amended so that correct repo is specified]*  
*Note: Test suite runs automatically with each push/merge.*  

## Quick Start

1. **Clone and install:**  
   ```bash
   git clone https://github.com/davedonnellydev/flask-python-starter.git
   cd flask-python-starter
   npm install
   ```

2. **Create a virtual environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**  
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application:**  
   ```bash
   # Option 1: Using Flask CLI (recommended)
   FLASK_APP=run.py python -m flask run --host=0.0.0.0 --port=8000

   # Option 2: Using Python directly (alternative)
   python run.py
   ```

The application will be available at `http://localhost:8000`  
**Note**: On macOS, port 5000 is often used by AirPlay Receiver. If you encounter "Address already in use" errors, use port 8000 or another available port.  


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

1. Set environment variables:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key
export LOG_LEVEL=WARNING
```

2. Run with a production WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### Docker (Optional)

```bash
# Build image
docker build -t flask-starter .

# Run container
docker run -p 8000:8000 flask-starter
```


## 📦 Available Scripts

### Test scripts

```bash
# Run all tests (with coverage by default)
pytest

# Run tests with coverage
pytest --cov=app

# Run tests and generate HTML coverage report
pytest --cov=app --cov-report=html

# Run tests without coverage
pytest --no-cov
```
**Note**: The pytest configuration in `pyproject.toml` automatically includes coverage reporting and sets the Python path to find the `app` module.

### Code Quality

```bash
# Format code
black .

# Check code style
flake8

# Run all quality checks
black --check .
flake8
pytest
```



## 📜 License
![GitHub License](https://img.shields.io/github/license/davedonnellydev/flask-python-starter)  
This project is licensed under the MIT License.  
