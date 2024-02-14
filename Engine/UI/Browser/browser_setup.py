# browser_setup.py

import os
from playwright.sync_api import sync_playwright

class BrowserUtils:
    def __init__(self):
        self.playwright = sync_playwright().start()
        app_data_path = os.getenv("LOCALAPPDATA")
        user_data_path = os.path.join(app_data_path, 'Chromium\\User Data\\Default')

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_path, 
            channel='chrome', 
            headless=False, 
            args=['--start-maximized'],
            no_viewport=True
        )
        self.page = self.context.new_page()

    def teardown(self):
        self.context.close()
        self.playwright.stop()
