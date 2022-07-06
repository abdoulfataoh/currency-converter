#!/usr/bin/python3


import cgi
from HTML_TREMPLATE import HTML_RESULT_TREMPLATE
from currency_converter import currencylayer_wrapper

api_url = "http://api.currencylayer.com/"
api_access_key = "856a913c5a9aa8f3e5b1c530383041a5"

currencylayer_obj = currencylayer_wrapper(api_url, api_access_key)


form = cgi.FieldStorage()
ammount = int(form.getvalue("ammount"))
from_currency = form.getvalue("from-currency")
to_currency = form.getvalue("to-currency")
r = currencylayer_obj.offline_convert(from_currency, to_currency, ammount)

print("Content-Type: text/html")
print()
print(HTML_RESULT_TREMPLATE % (r, to_currency))

