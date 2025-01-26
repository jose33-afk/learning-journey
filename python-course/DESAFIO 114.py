import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.nuuvem.com/br-pt/item/valorant-gift-card-digital-113')
    print('ok')
except:
    print('erro')
