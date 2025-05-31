from playwright.sync_api import Page

from models.admissionform import Form
from testing.utilities import afterset

#Verify by confirming the Admission enquiry form in the Application section(Application refernce getting
# from admission enquiry form)

def test_confirmapplicationform(page:Page, setup):


       """Test Steps:


          1.Log in as an internal user with access to the Applications menu.
          2.Navigate to Applications > Application List.
          3.Search for the Application using the Application Reference Number.
          4.Open the Application record.
          5.Verify the Application is in "New" state.
          6.Click the Confirm button."""

       login = afterset(page)


       """📝 Preconditions:
       An Application Enquiry should be submitted from the frontend.
       The Application Reference Number should be noted and saved."""

       form = Form(page)
       print("Preparing preconditions: creating the admission enquiry form.")
       reference_number = form.create_enquiry()

       #============================================
       #1.Log in as an internal user with access to the Applications menu.
       #===========================================

       login.admin_login()
       print("Logging in with admin credentials to confirm the application form...")
       # ============================================
       # 2.Navigate to Applications > Application List.
       # ===========================================
       page.wait_for_selector("a[href='/odoo/school-application']", state="visible")
       print("Navigating to the application form...")
       page.locator("a[href='/odoo/school-application']").click()

       # ============================================
       #  3.Search for the Application using the Application Reference Number.
       # ===========================================
       application_number = page.get_by_placeholder("Search...")
       print("Searching for the submitted application form in the admin panel...")
       application_number.fill("")
       application_number.fill(reference_number)
       application_number.press("Enter")


       #===============================================
       # 4.Open the Application record.
       # 5.Verify the Application is in "New" state.
       #===============================================
       page.wait_for_selector("//tbody[@class='ui-sortable']/tr[1]", state="visible")
       page.locator("//tbody[@class='ui-sortable']/tr[1]").click()
       print("Opening the details of the selected application form...")

       #=================================================
       #6.Click the Confirm button.
       #=================================================
       page.locator("[name='confirm_application']").click()
       page.locator("div.modal-content button.btn.btn-primary").click()
       print("Submitting confirmation for the application form...")















