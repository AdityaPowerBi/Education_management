from playwright.sync_api import Page, expect

from testing.utilities import afterset


def test_assignmentsubmission_byadmin(page:Page,setup):


    """🧪 Test Steps:
    1.For Mass Assignment Submission:
    2.Navigate to the Student Menu in the backend.
    3.Open the Assignment submenu.
    4.Select multiple assignments that are in the "New" state.
    5.Click on the "Action" button.
    6.Choose "Submit Mass Student Assignment".
    7.Fill in all required details, such as:
    Attachment type
    Assignment file
    Submission notes (if any)
    8.Submit the assignments."""

    login = afterset(page)
    login.admin_login()

    #======================================
    #1.For Mass Assignment Submission:
    #2.Navigate to the Student Menu in the backend.
    #3.Open the Assignment submenu.
    #============================================
    print("Clicking on the Assignment menu")
    page.locator("[data-menu-xmlid='wk_school_management.student_form_menu']").click()
    page.locator("[data-menu-xmlid='wk_school_management.student_assignment_menu']").click()
    print("Select the Assignment")
    page.locator("button.o_searchview_dropdown_toggler").click()
    page.locator(".o_filter_menu span.dropdown-item").nth(0).click()
    page.locator("button.o_searchview_dropdown_toggler").click()

    # ======================================
    # 4.Select multiple assignments that are in the "New" state.
    # 5.Click on the "Action" button.
    # 6.Choose "Submit Mass Student Assignment".
    # ============================================

    try:
        page.locator(".o-checkbox.form-check.d-flex.m-0").click()
        print("Clicked on the checkbox")

        page.locator("button.btn.btn-secondary.o-dropdown.dropdown-toggle").click()
        print("Clicked on the Action button")

        page.locator("div.dropdown-menu span.dropdown-item:nth-child(5)").click()
        print("Clicked on the Submit button")

        validation_error = page.locator(".text-prewrap").text_content()
        print(f"Validation Message: {validation_error}")

        page.locator(".o-default-button").click()
        print("Assignment is successfully submitted")

    except Exception as e:
        print("An error occurred:", e)















