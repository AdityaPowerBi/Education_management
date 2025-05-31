import pytest
from playwright.sync_api import Page

from models.applicationform_backend import applicationForm_backend
from tests.test_admissionenquiry import test_admissionenquiry


@pytest.fixture
def setup(page: Page):
    page.goto("http://192.168.5.139:8018/?db=School_management", wait_until="load")
    page.wait_for_load_state("networkidle")







