import os

from playwright.sync_api import Page

from testing.utilities import afterset


def test_populateclass(page:Page,setup):


    """🧪 Test Steps:
    1.Log in to the system using student credentials.
    2.Navigate to the Assignments section.
    3.Locate an assignment that is in "To-Do" status.
    4.Open the assignment and click on the "Submit Assignment" button.
    5.Fill in all required submission details, such as:
    6.Select Attachment Type
    7.Upload corresponding Attachment
    8.Click Submit.
"""

    login = afterset(page)

    #=========================================
    #1.Log in to the system using student credentials.
    #==============================================
    login.student_login()

    print("Submitting the Assignment...")

    # =========================================
    # 2.Navigate to the Assignments section.
    # ==============================================
    page.locator("[href='/my/assignments']").click()
    print("Click on the Assignment")

    # =========================================
    # 3.Locate an assignment that is in "To-Do" status.
    # ==============================================
    page.locator("#dropdownMenuLink").click()
    print("Click on the search ..")

    # =========================================
    #4.Open the assignment and click on the "Submit Assignment" button.
    # ==============================================
    page.locator("#search_bar_dropdown #state").click()
    print("Selecting the state..")

    # =========================================
    # 5.Fill in all required submission details, such as:
    # 6.Select Attachment Type
    # ==============================================
    page.select_option("#state_selection",value='new')

    #============================================
    #7.Upload corresponding Attachment
    #8.Click Submit.
    #=============================================
    file_path = os.path.abspath("tests/file.pdf")  # assuming you're in project root

    # Click assignment row
    page.locator("tr.clickable-assignment").click()
    print("Select the Assignment")

    # Open the modal
    page.locator("button[data-bs-target='#submit_assignment_modal']").click()
    print("Clicking on the Assignment submission")

    # Wait for modal to appear fully
    page.wait_for_selector("textarea#description", timeout=5000)

    # Fill in the description
    page.locator("textarea#description").fill("Test Assignment")
    print("Filling the details..")

    # Click the first attachment type radio button
    page.locator("#attachment_type_id label:first-child").click()

    # Wait for file input to be visible and enabled
    file_input = page.locator("input#attachement")
    file_input.wait_for(state="visible", timeout=5000)
    file_input.set_input_files(file_path)

    # Submit the assignment
    page.locator("button.submit_assignment").click()
    print("Assignment is submit")

    













