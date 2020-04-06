#!/usr/bin/env python3

import requests
import json
import os
import configparser


configFile = '/etc/dehydrated/credentials.conf'
if not os.path.isfile(configFile):
    cfgfile = open(configFile, 'w')
    Config = configparser.ConfigParser()
    Config.add_section('openprovider')
    Config.set('openprovider', 'api', 'https://api.openprovider.eu/v1beta')
    Config.set('openprovider', 'username', 'change_me')
    Config.set('openprovider', 'password', 'change_me')
    Config.set('openprovider', 'sourceip', '0.0.0.0')
    Config.write(cfgfile)
    cfgfile.close()
    print("Edit %s for a working script." % configFile)
    exit()


def OPToken():

    config = configparser.ConfigParser()
    config.read(configFile)
    api = config.get('openprovider', 'api')
    username = config.get('openprovider', 'username')
    password = config.get('openprovider', 'password')

    # api = "https://api.openprovider.eu/v1beta"
    # username = os.environ['OPENPROVIDER_API_USERNAME']
    # password = os.environ['OPENPROVIDER_API_PASSWORD']
    # sourceip = "0.0.0.0"
    postdata = {"username": username, "password": password, "ip": '0.0.0.0'}

    resp = requests.post(url=api + "/auth/login", data=json.dumps(postdata))

    if (resp.ok):
        data = json.loads(resp.text)
        bearertoken = data['data']['token']
        print(bearertoken)


if __name__ == '__main__':
    OPToken()
