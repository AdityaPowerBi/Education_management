import os

from playwright.sync_api import Page

from models.admissionform import Form
from models.applicationform_backend import applicationForm_backend
from testing.utilities import afterset


def test_enrollmentform(page:Page , setup):



      """"📌 Preconditions:
      The student must be successfully enrolled in the system with a valid enrollment record.


          🧪 Test Steps:
          1.Navigate to the Enrollment section from the dashboard or student profile.
          2.Locate and open the enrollment form for the enrolled student.
          3.Observe the current stage (should be in "Draft").
          4.Click on the "Start Now" button to begin the enrollment process.
          5.Verify that the stage changes to "In Progress", and an enrollment number is generated.
          6.Click to print the enrollment form.
          7.Click to print the report card (if applicable).
          8.Check the option to generate fee slips for the enrolled student"""

      Student_creation = applicationForm_backend(page)
      student_name = Student_creation.creatingapplicationform()


      #===============================================
      #1.Navigate to the Enrollment section from the dashboard or student profile.
      #===============================================

      page.locator("a[href='/odoo/school-enrollment']").click()

      # ===============================================
      #2.Locate and open the enrollment form for the enrolled student.
      #3.Observe the current stage (should be in "Draft")
      # ===============================================
      page.get_by_placeholder("Search...").fill(student_name)
      page.get_by_placeholder("Search...").press("Enter")
      page.locator("tbody.ui-sortable tr:nth-child(1)").click()
      status = page.locator("button.o_arrow_button_current").text_content()
      assert status == "Draft", f"Expected status to be 'Draft', but got '{status}'"
      print(f"Status of enrollment file is : {status}")



      # ===============================================
      # 4.Click on the "Start Now" button to begin the enrollment process.
      # 5.Verify that the stage changes to "In Progress", and an enrollment number is generated.
      # ===============================================
      page.locator("div.o_statusbar_buttons .btn.btn-primary").click()
      page.locator(".modal-footer .btn-primary").click()
      status1 = page.locator("button[data-value='progress']").text_content().strip()
      assert status1 == "In Progress", f"Expected status to be 'Confirmed', but got '{status1}'"
      print(f"Status of enrollment file changed from {status} to {status1}")


      # ===============================================
      # 6.Click to print the enrollment form.
      # 7.Click to print the report card (if applicable).
      # ===============================================
      # Setup download directory
      download_dir = os.path.abspath("downloads")
      os.makedirs(download_dir, exist_ok=True)

      # Click the print dropdown
      page.locator(".d-print-none.btn").click()
      page.locator(".o-dropdown.o-dropdown--has-parent").click()

      # Download Enrollment
      with page.expect_download() as enrollment_download_info:
            page.locator(".o-dropdown--menu-submenu .o_menu_item:first-child").click()
      enrollment_download = enrollment_download_info.value
      enrollment_path = os.path.join(download_dir, enrollment_download.suggested_filename)
      enrollment_download.save_as(enrollment_path)
      print(f"✔️ Enrollment downloaded at: {enrollment_path}")

      # Again click to reopen the dropdown before second download
      page.locator(".d-print-none.btn").click()
      page.locator(".o-dropdown.o-dropdown--has-parent").click()

      # Download Report Card
      with page.expect_download() as report_download_info:
            page.locator(".o-dropdown--menu-submenu .o_menu_item:last-child").click()
      report_download = report_download_info.value
      report_path = os.path.join(download_dir, report_download.suggested_filename)
      report_download.save_as(report_path)
      print(f"✔️ Report Card downloaded at: {report_path}")





