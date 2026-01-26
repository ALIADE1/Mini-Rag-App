from helpers.config import Settings, Get_Settings


class BaseController:
    def __init__(self):
        self.app_settings = Get_Settings()
