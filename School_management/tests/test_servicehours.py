from playwright.sync_api import Page

from testing.utilities import afterset


def test_servicehours(page:Page,setup):

    """🧪 Test Steps:
    1.Navigate to the Student Menu from the backend/dashboard.
    2.Open the "Service Hours" sub-menu.
    3.Click on "Create" or "New" to add service hours.
    4.Select the student from the dropdown.
    5.Fill in all required fields (e.g., title, hours, comments, start-time, etc.
    6.Click the "Save" button to create the service hour record."""


    login = afterset(page)
    login.admin_login()
    print("Login via Admin credentials..")


    #=============================================
    # 1.Navigate to the Student Menu from the backend/dashboard.
    #================================================
    page.locator("[data-menu-xmlid='wk_school_management.student_form_menu']").click()
    print("filling the data for service hours...")

    # =============================================
    #  2.Open the "Service Hours" sub-menu.
    # 3.Click on "Create" or "New" to add service hours.
    #4.Select the student from the dropdown.
    #5.Fill in all required fields (e.g., title, hours, comments, start-time, etc.
    #6.Click the "Save" button to create the service hour record.
    # ================================================
    page.locator("a[href='/odoo/student-service-hours']").click()
    page.locator(".o_list_button_add").click()
    page.locator("#name_0").fill("Test_service")
    page.locator("#student_id_0").click()
    page.locator("#student_id_0_0_0").click()
    page.locator("#start_time_0").fill("05/22/2025")

    page.locator("#supervisor_id_0").click()
    page.locator("#supervisor_id_0_0_0").click()
    page.locator("#total_hours_0").fill("01:00")
    page.locator(".fa-cloud-upload").click()
    page.locator("button[name='approve_service_hour']").click()
    page.locator(".modal-footer .btn.btn-primary").click()
    print("Service hours is successfully created.")






