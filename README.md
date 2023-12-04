# URL Shortener

This is a URL shortener application built with FastAPI and DynamoDB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Java Runtime Environment (JRE) for running DynamoDB Local
- AWS account, for non-local Database Connections
- Python 3.6 or later
- FastAPI
- Uvicorn, an ASGI server to serve your application
- PynamoDB, a Pythonic interface for Amazon DynamoDB
- Pytest, for running tests
- Docker, for containerization
- Optional: Postman, for endpoint testing

You can install the Python dependencies by running:

```bash
pip install fastapi uvicorn pynamodb pytest
```

## Running the Application

### Running Locally

1. Start Local Database Connection

    Navigate to the dynamodb_local_latest directory in your Documents folder and run the following command to start DynamoDB Local:

    ```bash
    java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
    ```

2. Start the Server

    In a separate terminal, run the following command within the url_shortener/app directory to start the Uvicorn server:

    ```bash
    uvicorn main:app --reload
    ```

### Running with AWS & Docker

1. Build Docker Image

    If not already built, build the docker image by navigating to app directory within project and running:

     ```bash
    docker build . -t url_project
    ```

2. Run Docker Container

    After building your image, you can now run your Docker conainer by running:

    ```bash
    docker run -e AWS_ACCESS_KEY_ID=your_access_key_id -e AWS_SECRET_ACCESS_KEY=your_secret_key --rm -it -p 80:80/tcp url_project:latest
    ```

    Now, you can navigate to http://0.0.0.0:80/ in your web browser to see the application in action. Postman can be used to utilize endpoints.

### Running the Tests

You can run the tests for the application by navigating to url_shortener/app directory and running:

```bash
pytest url_tests.py -vv -s
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
