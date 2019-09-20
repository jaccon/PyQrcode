import pyqrcode
# url = pyqrcode.create('https://www.ppinkpunch.com.br/loja/')
# url.svg('uca-url.svg', scale=8)
# print(url.terminal(quiet_zone=1))

url = pyqrcode.create('https://www.ppinkpunch.com.br/loja/')
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))