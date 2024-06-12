from fastapi import FastAPI

# fastapi intense
app = FastAPI()

@app.get("/")
def home():
    return {'message':"Hii"}