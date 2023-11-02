from fastapi import FastAPI
from users.routes import router_user
from api.routes import router_binance

app = FastAPI(title="API")

"ROUTES"
app.include_router(router_user)
app.include_router(router_binance)