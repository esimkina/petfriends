import requests

class PetFriends:
    def __init_(self) :
        self.base_url = "https://pettriends1.herokuapp.com/"


    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self,auth_Key,filter):
        headers = {'auth_key': auth_Key['key']}
        filter = {'filter': filter}

        res = requests.get(self, self.base_url + 'api/pets', headers=headers, params=filter)
