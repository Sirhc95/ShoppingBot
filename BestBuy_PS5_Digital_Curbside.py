from selenium import webdriver
import time

def order():
    #VARIABLES
    addToCart = '//*[@data-version="21.0.120"]/div/div/div/button'
    checkout = '//*[@data-track="Checkout - Top"]'
    continueAsGuest = '//*[@class="button-wrap "]/button'
    email = '//*[@id="user.emailAddress"]'
    phone = '//*[@id="user.phone"]'
    confirmInfo = '//*[@class="button--continue"]/button'
    creditCardNum = '//*[@id="optimized-cc-card-number"]'
    creditExpireMonth = "//select[@name='expiration-month']"
    creditExpireYear = "//select[@name='expiration-year']"
    creditCVV = '//*[@id="credit-card-cvv"]'
    firstName ='//*[@id="payment.billingAddress.firstName"]'
    lastName = '//*[@id="payment.billingAddress.lastName"]'
    address = '//*[@id="payment.billingAddress.street"]'
    city = '//*[@id="payment.billingAddress.city"]'
    state = "//select[@id='payment.billingAddress.state']"
    zipCode = '//*[@id="payment.billingAddress.zipcode"]'
    placeOrder = '//*[@data-track="Place your Order - Contact Card"]'

    #KEYS
    #add your information here
    myFirstName = 'John'
    myLastName = 'Smith'
    myEmail = 'mail@gmail.com'
    myPhone = '9803214321'
    myAddress = '1234 Apple Lane'
    myCity = 'New York'
    myState = 'NY'
    myZipCode = '10025'
    myCreditCardNum = '4232123412341234'
    myCreditExpireMonth = '12'
    myCreditExpireYear = '2025'
    myCVV = '123'

    #ADDS PS5 TO CART AND GOES TO CHECKOUT
    clickButton(addToCart)
    driver.get('https://www.bestbuy.com/cart')
    clickButton(checkout)
    clickButton(continueAsGuest)

    #FILLS OUT SHIPPING INFO
    enterData(email, myEmail)
    enterData(phone, myPhone)
    clickButton(confirmInfo)

    #FILLS OUT PAYMENT
    enterData(creditCardNum, myCreditCardNum)
    enterData(creditExpireMonth, myCreditExpireMonth)
    enterData(creditExpireYear, myCreditExpireYear)
    enterData(creditCVV, myCVV)
    enterData(firstName, myFirstName)
    enterData(lastName, myLastName)
    enterData(address, myAddress)
    enterData(city, myCity)
    enterData(state, myState)
    enterData(zipCode, myZipCode)


    #ORDER
    clickButton(placeOrder)

def clickButton(xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        clickButton(xpath)

def enterData(field,data):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(1)
        enterData(field,data)

if __name__ == "__main__":
    driver = webdriver.Chrome("C:/Users/chris/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163')
    time.sleep(3)
    order()
