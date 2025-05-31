import random
import string
from pathlib import Path

from playwright.sync_api import Page


class afterset():

    def __init__(self, page: Page):
        self.page = page



    def generate_random_email(self):
        random_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"portal_{random_name}@webkul.com"


    def generate_parent_email(self):
        parent = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"portal_{parent}@webkul.com"

    def generate_random_name(self):
        # Generate a random string with 6 characters (only letters)
        random_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"portal_{random_name}"


    def generate_mother_name(self):
        # Generate a random string with 6 characters (only letters)
        mother_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"mother_{mother_name}"

    def generate_father_name(self):
        # Generate a random string with 6 characters (only letters)
        father_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"father_{father_name}"

    def upload_profile_picture(self):
        return Path("tests/boy.png").resolve()


    def admin_login(self):
        self.page.locator(".navbar-nav.align-items-center.gap-2.flex-shrink-0 a[href='/web/login']").click()
        self.page.locator("#login").fill("admin")
        self.page.locator("#password").fill("admin")
        self.page.locator("button.btn.btn-primary").click()
        self.page.locator(".o_navbar_apps_menu").click()
        self.page.locator("a[href='/odoo/school-dashboard']").click()

    def generate_Teacher_name(self):
        # Generate a random string with 6 characters (only letters)
        random_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"teacher_{random_name}"

    def generate_Teacher_email(self):
        random_name = ''.join(random.choices(string.digits, k=3)).capitalize()
        return f"teacher_{random_name}@webkul.com"


    def create_assignment(self):

        self.page.locator("[data-menu-xmlid='wk_school_management.teacher_main_menu']").click()
        self.page.locator("[href='/odoo/teacher-grade-assignment']").click()
        self.page.locator("button.o_list_button_add").click()
        self.page.locator("#name_0").fill("Assignment")
        self.page.locator("#grade_id_0").click()
        self.page.locator("#grade_id_0_0_0").click()
        self.page.locator("#subject_id_0").click()
        self.page.locator("#subject_id_0_0_0").click()
        self.page.locator("#type_id_0").click()
        self.page.locator("#type_id_0_0_0").click()
        self.page.locator("#teacher_id_0").click()
        self.page.locator("#teacher_id_0_0_0").click()
        self.page.locator(".fa.fa-cloud-upload.fa-fw").click()
        self.page.locator("[name='approve_assignment']").click()
        self.page.locator(".modal-footer .btn.btn-primary").click()

    def student_login(self):
        self.page.locator(".navbar-nav.align-items-center.gap-2.flex-shrink-0 a[href='/web/login']").click()
        self.page.locator("#login").fill("sf.demo@web.in")
        self.page.locator("#password").fill("webkul")
        self.page.locator("button.btn.btn-primary").click()

    def teacher_login(self):
        self.page.locator(".navbar-nav.align-items-center.gap-2.flex-shrink-0 a[href='/web/login']").click()
        self.page.locator("#login").fill("teacher@web.in")
        self.page.locator("#password").fill("webkul")
        self.page.locator("button.btn.btn-primary").click()















