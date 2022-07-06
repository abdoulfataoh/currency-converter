# Programm: Convertisseur de devise
# Author: abdoulfataoh, abdoulfataoh@gmail.com
# Licence: GPL

import json
import io
import time
from typing import Dict

import pycurl


class currencylayer_wrapper:
    """
        currencylayer est plateforme en ligne permettant de convertir des devises.
        currencylayer API est une API HTTP proposee par cette plateforme.
        Documentation de cette API: https://currencylayer.com/documentation    
    """
    dic_currencies = dict()
    dic_exhange_rate = dict()

    def __init__(self, api_url: str, api_access_key: str) -> None:
        self.api_url = api_url
        self.api_access_key = api_access_key
        currencylayer_wrapper.dic_exhange_rate = self.get_exchange_rate()
        currencylayer_wrapper.dic_currencies = self.get_currencies()

    
    def get_currencies(self) -> Dict:
        endpoint = "list"
        data_property = "currencies"
        request = self.get_request_url(endpoint)
        return self.execute_request(request, data_property)
    
    def get_exchange_rate(self):
        endpoint = "live"
        data_property = "quotes"
        request = self.get_request_url(endpoint)
        return self.execute_request(request, data_property)
    
    def live_convert(self, from_currency: str, to_currency: str, amount: float):
        endpoint = "convert"
        data_property = "result"
        request = self.get_request_url(endpoint) + "&from=" + from_currency + "&to=" + to_currency + "&amount=" + str(amount)
        return self.execute_request(request, data_property)       
    
    def execute_request(self, request: str, data_property: str):
        url = request
        request_result = io.BytesIO()
        request_result_dic = dict()

        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)      
        curl.setopt(curl.WRITEDATA, request_result)
        try:
            curl.perform()
            time.sleep(2)
            
        except pycurl.error:
            print("Echec lors de la connection avec currencylayer, verifier votre connection internet")
        else:
            curl.close()
            request_result_dic = json.loads(request_result.getvalue().decode("utf8"))
            if request_result_dic["success"] == True:
                return request_result_dic[data_property]
            else:
                return {-1}
        
    def update(self):
        currencylayer_wrapper.dic_currencies = self.get_currencies()
        currencylayer_wrapper.dic_exhange_rate = self.get_exchange_rate()
        
    def get_request_url(self, endpoint: str):
        return self.api_url + endpoint + "?" + "access_key=" + self.api_access_key

    def get_currencie_html_format(self):
        html_obj = ''
        for key, name in self.get_currencies().items():
            html_obj += f'<option value="{key}"> {name} </option>'
        return html_obj

    def offline_convert(self, from_currency: str, to_currency: str, amount: float):
        return amount / self.dic_exhange_rate["USD"+from_currency] * self.dic_exhange_rate["USD"+to_currency]
            
    



### Excecutez si c'est l'entree principale

if __name__ == "__main__":
    api_url = "http://api.currencylayer.com/"
    api_access_key = "856a913c5a9aa8f3e5b1c530383041a5"

    print("---- Convertisseur de devises version 1.0: ----")
    currencylayer_obj = currencylayer_wrapper(api_url, api_access_key)
    ammount = float(input("Quelle est le montant a convertir: "))
    from_currency = input("Quelle est la devise de ce montant ? exemple XOF, EUR, USD ... : ").upper()
    to_currency = input("Quelle est la devise vers laquelle convertir ce montant ? exemple XOF, EUR, USD ... : ").upper()
    print(currencylayer_obj.offline_convert(from_currency, to_currency, ammount), " ", to_currency)








