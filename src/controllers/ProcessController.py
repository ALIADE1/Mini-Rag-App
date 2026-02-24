from .BaseController import BaseController
import os


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = os.path.join(self.file_dir, project_id)

    def get_file_content(self, file_id: str):
        file_path = os.path.join(self.project_path, file_id)

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def process_file_content(
        self,
        file_content: str,
        file_id: str,
        chunk_size: int = 500,
        overlap_size: int = 50,
    ):
        if file_content is None or len(file_content) == 0:
            return None

        chunks = []
        start = 0
        content_length = len(file_content)

        while start < content_length:
            end = start + chunk_size
            chunk = file_content[start:end]
            chunks.append(
                {
                    "file_id": file_id,
                    "chunk_index": len(chunks),
                    "chunk_content": chunk,
                }
            )
            start += chunk_size - overlap_size

        return chunks
