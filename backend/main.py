import uvicorn
from config.settings import app



if __name__ == '__main__':
    config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True, host="0.0.0.0")
    server = uvicorn.Server(config)
    server.run()