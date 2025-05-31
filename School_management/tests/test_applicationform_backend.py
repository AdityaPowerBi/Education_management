from playwright.sync_api import Page

from models.applicationform_backend import applicationForm_backend


def test_applicationform1(page:Page,setup):

    application = applicationForm_backend(page)
    application.creatingapplicationform()




