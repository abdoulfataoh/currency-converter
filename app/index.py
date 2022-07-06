#!/usr/bin/python3

from HTML_TREMPLATE import HTML_INDEX_TREMPLATE
from currency_converter import currencylayer_wrapper

api_url = "http://api.currencylayer.com/"
api_access_key = "856a913c5a9aa8f3e5b1c530383041a5"

currencylayer_obj = currencylayer_wrapper(api_url, api_access_key)
var = currencylayer_obj.get_currencie_html_format()

print("Content-Type: text/html")
print()
print(HTML_INDEX_TREMPLATE %(var, var))
