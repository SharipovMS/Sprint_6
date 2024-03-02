from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    '''поле имя'''
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    '''поле фамилия'''
    second_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    '''поле адрес'''
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    '''выпадающий список с метро'''
    metro = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    '''контейнер со списком метро'''
    contaner_metro = (By.CLASS_NAME, "select-search__options")
    '''класс с текстом, станции'''
    meto_text = (By.CLASS_NAME, "Order_Text__2broi")
    '''поле телефон'''
    phone_number = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    '''кнопка далее'''
    button_next = (By.XPATH, "//button[text()='Далее']")
    '''поле ввода даты'''
    date = (By.XPATH, "//input[contains(@placeholder,\'Когда\')]")
    '''ввод даты'''
    date_input = (By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--today")
    '''поле периода владения'''
    period = (By.CLASS_NAME, 'Dropdown-placeholder')
    '''ввод периода владения'''
    period_input = (By.XPATH, "//div[(text() = 'двое суток')]")
    '''поле выбора цвета самоката'''
    color_black = (By.ID, 'black')
    color_grey = (By.ID, 'grey')
    '''поле для комментария доставке'''
    comment_for_delivery = (By.XPATH, "//input[@class = 'Input_Input__1iN_Z Input_Responsible__1jDKN']")
    '''кнопка заказать'''
    button_order = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]')
    '''кнопка подтверждения заказа'''
    button_yep_order = (By.XPATH, "//button[text()='Да']")
    '''проверка статуса'''
    status = (By.XPATH, ".//*[contains(@class,'Order_ModalHeader')]")
    '''Кнопка для прокрутки до нижнейк кнопки Заказа'''
    zakaz_button_scroll = (By.XPATH ,"//div[@class= 'Home_FinishButton__1_cWm']")
    '''Кнопка заказа низ'''
    zakaz = (By.CLASS_NAME, 'Button_Button__ra12g')
    '''проверочный локатор что заказ успешно оформлен'''
    order_is_processed = (By.CSS_SELECTOR, 'div.Order_ModalHeader__3FDaJ div.Order_Text__2broi')
