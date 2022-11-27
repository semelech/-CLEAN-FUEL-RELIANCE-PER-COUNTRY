import pytest
from Invoice import Invoice
@pytest.fixture()
def products():
    products = {'pen':{'qnt':10, 'unit_price':3.75,'discount':5},
                'Notebook':{'qnt':5,'unit_price':7.5, 'discount':10}}
    return products
@pytest.fixture()
def invoice():
      invoice = Invoice()
      return invoice
def test_CanCalculateTotalImpurePrice(products):
      invoice =Invoice()
      invoice.totalImpurePrice(products)
      assert invoice.totalImpurePrice(products)== 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCaculatetotalCount(invoice, products):
        invoice.totalCount(products)
        assert invoice.totalCount(products) == 15

def test_CanCaculatetotalRoughImpurePrice(invoice, products):
            invoice.totalRoundImpurePrice(products)
            assert invoice.totalRoundImpurePrice(products) == 75


def test_CanCaculatetotalUnitPrice(invoice, products):
    invoice.totalunitprice(products)
    assert invoice.totalunitprice(products) == 11.25

def test_CanCaculatetotalSalesTax(invoice, products):
    invoice.totalSalesTax(products)
    assert invoice.totalSalesTax(products) == 3.29
