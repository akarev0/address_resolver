
from fastapi import FastAPI, status


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def health_check():
    """Simple health check"""