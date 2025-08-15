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

## Running the Application/Setup

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

### Running with AWS & Docker Locally

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

## Usage

Typer was used to build out the CLI for this project. Below are the available commands to use the app.

#### List all URLs

To display a list of all shortened URLs:

```bash
python3 cli.py list-urls
```

#### Shorten a URL

To shorten a url, a long url must always be provided. The short url is optional - if omitting a short url, just omit the 'short url' altogether from the command.

```bash
python3 cli.py shorten 'long url' 'short url'
```

#### Lookup a URL

To retrieve the long URL associated with a short URL:

```bash
python3 cli.py lookup 'short url'
```

#### Delete a URL

To delete a short URL and its associated long URL:

```bash
python3 cli.py delete 'short url'
```

#### Note

Ensure that the Docker container is running before using the CLI commands.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
