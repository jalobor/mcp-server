from fastapi import FastAPI
import pkg_resources

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

@app.get("/version")
def version():
    try:
        version = pkg_resources.get_distribution("mcp").version
        return {"mcp_version": version}
    except Exception as e:
        return {"error": str(e)}
        
