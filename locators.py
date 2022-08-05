# Главная страница
class MainLocators:
    button_login = "//button[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт
    menu_item_account = "//p[text()='Личный Кабинет']"  # пункт меню Личный Кабинет
    menu_item_constructor = "//p[text()='Конструктор']"  # пункт меню Конструктор
    menu_item_logo = "//div[@class='AppHeader_header__logo__2D0X2']"  # пункт меню логотип
    title_menu_buns = "//span[text()='Булки']"  # вкладка Булки
    title_menu_sauces = "//span[text()='Соусы']"  # вкладка Соусы
    title_menu_fillings = "//span[text()='Начинки']"  # вкладка Начинки
    button_submit = "//button[text()='Оформить заказ']"  # кнопка Оформить заказ
    button_logout = "//button[text()='Выход']"  # кнопка Выход
    title_buns = "//h2[text()='Булки']"  # заголовок раздела Булки
    title_sauces = "//h2[text()='Соусы']"  # заголовок раздела Соусы
    title_fillings = "//h2[text()='Начинки']"  # заголовок раздела Начинки


# Страница регистрации
class RegLocators:
    input_name = "(//input[@name='name'])[1]"  # поле ввода Имя // оторвать руки за такой нейминг
    input_email = "(//input[@name='name'])[2]"  # поле ввода Email // оторвать руки за такой нейминг
    input_password = "//input[@name='Пароль']"  # поле ввода Пароль
    button_submit_reg = "//button[text()='Зарегистрироваться']"  # кнопка Зарегистрироваться
    link_login = "//a[@href='/login']"  # ссылка Войти
    text_invalid_password = "//p[text()='Некорректный пароль']"  # текст с ошибкой Некорректный пароль


# Страница авторизации
class AuthLocators:
    input_email = "//input[@name='name']"  # поле ввода Email // оторвать руки за такой нейминг
    button_submit_login = "//button[text()='Войти']"  # кнопка Войти
    link_register = "//a[@href='/register']"  # ссылка на страницу регистрации
    link_forgot_password = "//a[@href='/forgot-password']"  # ссылка на страницу восстановления пароля
