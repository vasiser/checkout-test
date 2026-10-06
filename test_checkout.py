from playwright.sync_api import Page, expect

def test_successful_checkout(page: Page):

    # Login
    page.goto("https://www.saucedemo.com/")
    # WORKS TOO - switched to data-test for standard approach
    # page.get_by_role("textbox", name="Username").fill("standard_user")
    # page.get_by_role("textbox", name="Password").fill("secret_sauce")
    # page.get_by_role("button", name="Login").click()
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # Add two items
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")

    # Switch to cart
    page.locator('[data-test="shopping-cart-link"]').click()

    # Verify 2 items
    cart_items = page.locator('[data-test="inventory-item-name"]')
    expect(cart_items).to_have_text([
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light"
        ]
    )

    # Remove one item
    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
    expect(cart_items).to_have_text("Sauce Labs Backpack")

    # Go to checkout
    page.locator('[data-test="checkout"]').click()

    # Fill form
    page.locator('[data-test="firstName"]').fill("Alex")
    page.locator('[data-test="lastName"]').fill("Moore")
    page.locator('[data-test="postalCode"]').fill("54321")
    page.locator('[data-test="continue"]').click()

    # Checkout
    page.locator('[data-test="finish"]').click()

    # Assert checkout text and take screenshot
    expect(page.locator('[data-test="complete-header"]')).to_contain_text(
        "THANK YOU FOR YOUR ORDER", ignore_case=True)
    page.screenshot(path="screenshots/confirmation.png", full_page=True)
