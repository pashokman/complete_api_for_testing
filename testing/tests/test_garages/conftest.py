from testing.classes.garage import Garage
from testing.classes.house import House
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup():
    user = User()
    user.create_user()
    user.auth()
    house = House()
    garage = Garage()
    yield user, house, garage


@pytest.fixture()
def setup_not_auth():
    user = User()
    user.create_user()
    house = House()
    garage = Garage()
    yield user, house, garage
