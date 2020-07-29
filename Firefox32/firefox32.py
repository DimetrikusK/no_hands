from openpyxl import load_workbook
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

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
    driver = webdriver.Firefox()
    driver.get('http://egisso.ru/site/')
    test_page = driver.find_element_by_link_text(click_me)
    # driver.refresh()
    try:
        test_page.click()
        driver.refresh()
        load_time = driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart);")
        driver.close()
        return str(load_time)
    except WebDriverException:
        driver.close()
        return "There was an ERROR"

res = []
for link in click_me:
    res.append(ft_load_time(link))

wb = load_workbook('C:\\Users\\admin\\Desktop\\test\\info10.XLSX')
sheet = wb['Время отклика']
sheet['F8'] = res[0]
sheet['F16'] = res[1]
sheet['F24'] = res[2]
sheet['F32'] = res[3]
sheet['F40'] = res[4]
sheet['F48'] = res[5]
sheet['F56'] = res[6]
sheet['F64'] = res[7]
sheet['F72'] = res[8]
wb.save('C:\\Users\\admin\\Desktop\\test\\info10.XLSX')
