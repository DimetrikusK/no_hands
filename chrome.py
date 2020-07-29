from selenium import webdriver
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
    driver = webdriver.Chrome()
    driver.get('http://egisso.ru/site/')
    test_page = driver.find_element_by_link_text(click_me)
    # driver.refresh()
    test_page.click()
    # time.sleep(5) # - не влияет на load time
    load_time = driver.execute_script(
        "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart);")
    driver.close()
    return str(load_time)


res = []
for link in click_me:
    res.append(ft_load_time(link))

wb = load_workbook('info10.XLSX')
sheet = wb['Время отклика']
sheet['C8'] = res[0]
sheet['C16'] = res[1]
sheet['C24'] = res[2]
sheet['C32'] = res[3]
sheet['C40'] = res[4]
sheet['C48'] = res[5]
sheet['C56'] = res[6]
sheet['C64'] = res[7]
sheet['C72'] = res[8]
wb.save('info10.XLSX')
