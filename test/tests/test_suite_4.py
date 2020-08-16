import pytest
import allure


@pytest.fixture
def product_creation(catalog_page):
    """
        TEARDOWN for tests that create products.
        Removes the product created from the app Catalog
    """
    yield
    catalog_page.remove_created_products_from_catalog(keyword='item')


@allure.title('Items are added into a cart. Qty badge on the cart icon displays correct information')
def test_add_items_to_the_cart(main_page):
    """
        verifies if product items can be added to a cart,
        and that the qty number on the cart badge increases by one as a new item added
    """
    for item in main_page.popular_products_locators(qty=3):
        main_page.click_on(item)
        # the click on locator function is being passed to the wrapper 'is_cart_qty_badge_number_grew'
        # that returns True if the qty number on the badge increased by 1 after the click, or False otherwise
        assert main_page.is_cart_qty_badge_number_grew(main_page.click_on)(main_page.add_to_cart_button) is True
        main_page.open()


@allure.title('Items can be removed from a cart')
def test_remove_all_items_from_cart(main_page):
    """
        verifies if product items can be removed from a cart,
        and the qty number on the cart badge displays nothing after all items were removed
    """
    main_page.open()
    main_page.open_the_cart()
    main_page.remove_all_items_in_cart()
    main_page.open()
    assert main_page.cart_badge_number == 0


@allure.title('Creation of a product with certain fields followed by its presence in the root catalog')
def test_product_creation(catalog_page, product_creation):
    """
        verifies creation of a product in the catalog page,
        and verifies if the product created appeared in the root list in the Catalog page
    """
    catalog_page.click_on(catalog_page.add_new_product_button)
    name_of_product_created = catalog_page.create_product()
    assert catalog_page.is_product_in_the_root_catalog(name_of_product_created) is True
