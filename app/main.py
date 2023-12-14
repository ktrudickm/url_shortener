from fastapi import FastAPI
from app.api.api_handlers import router


app = FastAPI()

app.include_router(router)

# Run the server with: uvicorn main:app --reload
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)