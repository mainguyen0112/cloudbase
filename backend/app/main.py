from fastapi import FastAPI

app = FastAPI(title="CloudBase API")


@app.get("/health")
def health():
    return {"status": "ok"}