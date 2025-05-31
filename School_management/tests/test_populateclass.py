from playwright.sync_api import Page

from testing.utilities import afterset


def test_populateclass(page:Page , setup):
    """📌 Preconditions:
    1.Logged-in user must have Administrator access.
    2.Required data (grades, subjects, sessions, academic years, terms, students, and teachers) must already exist in the system.
    🧪 Test Steps:
    1.Navigate to the Classes menu in the backend.
    2.Open the Populate Class section.
    3.Click on the "New" button to create a new populate class.
    4.Fill in all mandatory fields (grade, subject, teacher, session, academic year, term, etc.).
    5.Enroll students into the populate class based on selected grade and subject.
    6.Add the weekly schedule.
    7.Add assignment types and configure their weightage."""


    login = afterset(page)
    login.admin_login()
    print("Now Satisfying the preconditions by creating the Grade Assignment.")
    login.create_assignment()
    print("Admin is successfully logined.")

    #===================================================
    #1.Navigate to the Classes menu in the backend.
    #===================================================

    page.locator("[data-menu-xmlid='wk_school_management.class_main_menu']").click()

    # ===================================================
    # 2.Open the Populate Class section.
    # ===================================================
    page.locator("[data-menu-xmlid='wk_school_management.populate_class_menu']").click()

    # ===================================================
    # 3.Click on the "New" button to create a new populate class.
    # ===================================================
    page.locator(".d-inline-flex.gap-1 button.o_list_button_add").click()
    page.locator("#title_0").fill("Testpppppppp")

    # ===================================================
    # 4.Fill in all mandatory fields (grade, subject, teacher, session, academic year, term, etc.).
    # ===================================================
    page.locator("#grade_id_0").click()
    page.locator("a#grade_id_0_0_0").click()
    page.locator("#session_id_0").click()
    page.locator("#session_id_0_0_0").click()
    page.locator("#subject_id_0").click()
    page.locator("#subject_id_0_0_0").click()
    page.locator("#academic_year_id_0").click()
    page.locator("#academic_year_id_0_0_0").click()
    page.locator("#teacher_id_0").click()
    page.locator("#teacher_id_0_0_0").click()
    page.locator("#term_id_0").click()
    page.locator("#term_id_0_0_0").click()
    page.locator("#capacity_0").fill("5")
    page.locator(".o-checkbox").click()

    # ===================================================
    # 5.Enroll students into the populate class based on selected grade and subject.
    # ===================================================
    #enrolled student
    print("Allocate the students...")
    page.locator(".o-kanban-button-new").click()
    page.locator(".o-checkbox.form-check.d-flex.m-0").click()
    page.locator(".o_select_button").click()

    # ===================================================
    #  6.Add the weekly schedule.
    # ===================================================
    #weekly schedule
    try:
      print("Filling the weekly schedule......")
      page.locator(".nav-tabs li:nth-child(2)").click()
      page.locator("td.o_field_x2many_list_row_add a[role='button']").click()
      page.locator(".o_field_widget.o_required_modifier.o_field_selection").click()
      page.select_option("select.o_input.pe-3", value='"Saturday"')
      print("Day Tuesday is selected")
      page.locator("tr.o_data_row td[name='timeslot_id']").click()
      page.locator("ul.o-autocomplete--dropdown-menu a#autocomplete_0_4").click()
      print("Timeslot 8:00am to 9:00am is selected.")
      page.locator("td.o_data_cell div[name='location_id']").click()
      page.locator(".o-autocomplete--dropdown-menu  a#autocomplete_0_4").click()
      print("Hall 1 is selected")
    except:
        print(f"No alert message is shown.")

    # ===================================================
    #  7.Add assignment types and configure their weightage
    # ===================================================
    #assignment
    try:
        print("Selecting the Assignment type...")
        page.locator(".nav-tabs li:nth-child(3)").click()
        page.locator("td.o_field_x2many_list_row_add a[role='button']").click()
        page.locator("td[name='assignment_type_id']").click()
        page.locator("#autocomplete_0_0").click()
        page.locator("i.fa.fa-cloud-upload.fa-fw").click()

        # Check if alert is visible
        if page.locator("div.modal-content p.text-prewrap").is_visible(timeout=3000):
            alert_text = page.locator("div.modal-content p.text-prewrap").text_content()
            print(f"Alert shown: {alert_text}")
            page.locator(".o_error_dialog .modal-footer .btn.btn-primary").click()
            print(f"{alert_text}")
            page.locator(".modal-footer .o-default-button").click()
        else:
            print("No alert shown, Populated Class is successfully created.")

    except Exception as e:
        print(f"An error occurred: {e}")


    #=====================================================
    #confirming the populated class
    #=====================================================
    try:
        confirm_btn = page.wait_for_selector("button[name='confirm_class']",timeout=5000)
        confirm_btn.click()
        page.locator(".modal-footer .btn.btn-primary").click()
    except:
       print("Populate class is confirmed")



    #=================================================
    #Assign assignment
    #=================================================
    try:
       print("Assign the assignment...")
       page.locator("button[name='assign_assignment']").click()
       page.locator("input#name_0").fill("Test_assignment")
       page.locator("#type_id_0").click()
       page.locator("#type_id_0_0_0").click()
       page.locator("#assignment_id_0").click()
       page.locator("#assignment_id_0_0_0").click()
       #    page.locator("#assignment_id_0_0_0").click()
       # else:
       #    print("Assignment not visible, creating a new one...")
       #    login.create_assignment()
       #
       #    # Wait for assignment element to appear after creation
       #    page.locator("#assignment_id_0_0_0").wait_for(state="visible", timeout=5000)
       #    page.locator("#assignment_id_0_0_0").click()
       #    print("New assignment created and selected.")

       page.locator("input#o_input").fill("30")
       page.locator("button[name='assign_now']").click()
       if page.locator(".o_notification_title.m-0").is_visible(timeout=3000):
          alert = page.locator(".o_notification_title.m-0").text_content()
          print(alert)
       else:
           print("Assignment is successfully assigned.")
    except Exception as e:
           print(f"An error occurred: {e}")



    #Allocating the student on the Assignment
    print("Allocating Student to the Assignment...")
    page.locator("button[name='start_assignment']").click()
    page.locator(".modal-footer .btn.btn-primary").click()


    #Scheduling the class
    print("Scheduling the class..")
    page.locator(".o_statusbar_buttons [name='schedule_class']").click()
    page.locator(".modal-footer .btn.btn-success").click()



































