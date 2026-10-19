from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "OK",
        "server": "MCP Test Server"
    }

@app.get("/health")
def health():
    return {
        "healthy": True
    }
  
