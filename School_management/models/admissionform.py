import re
from pathlib import Path
from playwright.sync_api import Page, expect
from testing.utilities import afterset  # this should NOT import anything back from this file


class Form:
    def __init__(self, page: Page):
        self.page = page

    def create_enquiry(self) -> str:
        email = afterset
        mail = email.generate_random_email(self)
        student_name = email.generate_random_name(self)
        mother_name = email.generate_mother_name(self)
        father_name = email.generate_father_name(self)
        image_path = email.upload_profile_picture(self)
        parent_email = email.generate_parent_email(self)

        self.page.locator("ul#top_menu a[href='/OnlineRegistration']").click()
        print("Click on the Admission enquiry form")
        expect(self.page).to_have_url(re.compile(".*/OnlineRegistration$"))
        self.page.locator("#name").fill(student_name)
        print(f"Student name is : {student_name}")
        self.page.locator("//input[@value='male']").click()
        print("Selecting the gender :male")
        self.page.locator("input#dob").fill("2000-02-26")
        print("Filling all required field , Grade , email , phno , Disablities")
        self.page.locator("#grade_id").select_option("1")
        self.page.locator("#email").fill(mail)
        self.page.locator("input#phone").fill("3698521470")
        self.page.locator("select#disability").select_option("no")

        print("Filing the parents details.....")
        self.page.locator("input#m_name").fill(mother_name)
        self.page.locator("input#father_name").fill(father_name)
        self.page.locator("input[name='mothers_contact']").fill("3698521470")
        self.page.locator("input[name='fathers_contact']").fill("8521479630")
        self.page.locator("#parent_email").fill(parent_email)
        self.page.locator("input[name='mothers_occupation']").fill("Mother_occupation")
        self.page.locator("input[name='fathers_occupation']").fill("Father_occupation")
        self.page.set_input_files("input[type='file']", Path(image_path).resolve())
        self.page.locator("button#application_submit").click()

        reference_number = self.page.locator("div.main p strong").text_content()
        print(f"Reference number is: {reference_number}")
        return reference_number




