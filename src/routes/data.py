from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from ..controllers.DataController import DataController
from ..helpers.config import Get_Settings, Settings
import aiofiles
from ..models import ResponseStatus


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

    file_path = DataController().generate_unique_filename(
        original_filename=file.filename, project_id=project_id
    )

    async with aiofiles.open(file_path, "wb") as out_file:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await out_file.write(chunk)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": ResponseStatus.FILE_UPLOADED_SUCCESS.value,
        },
    )
