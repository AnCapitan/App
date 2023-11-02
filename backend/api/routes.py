from fastapi import APIRouter, Depends
from binance.spot import Spot
from config.config import BINANCE_API, BINANCE_SECRET_KEY


client = Spot(api_key=BINANCE_API, api_secret=BINANCE_SECRET_KEY)
router_binance = APIRouter()


