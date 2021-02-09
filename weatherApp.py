from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def usage():
    return {"Usage" : "Call with /weather"}

@app.get("/weather")
async def weahter():
    weatherStr = await getWeather()
    return json.loads(weatherStr)

async def getWeather():
    weather = open("weather", "r")
    weatherStr = weather.readline()
    weather.close()
    return weatherStr
