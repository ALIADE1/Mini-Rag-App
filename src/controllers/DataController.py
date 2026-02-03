from .BaseController import BaseController
from .projectcontroller import ProjectController
from fastapi import UploadFile
from ..models import ResponseStatus
import os
import re


class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):
        try:
            if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
                return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value

            # Determine uploaded file size safely from the underlying file object
            uploaded_file = file.file
            uploaded_file.seek(0, os.SEEK_END)
            size = uploaded_file.tell()
            uploaded_file.seek(0)

            if size > self.app_settings.MAX_FILE_SIZE_MB * 1024 * 1024:
                return False, ResponseStatus.FILE_SIZE_EXCEEDED.value

            return True, ResponseStatus.FILE_VALIDATED_SUCCESS.value
        except Exception as e:
            return False, str(e)

    def generate_unique_filename(self, original_filename: str, project_id: str) -> str:
        random_file_name = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_File_name(original_filename)

        new_file_path = os.path.join(
            project_path, random_file_name + "." + cleaned_file_name.split(".")
        )

        while os.path.exists(new_file_path):
            random_file_name = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_file_name + "." + cleaned_file_name.split(".")[-1],
            )

        return new_file_path

    def get_clean_File_name(self, original_filename: str):
        cleaned_file_name = re.sub(r"[^a-zA-Z0-9]", "_", original_filename)
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
