import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_find_button_basket(browser):
    browser.get(link)
    assert browser.find_element_by_tag_name("button"), "The button not found"

    #time.sleep(30)
