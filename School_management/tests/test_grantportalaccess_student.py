import os

from playwright.sync_api import Page

from models.applicationform_backend import applicationForm_backend
from testing.utilities import afterset


def test_grantportalaccess(page:Page, setup, download_dir=None):

    """📌Preconditions:-
    1.The user must have Administrator access to grant the portal access.
    2.The student must be successfully enrolled in the system.
    3.Student records should exist under the Student Menu.

    🧪 Test Steps:
    1.Navigate to the Student Menu in the backend/dashboard.
    2.Open the list of students.
    3.Select the desired student record.
    4.Click on the "Grant Portal Access" button.
    5.Verify the options to print Transcript and Student ID Card (General)."""



    #prconditions===========================================
    print("Creating the student....")
    Application = applicationForm_backend(page)
    student_name = Application.creatingapplicationform()

    #=========================================================
    #1.Navigate to the Student Menu in the backend/dashboard.
    #=============================================================
    print("Navigating to the Student menu.")
    page.locator("button[data-menu-xmlid='wk_school_management.student_form_menu']").click()
    page.locator("a[href='/odoo/school-student']").click()

    # ==============================================
    #2.Open the list of students.
    #3.Select the desired student record.
    # ==============================================
    print("Search the Student ans select the student...")
    page.get_by_placeholder("Search...").fill(student_name)
    page.get_by_placeholder("Search...").press("Enter")
    page.locator(".o_switch_view.o_list").click()
    page.locator("tbody.ui-sortable tr.o_data_row").click()

    #==============================================
    # 4.Click on the "Grant Portal Access" button.
    #==============================================
    print("Now clicking on the Grant Portal Access....")
    page.locator("button[name='create_related_user']").click()
    page.locator("[name='action_grant_access']").click()
    print(f"Portal Access has been granted to the {student_name}")
    page.locator(".modal-footer .btn.btn-primary:nth-child(1)").click()

    # ==============================================
    # 5.Verify the options to print Transcript and Student ID Card (General)."""
    # ==============================================

    print("Printing the Student Id card ....")
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    page.locator(".d-print-none.btn").click()
    page.locator(".o-dropdown.o-dropdown--has-parent").click()
    # Download student_id_card
    with page.expect_download() as Id_card_download_info:
        page.locator(".o-dropdown--menu-submenu .o_menu_item:last-child").click()
    Id_card_download = Id_card_download_info.value
    Id_card_path = os.path.join(download_dir, Id_card_download.suggested_filename)
    Id_card_download.save_as(Id_card_path)
    print(f"✔️ Id_card downloaded at: {Id_card_path}")

    



















