from playwright.sync_api import Page

from testing.utilities import afterset


class teacher:
    def __init__(self, page: Page):
        self.page = page

    def create_teacher(self):
        login = afterset(self.page)
        login.admin_login()
        teacher_name = login.generate_Teacher_name()
        teacher_email = login.generate_Teacher_email()





        self.page.locator("[data-menu-xmlid='wk_school_management.teacher_main_menu']").click()
        self.page.locator("[href='/odoo/school-employees']").click()
        self.page.locator(".o_control_panel_main_buttons .o-kanban-button-new").click()
        self.page.locator("#name_0").fill(teacher_name)
        self.page.locator("#job_title_0").fill("teacher")
        self.page.locator("#work_email_0").fill(teacher_email)
        self.page.locator("#is_supervisor_0").click()
        self.page.locator("#department_id_0").click()
        self.page.locator("#department_id_0_0_0").click()
        self.page.locator("button.o_form_button_save").click()


        return teacher_name






