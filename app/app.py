from fastapi import FastAPI

app = FastAPI()

# Simple GET API
@app.get("/")
def home():
    return {"message": "I am Atharva from LetsLearnGit!"}

# Another GET API with a parameter
@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

# Simple POST API to receive JSON data
@app.post("/submit")
def submit_data(data: dict):
    return {"received_data": data, "message": "Data received successfully!"}
