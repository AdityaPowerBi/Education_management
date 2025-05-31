from playwright.sync_api import Page

from testing.utilities import afterset


def test_assignmentsubmission_byadmin(page:Page,setup):

    login = afterset(page)
    login.admin_login()

    print("Clicking on the Assignment menu")
    page.locator("[data-menu-xmlid='wk_school_management.student_form_menu']").click()
    page.locator("[data-menu-xmlid='wk_school_management.student_assignment_menu']").click()

    page.locator("button.o_searchview_dropdown_toggler").click()
    page.locator(".o_filter_menu span.dropdown-item").nth(1).click()
    page.locator("button.o_searchview_dropdown_toggler").click()

    print("Select the Assignment")
    page.locator(".o-checkbox.form-check.d-flex.m-0").click()
    print("Click on the Action button")
    page.locator("button.btn.btn-secondary.o-dropdown.dropdown-toggle").click()
    print("Click on the Submit button")
    page.locator("div.dropdown-menu span.dropdown-item:nth-child(6)").click()
    validation_error = page.locator(".text-prewrap").text_content()
    print(validation_error)
    page.locator(".o-default-button").click()



