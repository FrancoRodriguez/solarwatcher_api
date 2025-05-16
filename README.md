# 🌞 SolarWatcher API

A FastAPI project to fetch and serve solar event data using NASA's APIs.

🔧 Built with:

- **FastAPI** for high-performance APIs
- **HTTPX** for async HTTP requests
- **JWT** for authentication and authorization
- **Docker** for containerization
- **pytest** for testing
- **flake8**, **black**, and **isort** for linting

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FrancoRodriguez/solarwatcher_api.git
cd solarwatcher_api
```

### Set Up Environment Variables
Create a .env file in the root directory with the following content:

```bash
ADMIN_USERNAME=admin
ADMIN_PASSWORD=supersecret
NASA_API_KEY=your_nasa_api_key_here
JWT_ALGORITHM = "HS256"
SECRET_KEY = any_secret_key_to_use
TOKEN_EXPIRATION_TIME = 30
```

## 🔐 Get a NASA API Key

1. Go to https://api.nasa.gov
2. Fill out the form to request your API key (it's free).
3. You will receive your key via email or directly in the browser.
4. Add it to your .env file under NASA_API_KEY.

## 🐳 Run the App

```bash
make app
```

## 🔐 Authentication

 - This project uses JWT (JSON Web Tokens) for secure authentication.
 - Login endpoint issues JWT tokens on successful authentication.

## 🧪 Testing the API with Swagger UI
1. Open your browser and go to: http://localhost:8000/docs
2. You will see all the available endpoints and their schemas.
3. To test a protected endpoint:
    - First, use the /login endpoint to obtain a JWT token by providing valid credentials.
    - Copy the token from the response.
    - Click the Authorize button (top right in Swagger UI).
    - In the value field, enter: Bearer <your_token_here>
    - Click Authorize and then close the modal.
4. Now you can interact with secured endpoints directly from Swagger UI.

### Demo Video

[![Watch the demo](https://img.youtube.com/vi/z7n9mJzFve4/0.jpg)](https://youtu.be/z7n9mJzFve4)



## 🧱 Database and Migrations
❌ Not required. This project does not use a database or migrations.

## 🧹 Code Quality

### Run Linters
```bash
make app-linter
```

### Auto-fix Lint Issues
```bash
make app-linter-fix
```

Make sure pyproject.toml includes:
```toml
[tool.black]
line-length = 120

[tool.isort]
line_length = 120
```

## ✅ Run Tests
```bash
make tests
```
Test files are located in app/tests.

## 🗂 Project Structure
```bash
app/
├── auth/               # Authentication logic (JWT implementation)
├── dependencies.py     # FastAPI dependencies
├── i18n.py             # Translations/locales
├── routers/            # Route handlers
├── services/           # Business logic (e.g. NASA data fetcher)
├── tests/              # Unit and integration tests
├── main.py             # FastAPI entry point
```

### 🛠 Useful Make Commands
```bash
make app              # Start app with Docker
make app-linter       # Run linters
make app-linter-fix   # Auto-fix lint issues
make tests            # Run all tests
```

## 📦 Requirements
 - Docker & Docker Compose
 - Make (optional but recommended)

 ## 📫 Contact
For questions or feedback, feel free to open an issue or contact me.