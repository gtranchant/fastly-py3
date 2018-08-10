import requests
import json

class Fastly:
    def __init__(self, host='api.fastly.com'):
        self.host = host
        self.https_host = 'https://%s' % host
        self.key = None
        self.requests = requests.Session()

    # private function for print json pretty
    def __print_json_pretty(self, json_txt):
        parsed_json = json.loads(json_txt)
        print(json.dumps(parsed_json, indent=4, sort_keys=False))

    # private function call GET Fastly's API
    def __GET(self, path, params=None):
        return self.requests.get(self.https_host + path, params=params)

    # private function call POST Fastly's API
    def __POST(self, path, data):
        return self.requests.post(self.https_host + path, data=data)

    # private function call POST Fastly's API
    def __PUT(self, path, params=None):
        return self.requests.put(self.https_host + path, params=params)

    # set key to auth in fastly api service
    def authenticate_by_key(self, key):
        self.key = key
        self.requests.headers.update( {'Fastly-Key': key } )

    def print_json_pretty(self, json):
        self.__print_json_pretty(json_txt=json)

    # call api /service : List Services
    def get_services(self):
        return self.__GET(path='/service')

    #call api /service/<service_id>/details : List detailed information on a specified service
    def get_service_details(self, service_id):
        return self.__GET(path='/service/%s/details' % service_id)

    # call api /service/search : Get a specific service by name
    def get_service_search(self, service_name):
        return self.__GET(path='/service/search', params={ 'name': service_name })

    # call api /service/<service_id>/version/<version>/backend : List all backends for a particular service and version 
    def get_backends(self, service_id, version):
        return self.__GET(path='/service/%s/version/%s/backend' % (service_id, version))

    # call api /service/<service_id>/version/<version>/backend/<name> : Get the backend for a particular service and version
    def get_backend_name(self, service_id, version, name):
        r = self.__GET(path='/service/%s/version/%s/backend/%s' % (service_id, version, name))
        return r.status_code, r.json()

    def update_backend(self, service_id, version, backend_name, params):
        return self.__PUT(path='/service/%s/version/%s/backend/%s' % (service_id, version, backend_name), params=params)

