from fastapi import FastAPI
from users.routes import router_user

app = FastAPI(title="API")

"ROUTES"
app.include_router(router_user)