# FastAPI Application

This is a FastAPI application template designed to demonstrate how to build a RESTful API using FastAPI. The application integrates middleware for CORS handling and a custom token-based authentication mechanism.

## Table of Contents

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+
- pip

### Steps

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-repo/your-project.git
   cd your-project
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:

   ```sh
   touch .env
   ```

   Populate the `.env` file with the necessary environment variables (see [Environment Variables](#environment-variables) section).

## Environment Variables

The `.env` file should contain the following environment variables:

```env
# Example Environment Variables
DATABASE_URL=mongodb://localhost:27017/mydatabase
SECRET_KEY=your_secret_key
```

## Usage

1. **Run the FastAPI application**:

   ```sh
   fastapi run app/main.py --reload
   ```

2. **Access the API documentation**:

   Open your browser and navigate to `http://127.0.0.1:8000/docs` for the interactive Swagger documentation or `http://127.0.0.1:8000/redoc` for ReDoc.

## Testing

To run the tests, use the `pytest` command:

```sh
pytest
```

Ensure you have set the `PYTHONPATH` correctly so that the tests can find the `app` module.

## Project Structure

```plaintext
your_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── chats/
│   │   ├── __init__.py
│   │   ├── chats_router.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── mongodb.py
├── tests/
│   ├── __init__.py
│   ├── middlewares/
│   │   ├── test_auth.py
├── .env
├── requirements.txt
└── README.md
```

## Routes

### Chats

- **To be defined** based on `chats_router.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.