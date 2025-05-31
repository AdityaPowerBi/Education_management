from pathlib import Path

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from testing.utilities import afterset


# Verify by creating application-form from backend

""" Test Steps:
        1.Navigate to the Application section in the backend.
        2.Click on the New button to create a fresh application record.
        3.Fill in all the required fields with valid data (e.g., student name, contact info, class, etc.).
        4.Click on the Save button."""


class applicationForm_backend:
    def __init__(self, page: Page):
        self.page = page

    def creatingapplicationform(self):




        login = afterset(self.page)
        login.admin_login()
        student_name = login.generate_random_name()
        email = login.generate_random_email()
        father_name = login.generate_father_name()
        mother_name = login.generate_mother_name()
        image_path = login.upload_profile_picture()
        parent_email = login.generate_parent_email()

        self.page.wait_for_selector("a[href='/odoo/school-application']", state="visible")
        self.page.locator("a[href='/odoo/school-application']").click()

    #==================================================
    #1.Navigate to the Application section in the backend.
    #2.Click on the New button to create a fresh application record
    #===================================================
        self.page.locator("button.btn.btn-primary").click()
        self.page.locator("#student_name_0").fill(student_name)
        print(student_name)

    #======================================================
    # 3.Fill in all the required fields with valid data (e.g., student name, contact info, class, etc.)
    #======================================================
        self.page.locator("#email_0").fill(email)
        self.page.locator("#parent_email_0").fill(parent_email)
        self.page.locator("#phone_0").fill("1236547890")
        self.page.locator("#dob_0").fill("01/01/2025")
        self.page.locator("#grade_id_0").click()
        self.page.locator("#grade_id_0_0_0").click()
        print("Filling all the required details...")

        self.page.locator("#father_name_0").fill(father_name)
        self.page.locator("#fathers_contact_0").fill("258963611470")
        self.page.locator("#fathers_occupation_0").fill("IT")

        self.page.locator("#mother_name_0").fill(mother_name)
        self.page.locator("#mothers_contact_0").fill("2589632586")
        self.page.locator("#mothers_occupation_0").fill("Homemaker")

        self.page.set_input_files("input[type='file']", Path(image_path).resolve())

    #=============================================
    # 4.Click on the Save button
    #=============================================
        self.page.locator("button.o_form_button_save").click()
        print("Student Application is Successfully Saved")

#=============================================================================================================
# Verify the student enrollment form for the confirmed application form

        """🧪 Test Steps:
                1.Navigate to the relevant confirmed application.
                2.Click on the "Enroll Now" button.
                3.Click on "Create a New Student".
                4.Click on the "Enroll" button.
                5.Fill in all required details:
                  Select Session
                  Select Academic Year (based on selected session)
                6.Add the Grade/Standard.
                7.Add the Subject(s) corresponding to the selected grade.
                8.Click on the Save button."""



    #======================================================
    # 1.Navigate to the relevant new application.
    #======================================================
        self.page.locator(".o_statusbar_buttons .btn.btn-primary").click()
        self.page.locator(".modal-footer .btn-primary").click()
        print(f"Confirming the Application form of : {student_name}")
        self.page.wait_for_selector("button[data-value='confirm']", timeout=5000)
        status = self.page.locator("button[data-value='confirm']").text_content().strip()
        assert status == "Confirmed", f"Expected status to be 'Confirmed', but got '{status}'"

    #============================================================
    #2.Click on the "Enroll Now" button.
    #3.Click on "Create a New Student".
    #4.Click on the "Enroll" button.
    #============================================================
        print("Enrolled the Student")
        self.page.locator("button.bg-success").click()
        self.page.locator("button.btn-success").click()

    # ============================================================
    # 5.Fill in all required details:
    #             Select Session
    #             Select Academic Year (based on selected session)
    #           6.Add the Grade/Standard.
    # ============================================================
        self.page.locator("#session_id_0").click()
        self.page.locator("#session_id_0_0_0").click()
        self.page.locator("#academic_year_id_0").click()
        self.page.locator("#academic_year_id_0_0_0").click()
        print("Adding the session , Academic years")

    #=============================================================
    #7.Add the Subject(s) corresponding to the selected grade.
    # 8.Click on the Save button.
    #===============================================================
        print("Selecting the Subject According to the select grade")
        self.page.locator("//button[@name='add_subjects']").click()
        self.page.locator("//button[@name='add_subject_wizard']").click()
        print("Student is successfully enrolled.")
        return student_name





















