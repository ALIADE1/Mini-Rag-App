from fastapi import APIRouter, FastAPI, Depends
import os
from ..helpers.config import Get_Settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def base_root(app_settings: Settings = Depends(Get_Settings)):

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "message": "Hello All!",
        "app_name": app_name,
        "app_version": app_version,
    }
