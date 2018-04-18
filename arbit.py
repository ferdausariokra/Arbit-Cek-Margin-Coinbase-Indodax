import common
import public
import coinbase
import requests
import pandas
import numpy
import urllib
import string
import time
from bs4 import BeautifulSoup
from lxml import html

from coinbase.wallet.client import Client
client = Client("50HzWqiInd2qNsdB", "q4z20FSl62zaxM3CW4MH4nNfwwComPYK")

def cek_margin(deposit_usd, kurs_usd_idr, param_cb, param_vip, miningfee_cb):
    transferfee = 30.0
    saldo_usd = deposit_usd - transferfee
    deposit_idr = deposit_usd*kurs_usd_idr
    price_btc_cb = client.get_buy_price(currency_pair = param_cb)
    btc_cb = saldo_usd/float(price_btc_cb["amount"])
    btc_vip = btc_cb - miningfee_cb
    vip = public.getTicker(param_vip)
    saldo_idr = float(vip['buy'])*btc_vip
    tarik_idr = 0.99*saldo_idr
    margin = tarik_idr - deposit_idr
    persenmargin =  margin*100/deposit_idr
    return persenmargin



while(1):
    
    url = 'https://www.bankmandiri.co.id/kurs'
    usd_idr_float = float(BeautifulSoup(urllib.request.urlopen(url), "lxml").find('table').findAll('strong')[len(BeautifulSoup(urllib.request.urlopen(url), "lxml").find('table').findAll('strong'))-1].contents.pop(0).strip(',00'))*1000
    print("Mandiri USD-IDR  -> Rp",usd_idr_float)
    print("Modal IDR        -> Rp",usd_idr_float*3000)

    persen = cek_margin(3000.0, usd_idr_float, 'BTC-USD', 'btc', 0.001)
    print("Margin Arbit BTC -> ", "%.2f" %persen, "%")

    persen = cek_margin(3000.0, usd_idr_float, 'ETH-USD', 'eth', 0.1)
    print("Margin Arbit ETH -> ", "%.2f" %persen, "%")

    persen = cek_margin(3000.0, usd_idr_float, 'BCH-USD', 'bch', 0.01)
    print("Margin Arbit BCH -> ", "%.2f" %persen, "%")

    persen = cek_margin(3000.0, usd_idr_float, 'LTC-USD', 'ltc', 0.1)
    print("Margin Arbit LTC -> ", "%.2f" %persen, "%")
    

    #depth = public.getDepth('ltc')
    #print(depth)
  
    print(" ")
    time.sleep(3)

     
