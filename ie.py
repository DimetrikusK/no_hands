import time
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from openpyxl import load_workbook

click_me = ["Сервисы для поставщиков и потребителей информации",
            "Новости",
            "Социальный калькулятор",
            "Кабинет поставщика информации",
            "Кабинет органа, назначающего меры социальной поддержки",
            "Личный кабинет гражданина",
            "Кабинет аналитика",
            "Репозиторий документов ЕГИССО",
            "Обратная связь"]


def ft_load_time(click_me):
    driver = webdriver.Ie("IEDriverServer.exe")
    driver.get('http://egisso.ru/site/')
    test_page = driver.find_element_by_link_text(click_me)
    try:
        test_page.click()
        time.sleep(5)
        load_time = driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart);")
        driver.close()
        return str(load_time)
    except UnexpectedAlertPresentException:
        driver.close()
        return "There was an ERROR"


res = []
for link in click_me:
    res.append(ft_load_time(link))

wb = load_workbook('info10.XLSX')
sheet = wb['Время отклика']
sheet['D8'] = res[0]
sheet['D16'] = res[1]
sheet['D24'] = res[2]
sheet['D32'] = res[3]
sheet['D40'] = res[4]
sheet['D48'] = res[5]
sheet['D56'] = res[6]
sheet['D64'] = res[7]
sheet['D72'] = res[8]
wb.save('info10.XLSX')
