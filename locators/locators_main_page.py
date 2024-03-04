from selenium.webdriver.common.by import By

class LocatorsMainPage:

    '''кнопка принятия условия о сборе куки.'''
    cookie_button = [By.ID, 'rcc-confirm-button']

    '''ссылка "Самокат"'''
    logo_link_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    '''ссылка на Яндекс лого'''
    logo_link_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    '''кнопка заказать в шапке сайта.'''
    order_button_main = [By.XPATH, "//button[@class = 'Button_Button__ra12g']"]

    '''кнопка "ЗАКАЗАТЬ" в сердине сайта'''
    order_button_low = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp]']"]

    '''Страница дзена'''
    dzen_page = [By.CLASS_NAME, 'e522eddb9']

    # перый вопрос
    QUESTION_1 = [By.ID, 'accordion__heading-0']
    # второй вопрос
    QUESTION_2 = [By.ID, 'accordion__heading-1']
    # третий вопрос
    QUESTION_3 = [By.ID, 'accordion__heading-2']
    # четвертый вопрос
    QUESTION_4 = [By.ID, 'accordion__heading-3']
    # пятый вопрос
    QUESTION_5 = [By.ID, 'accordion__heading-4']
    # шестой вопрос
    QUESTION_6 = [By.ID, 'accordion__heading-5']
    # седьмой вопрос
    QUESTION_7 = [By.ID, 'accordion__heading-6']
    # восьмой вопрос
    QUESTION_8 = [By.ID, 'accordion__heading-7']

    # перый ответ
    ANSWER_1 = [By.ID, 'accordion__panel-0']
    # второй ответ
    ANSWER_2 = [By.ID, 'accordion__panel-1']
    # третий ответ
    ANSWER_3 = [By.ID, 'accordion__panel-2']
    # четвертый ответ
    ANSWER_4 = [By.ID, 'accordion__panel-3']
    # пятый ответ
    ANSWER_5 = [By.ID, 'accordion__panel-4']
    # шестой ответ
    ANSWER_6 = [By.ID, 'accordion__panel-5']
    # седбмой ответ
    ANSWER_7 = [By.ID, 'accordion__panel-6']
    # восьмой ответ
    ANSWER_8 = [By.ID, 'accordion__panel-7']


