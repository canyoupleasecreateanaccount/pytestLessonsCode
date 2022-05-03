import requests
import pytest
from pydantic.error_wrappers import ValidationError


from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses

from src.baseclasses.response import Response


from src.schemas.computer import Human, Inventory


@pytest.mark.parametrize("status", Statuses.list())
def test_something1(status, get_player_generator):
    # print(get_player_generator.set_status(status).build())
    pass


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_something2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    # print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something3(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    # print(object_to_send)


def test_human():
    r = requests.get('https://petstore.swagger.io/v2/store/inventory')
    response = Response(r)
    response.validate(Inventory)




