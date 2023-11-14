# URL Shortener

This is a URL shortener application built with FastAPI and DynamoDB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Java Runtime Environment (JRE) for running DynamoDB Local
- Python 3.6 or later
- FastAPI
- Uvicorn, an ASGI server to serve your application
- PynamoDB, a Pythonic interface for Amazon DynamoDB
- Pytest for running the tests

You can install the Python dependencies by running:

```bash
pip install fastapi uvicorn pynamodb pytest
```

## Running the Application

1. Start Local Database Connection

Navigate to the dynamodb_local_latest directory in your Documents folder and run the following command to start DynamoDB Local:

```bash
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

2. Start the Server

Run the following command to start the Uvicorn server:

```bash
uvicorn main:app --reload
```


3. Run the Tests

You can run the tests for the application by running:

```bash
pytest url_tests.py -vv -s
```


Now, you can navigate to http://localhost:8000 in your web browser to see the application in action. Postman can be used to utilize endpoints.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
