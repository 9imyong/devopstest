from fastapi import FastAPI


app = FastAPI(title="DevOps test API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello, good!"}


@app.get("/healthz")
def healthz():
    return {"status": "ok"}