from fastapi import APIRouter, FastAPI, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from controllers.DataController import DataController
from helpers.config import Get_Settings, Settings

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(Get_Settings),
):
    is_valid, result = DataController().validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": is_valid, "details": result},
        )
