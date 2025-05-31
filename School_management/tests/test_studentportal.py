from playwright.sync_api import Page

from testing.utilities import afterset


def test_studentportal(page:Page,setup):

    """🧪 Test Steps:
    1.Log in using valid student credentials."""



    login = afterset(page)
    login.student_login()


    student_name = page.locator(".sidebar-title.fw-bold").text_content()
    print(f"name of the student : {student_name}")

    enrollment_number = page.locator("div.d-flex.flex-column.col-lg-8.p-0.m-0 span:nth-child(2)").text_content()
    print(f"enrollment number is : {enrollment_number}")

    academic_year = page.locator(".col-7 div.text-center:nth-child(2)").text_content()
    print(f"academic year :{academic_year}")

    grade = page.locator(".col-5 div.text-center:nth-child(2)").text_content()
    print(f"grade is : {grade}")

    dashboard_menus = page.locator(".ms-2")
    all_texts = dashboard_menus.all_text_contents()

    for text in all_texts:
        print(text)



















