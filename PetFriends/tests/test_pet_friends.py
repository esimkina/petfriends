from gettext import install
#pip install pytest==7.4.0
from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_velid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filtere=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0