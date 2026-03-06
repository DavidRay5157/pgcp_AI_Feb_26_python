from fastapi import FastAPI

app = FastAPI()   # this is fastapi object after import



@app.get("/")
def greet():
    return "welcome to my app"




