from enum import Enum


class ResponseStatus(Enum):

    FILE_VALIDATED_SUCCESS = "file_validated_success"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOADED_SUCCESS = "file_uploaded_success"
    FILE_UPLOADED_FAILURE = "file_upload_failure"
