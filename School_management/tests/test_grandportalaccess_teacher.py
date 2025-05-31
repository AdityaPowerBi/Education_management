import os

from playwright.sync_api import Page

from models.teacher import teacher
from testing.utilities import afterset


def test_grandportalaccess_teacher(page:Page,setup):



    """    🧪 Test Steps:
    1.The teacher profile is creating in the system.
    2.Click on the "Grant Portal Access" button.
    3.Verify the availability of options to:
    4.Print Teacher Badge
    5.View/Print Time Off Summary
    6.Print Teacher Resume"""



    #==============================================
    # 1.The teacher profile is creating in the system.
    #=================================================
    print("Teacher profile is creating...")
    teacher_application = teacher(page)
    teacher_application.create_teacher()

    # ==============================================
    # 2.Click on the "Grant Portal Access" button.
    # ==============================================
    print("Grant the protal Access..")
    page.locator("[name='action_create_user']").click()
    page.locator("footer.modal-footer button[special='save']").click()

    # ==============================================
    #3.Verify the availability of options to:
    #4.Print Teacher Badge
    #5.View/Print Time Off Summary
    #6.Print Teacher Resume
    # ==============================================

    print("Print the badges for the teacher.")
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    page.locator(".d-print-none.btn").click()
    page.locator(".o-dropdown.o-dropdown--has-parent").click()
    # Download student_id_card
    with page.expect_download() as Print_badge_info:
        page.locator(".o-dropdown--menu-submenu .o_menu_item:first-child").click()
    Print_badge = Print_badge_info.value
    Print_badge_path = os.path.join(download_dir, Print_badge.suggested_filename)
    Print_badge.save_as(Print_badge_path)
    print(f"✔️ Id_card downloaded at: {Print_badge_path}")

    print("Badge is successfully printed")




















