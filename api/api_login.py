"""
智检精灵登录环境封装
"""

import requests
import configparser

# 读取配置
config = configparser.ConfigParser()
config.read("./config/env_config.ini")
section = "Inspection"

env = config.get(section, "execution_env")
space_name = config.get(section, "space_name")
miai_product_code = config.get(section, "miai-product-code")
miaispacemanageid = config.get(section, "miaispacemanageid")

if env == "dev":
    token_url = ""
    username = ""
    password = 123456
    url = ""
    code = miai_product_code
    manageid = miaispacemanageid
else:
    if env == "fat":
        token_url = ""
        username = ""
        password = 123456
        url = ""
        code = miai_product_code
        manageid = miaispacemanageid
    else:
        print("环境不正确，请重新输入")


class ApiLogin:
    def __init__(self):
        pass

    def login(self):
        login_data = {"client_id": "brainstorm-fe", "username": username, "password": password,
                      "grant_type": "password"}
        login_header = {"content-type": "application/x-www-form-urlencoded"}

        login_rep = requests.post(url=token_url, data=login_data, headers=login_header)
        # print(login_rep.text)
        token_type = login_rep.json()["token_type"]
        access_token = login_rep.json()["access_token"]
        token = token_type + " " + access_token
        # print(token)
        return token


if __name__ == '__main__':
    m = ApiLogin()
    m.login()
