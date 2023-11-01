"""API entrypoint"""

import json

from fastapi import FastAPI

api = FastAPI(
    title="API for Twinoid forums static archive",
    description="This API allows you to access the static archive of the Twinoid forums.",
    version="0.1.0",
    contact={
        "name": "Evian"
    },
    license_info={
        "name": "MIT",
    },
)

@api.get("/api/v1/")
async def root():
    return {"data": "The API is working!"}

@api.get("/api/v1/forums/")
async def forums():
    return {
        "data": [
        {
            "name": "ambassade",
            "uri": "/api/v1/forums/ambassade/"
        }
    ]}

@api.get("/api/v1/forums/{name}/")
async def forum(name: str):
    return {"data": json.loads(open(f"../data/fr/mush/{name}.json", "rb").read())}