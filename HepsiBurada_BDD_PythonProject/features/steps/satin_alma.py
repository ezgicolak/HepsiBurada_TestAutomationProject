import time
import random
# behave ve selenium kütüphaneleri
from behave import *
from selenium import webdriver
# chrome driver extensions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
# firefox driver extensions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
# edge driver extensions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# html object detect extension
from selenium.webdriver.common.by import By
# expected conditions extension
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# yakalanan test objects kütüphaneleri
from object_repository.home_page import header_area as ha, products_area as pa, filter_area as fa
from object_repository import login_page as lp
from object_repository import product_page as pp


@given('"{tarayici}" uzerinde "{url}" acilir')
def step_impl(context, tarayici, url):
    try:
        if tarayici == "Chrome":
            chromeOptions = ChromeOptions()
            chromeOptions.add_argument("start-maximized")
            chromeOptions.add_argument("--disable-notifications")
            chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
            chromeOptions.add_argument("--disable-extensions")
            chromeOptions.add_experimental_option('useAutomationExtension', False)
            chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            chromeOptions.add_experimental_option("prefs", prefs)
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chromeOptions)
            context.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        elif tarayici == "Firefox":
            firefoxOptions = FirefoxOptions()

            context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                               options=firefoxOptions)
            context.driver.maximize_window()
        elif tarayici == "Edge":
            edgeOptions = EdgeOptions()
            edgeOptions.add_argument("start-maximized")
            edgeOptions.add_argument("--disable-notifications")
            edgeOptions.add_argument("--disable-blink-features=AutomationControlled")
            edgeOptions.add_argument("--disable-extensions")
            edgeOptions.add_experimental_option('useAutomationExtension', False)
            edgeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            edgeOptions.add_experimental_option("prefs", prefs)
            context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                            options=edgeOptions)
        else:
            chromeOptions = ChromeOptions()
            chromeOptions.add_argument("start-maximized")
            chromeOptions.add_argument("--disable-notifications")
            chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
            chromeOptions.add_argument("--disable-extensions")
            chromeOptions.add_experimental_option('useAutomationExtension', False)
            chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            chromeOptions.add_experimental_option("prefs", prefs)
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chromeOptions)
        context.driver.get(url)
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('"{username}" ve "{password}" ile giris yapilir')
def step_impl(context, username, password):
    try:
        wait = WebDriverWait(context.driver, 20)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.myAccount)))
        element.click()
        if EC.element_to_be_selected((By.XPATH, lp.myAccount)):
            element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.login)))
            element.click()
        else:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.myAccount)))
            element.click()
            element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.login)))
            element.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.userName)))
        element.send_keys(username)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.btnLogin)))
        element.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.password)))
        element.send_keys(password)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, lp.btnEmailSelect)))
        element.click()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('"{urun}" isimli urun aranir')
def step_impl(context, urun):
    try:
        wait = WebDriverWait(context.driver, 20)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, ha.searchBox)))
        element.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, ha.searchBox)))
        element.send_keys(urun)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, ha.searchBoxButton)))
        element.click()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Fiyat araligi "{min}" ve "{max}" olarak secilir')
def step_impl(context, min, max):
    try:
        wait = WebDriverWait(context.driver, 20)

        element = wait.until(EC.presence_of_element_located((By.XPATH, fa.min)))
        element.click()
        element.send_keys(min)

        element = wait.until(EC.presence_of_element_located((By.XPATH, fa.max)))
        element.click()
        element.send_keys(max)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, fa.moriaButton)))
        element.click()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('En alttan rastgele urun secilir')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 20)
        selectedItem = 1

        productList = wait.until(EC.visibility_of_all_elements_located((By.XPATH, pa.productList)))
        productListSize = len(productList)
        if productListSize > 3:
            randomNumber = random.randint(0, 3)
            selectedItem = productListSize - randomNumber
        time.sleep(3)
        productList[selectedItem - 1].click()
    except:
        context.driver.close()
        assert False, "Test Failed"


@then('En dusuk puanli saticidan urun sepete eklenir')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 20)
        # Açılan yeni sekmeye geçiş işlemi
        newTab = context.driver.window_handles[1]
        context.driver.switch_to.window(newTab)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, pp.merchants)))
        element.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, pp.merchantListSort)))
        element.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, pp.merchantListSort)))
        element.click()

        merchantsList = wait.until(EC.visibility_of_all_elements_located((By.XPATH, pp.merchantList)))

        addCart = WebDriverWait(merchantsList[2], 20).until(EC.element_to_be_clickable((By.XPATH, pp.addToCartButton)))
        addCart.click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, pp.popupCloser)))
        element.click()

        time.sleep(3)
        cartControl = wait.until(EC.presence_of_element_located((By.XPATH, pp.addToCartMessage)))

        wait.until(EC.visibility_of_element_located((By.XPATH, pp.addToCartMessage)))

        time.sleep(3)
        assert True, cartControl.text == 'Ürün sepetinizde'

        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test Failed"
