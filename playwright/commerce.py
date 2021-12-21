from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://demo.vuestorefront.io/
    page.goto("https://demo.vuestorefront.io/")
    # Click [data-testid="menuButton"]
    page.click("[data-testid=\"menuButton\"]")
    # Click :nth-match([data-testid="categoryButton"], 2)
    page.click(":nth-match([data-testid=\"categoryButton\"], 2)")
    # Click [data-testid="categoryButton"]
    page.click("[data-testid=\"categoryButton\"]")
    # Click text=Jackets
    # with page.expect_navigation(url="https://demo.vuestorefront.io/men/tops-men/jackets-men.html"):
    with page.expect_navigation():
        page.click("text=Jackets")
    # Click :nth-match(img[alt="Montana Wind Jacket"], 3)
    # with page.expect_navigation(url="https://demo.vuestorefront.io/montana-wind-jacket.html?childSku=MJ03-XS-Black"):
    with page.expect_navigation():
        page.click(":nth-match(img[alt=\"Montana Wind Jacket\"], 3)")
    # Click [aria-label="Select color Green"]
    page.click("[aria-label=\"Select color Green\"]")
    # assert page.url == "https://demo.vuestorefront.io/montana-wind-jacket.html?childSku=MJ03-XS-Green"
    # Click [aria-label="Select size M"]
    page.click("[aria-label=\"Select size M\"]")
    # assert page.url == "https://demo.vuestorefront.io/montana-wind-jacket.html?childSku=MJ03-M-Green"
    # Click [data-testid="addToCart"]
    page.click("[data-testid=\"addToCart\"]")
    # Click [data-testid="notificationAction1"]
    page.click("[data-testid=\"notificationAction1\"]")

    # insert to scroll up
    page.mouse.wheel(0, -1000)

    # Click [data-testid="openMicrocart"]
    page.click("[data-testid=\"openMicrocart\"]")
    # Click [data-testid="subscribeSubmit"]
    # with page.expect_navigation(url="https://demo.vuestorefront.io/checkout"):
    with page.expect_navigation():
        page.click("[data-testid=\"subscribeSubmit\"]")
    # Click input[name="first-name"]
    page.click("input[name=\"first-name\"]")
    # Fill input[name="first-name"]
    page.fill("input[name=\"first-name\"]", "steve")
    # Press Tab
    page.press("input[name=\"first-name\"]", "Tab")
    # Fill input[name="last-name"]
    page.fill("input[name=\"last-name\"]", "steve")
    # Press Tab
    page.press("input[name=\"last-name\"]", "Tab")
    # Fill input[name="email-address"]
    page.fill("input[name=\"email-address\"]", "steve@email.com")
    # Click [data-testid="personalDetailsSubmit"]
    page.click("[data-testid=\"personalDetailsSubmit\"]")
    # assert page.url == "https://demo.vuestorefront.io/checkout#shipping"
    # Click input[name="street-address"]
    page.click("input[name=\"street-address\"]")
    # Fill input[name="street-address"]
    page.fill("input[name=\"street-address\"]", "main")
    # Click input[name="apartment-number"]
    page.click("input[name=\"apartment-number\"]")
    # Fill input[name="apartment-number"]
    page.fill("input[name=\"apartment-number\"]", "15")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "Los Angeles")
    # Press Tab
    page.press("input[name=\"city\"]", "Tab")
    # Fill input[name="state"]
    page.fill("input[name=\"state\"]", "CA")
    # Press Tab
    page.press("input[name=\"state\"]", "Tab")
    # Fill input[name="zip-code"]
    page.fill("input[name=\"zip-code\"]", "93242")

    time.sleep(1)
    # Click input[name="phone-number"]
    page.click("input[name=\"phone-number\"]")
    # Fill input[name="phone-number"]
    page.fill("input[name=\"phone-number\"]", "9999999999")
    # Click [data-testid="shippingSubmit"]
    page.click("[data-testid=\"shippingSubmit\"]")
    # assert page.url == "https://demo.vuestorefront.io/checkout#payment"
    # Click text=Copy address data from shipping
    page.click("text=Copy address data from shipping")

    time.sleep(1)
    
    # Click [data-testid="paymentSubmit"]
    page.click("[data-testid=\"paymentSubmit\"]")
    # assert page.url == "https://demo.vuestorefront.io/checkout#orderReview"
    # Click text=I agree to Terms and conditions
    page.click("text=I agree to Terms and conditions")
    # Click [data-testid="orderReviewSubmit"]
    page.click("[data-testid=\"orderReviewSubmit\"]")
    # Click h2:has-text("Order confirmation")
    page.click("h2:has-text(\"Order confirmation\")")
    
    # got xpath through inspection (this is a dynamic value)
    order = page.query_selector('//*[@id="checkout"]/div[2]/div/div/div/div[1]/p[2]').text_content()
    print(order)

    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)