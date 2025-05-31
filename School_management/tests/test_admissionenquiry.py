
from playwright.sync_api import Page

from models.admissionform import Form


def test_admissionenquiry(page: Page, setup):
    form = Form(page)

    reference_number = form.create_enquiry()
    print("Application Reference Number:", reference_number)

