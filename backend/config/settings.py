from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.routes import router_user
from api.routes import router_binance
from tasks.routes import router_task
from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("RUN")
    yield
    print("STOP")




app = FastAPI(title="API", lifespan=lifespan)

origins = [
    "http://127.0.0.1:3000",
    "http://172.18.0.1:33834",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


"ROUTES"
app.include_router(router_user, tags=["users"])
app.include_router(router_binance, tags=["binance"])
app.include_router(router_task, tags=["tasks"])