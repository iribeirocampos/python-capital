import requests
import json
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from .exceptions import CapitalAPIException


class Client:
    def __init__(self, username, api_key, password, demo=False):
        self.username = username
        self.api_key = api_key
        self.password = password
        self.headers = {
            "X-CAP-API-KEY": self.api_key,
            "content-type": "application/json",
        }
        if demo is False:
            self.server = "https://api-capital.backend-capital.com"
        else:
            self.server = "https://demo-api-capital.backend-capital.com/"

    def __get_encryption_key__(self):
        url = f"{self.server}/api/v1/session/encryptionKey"
        data = self.__make_request__("get", url, "")[0]
        self.enc_key = [data["encryptionKey"], data["timeStamp"]]

    def __make_request__(self, type, url, payload):
        if type == "post":
            response = requests.post(url, headers=self.headers, data=payload)
        if type == "get":
            response = requests.get(url, headers=self.headers, data=payload)
        if type == "delete":
            response = requests.delete(url, headers=self.headers, data=payload)
        if type == "put":
            response = requests.put(url, headers=self.headers, data=payload)
        if not (200 <= response.status_code < 300):
            raise CapitalAPIException(response, response.status_code, response.text)
        else:
            return json.loads(response.text), response.headers

    def __encrypt__(self, password, key):
        key = b64decode(key)
        key = RSA.importKey(key)
        cipher = PKCS1_v1_5.new(key)
        ciphertext = b64encode(cipher.encrypt(bytes(password, "utf-8")))
        return ciphertext

    def __create_session__(self):
        self.__get_encryption_key__()
        url = f"{self.server}/api/v1/session"
        string_encrypt = f"{self.password}|{self.enc_key[1]}"
        encrypted_password = str(
            self.__encrypt__(string_encrypt, self.enc_key[0]), "utf-8"
        )
        payload = json.dumps(
            {
                "identifier": self.username,
                "password": encrypted_password,
                "encryptedPassword": True,
            }
        )
        data = self.__make_request__("post", url, payload)[1]
        self.CST = data["CST"]
        self.X_TOKEN = data["X-SECURITY-TOKEN"]
        self.headers = {
            "X-SECURITY-TOKEN": self.X_TOKEN,
            "CST": self.CST,
            "content-type": "application/json",
        }

    def __confirmation__(self, deal_reference):
        url = f"{self.server}/api/v1/confirms/{deal_reference}"
        return self.__make_request__("get", url, payload="")[0]

    # Returns all accounts in server
    def all_accounts(self):
        self.__create_session__()
        url = f"{self.server}/api/v1/accounts"
        data = self.__make_request__("get", url, payload="")[0]
        self.__log_out__()
        return data

    # Returns account preferences, i.e. leverage settings and trading mode
    def account_pref(self):
        self.__create_session__()
        url = f"{self.server}/api/v1/accounts/preferences"
        data = self.__make_request__("get", url, payload="")[0]
        self.__log_out__()
        return data

    # Update account preferences
    def update_account_pref(
        self,
        leverages={
            "SHARES": 5,
            "INDICES": 20,
            "CRYPTOCURRENCIES": 2,
        },
        hedging_mode=False,
    ):
        self.__create_session__()
        data = {
            "leverages": leverages,
            "hedgingMode": hedging_mode,
        }
        payload = json.dumps(data)
        url = f"{self.server}/api/v1/accounts/preferences"
        data = self.__make_request__("put", url, payload=payload)[0]
        self.__log_out__()
        return data

    # Switch active account
    def change_active_account(self, account_id):
        self.__create_session__()
        url = f"{self.server}/api/v1/session"
        payload = json.dumps({"accountId": account_id})
        data = self.__make_request__("put", url, payload=payload)[0]
        self.__log_out__()
        return data

    # gets you all current positions
    def all_positions(self):
        self.__create_session__()
        url = f"{self.server}/api/v1/positions"
        data = self.__make_request__("get", url, payload="")[0]
        self.__log_out__()
        return data

    # Opens a new position
    def create_position(
        self,
        epic,
        direction,
        size,
        guaranteed_stop=False,
        trailing_stop=False,
        stop_level=None,
        stop_distance=None,
        stop_amount=None,
        profit_level=None,
        profit_distance=None,
        profit_amount=None,
    ):
        self.__create_session__()
        url = f"{self.server}/api/v1/positions"
        data = {
            "epic": epic,
            "direction": direction.upper(),
            "size": str(size),
            "guaranteedStop": guaranteed_stop,
            "trailingStop": trailing_stop,
        }
        if stop_level is not None:
            data.update({"stopLevel": stop_level})
        if stop_distance is not None:
            data.update({"stopDistance": stop_distance})
        if stop_amount is not None:
            data.update({"stopAmount": stop_amount})
        if profit_level is not None:
            data.update({"profitLevel": profit_level})
        if profit_distance is not None:
            data.update({"profitDistance": profit_distance})
        if profit_amount is not None:
            data.update({"profitAmount": profit_amount})
        payload = json.dumps(data)
        data = self.__make_request__("post", url, payload=payload)[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Closes a specific position with the deal_id
    def close_position(self, deal_id):
        self.__create_session__()
        url = f"{self.server}/api/v1/positions/{deal_id}"
        data = self.__make_request__("delete", url, payload="")[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Update the position
    def update_position(
        self,
        deal_id,
        guaranteed_stop=False,
        trailing_stop=False,
        stop_level=None,
        stop_distance=None,
        stop_amount=None,
        profit_level=None,
        profit_distance=None,
        profit_amount=None,
    ):
        data = {"guaranteedStop": guaranteed_stop, "trailingStop": trailing_stop}
        if stop_level is not None:
            data.update({"stopLevel": stop_level})
        if stop_distance is not None:
            data.update({"stopDistance": stop_distance})
        if stop_amount is not None:
            data.update({"stopAmount": stop_amount})
        if profit_level is not None:
            data.update({"profitLevel": profit_level})
        if profit_distance is not None:
            data.update({"profitDistance": profit_distance})
        if profit_amount is not None:
            data.update({"profitAmount": profit_amount})
        payload = json.dumps(data)
        self.__create_session__()
        url = f"{self.server}/api/v1/positions/{deal_id}"
        data = self.__make_request__("put", url, payload=payload)[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Returns all open working orders for the active account
    def all_working_orders(self):
        self.__create_session__()
        url = f"{self.server}/api/v1/workingorders"
        data = self.__make_request__("get", url, payload="")[0]
        self.__log_out__()
        return data

    # Create a limit or stop order
    def create_working_order(
        self,
        epic,
        direction,
        size,
        level,
        type,
        guaranteed_stop=False,
        trailing_stop=False,
        stop_level=None,
        stop_distance=None,
        stop_amount=None,
        profit_level=None,
        profit_distance=None,
        profit_amount=None,
    ):
        self.__create_session__()
        url = f"{self.server}/api/v1/workingorders"
        data = {
            "epic": epic,
            "direction": direction.upper(),
            "size": str(size),
            "level": level,
            "type": type,
            "guaranteedStop": guaranteed_stop,
            "trailingStop": trailing_stop,
        }
        if stop_level is not None:
            data.update({"stopLevel": stop_level})
        if stop_distance is not None:
            data.update({"stopDistance": stop_distance})
        if stop_amount is not None:
            data.update({"stopAmount": stop_amount})
        if profit_level is not None:
            data.update({"profitLevel": profit_level})
        if profit_distance is not None:
            data.update({"profitDistance": profit_distance})
        if profit_amount is not None:
            data.update({"profitAmount": profit_amount})
        payload = json.dumps(data)
        data = self.__make_request__("post", url, payload=payload)[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Update a limit or stop order
    def update_working_order(
        self,
        deal_id,
        level,
        guaranteed_stop=False,
        trailing_stop=False,
        stop_level=None,
        stop_distance=None,
        stop_amount=None,
        profit_level=None,
        profit_distance=None,
        profit_amount=None,
    ):
        data = {
            "guaranteedStop": guaranteed_stop,
            "trailingStop": trailing_stop,
            "level": level,
        }
        if stop_level is not None:
            data.update({"stopLevel": stop_level})
        if stop_distance is not None:
            data.update({"stopDistance": stop_distance})
        if stop_amount is not None:
            data.update({"stopAmount": stop_amount})
        if profit_level is not None:
            data.update({"profitLevel": profit_level})
        if profit_distance is not None:
            data.update({"profitDistance": profit_distance})
        if profit_amount is not None:
            data.update({"profitAmount": profit_amount})
        payload = json.dumps(data)
        self.__create_session__()
        url = f"{self.server}/api/v1/workingorders/{deal_id}"
        data = self.__make_request__("put", url, payload=payload)[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Delete a limit or stop order
    def delete_working_order(self, deal_id):
        self.__create_session__()
        url = f"{self.server}/api/v1/workingorders/{deal_id}"
        data = self.__make_request__("delete", url, payload="")[0]
        final_data = self.__confirmation__(data["dealReference"])
        self.__log_out__()
        return final_data

    # Returns all top-level nodes (market categories) in the market navigation hierarchy
    def all_top(self):
        self.__create_session__()
        url = f"{self.server}/api/v1/marketnavigation"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    # Returns all sub-nodes (markets) of the given node (market category) in the market navigation hierarchy
    def all_top_sub(self, node_id):
        self.__create_session__()
        url = f"{self.server}/api/v1/marketnavigation/{node_id}?limit=500"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    # Returns the details of the given markets
    def market_details(self, market):
        self.__create_session__()
        url = f"{self.server}/api/v1/markets?searchTerm={market}"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    # Returns the details of the given market
    def single_market_details(self, epic):
        self.__create_session__()
        url = f"{self.server}/api/v1/markets/{epic}"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    # Returns historical prices for a particular instrument
    def prices(self, epic, resolution="MINUTE", max=10):
        self.__create_session__()
        url = f"{self.server}/api/v1/prices/{epic}?resolution={resolution}&max={max}"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    # Client sentiment for market
    def client_sentiment(self, market_id):
        self.__create_session__()
        url = f"{self.server}/api/v1/clientsentiment/{market_id}"
        data = self.__make_request__("get", url, payload="")
        self.__log_out__()
        return data

    def __log_out__(self):
        requests.delete(f"{self.server}/api/v1/session", headers=self.headers)
        self.headers = {
            "X-CAP-API-KEY": self.api_key,
            "content-type": "application/json",
        }
