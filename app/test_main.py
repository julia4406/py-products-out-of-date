import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_one_product_outdated(products_list: list) -> None:
    date_for_check, result = (datetime.date(2022, 2, 2), ["duck"])
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date_for_check
        assert outdated_products(products_list) == result


def test_couple_products_outdated(products_list: list) -> None:
    date_for_check = datetime.date(2022, 3, 2)
    result = ["salmon", "chicken", "duck"]
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date_for_check
        assert outdated_products(products_list) == result


def test_no_products_outdated(products_list: list) -> None:
    date_for_check, result = (datetime.date(2022, 2, 1), [])
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date_for_check
        assert outdated_products(products_list) == result
