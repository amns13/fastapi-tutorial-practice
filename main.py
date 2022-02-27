from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# A different app. Both cam run in parallel.
altapp = FastAPI()


@altapp.get("/")
async def root():
    return {"message": "Hello World from alt"}
