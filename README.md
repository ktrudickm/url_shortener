# URL Shortener

To start:
- start local database connection by running
`dynamodb_local_latest java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`

- start server for app
`uvicorn main:app --reload`

- to run tests, also then run
 `pytest url_tests.py -vv -s`