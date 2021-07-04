# importar a biblioteca PyQRCode
import pyqrcode

# Url do site
url = pyqrcode.create('https://github.com/luiz-pr')

# Cria um arquivo svg
url.svg('git-url.svg', scale=4)

# Cria um arquivo eps
url.eps('git-url.eps', scale=1)

# Mostra o que aconteceu
print(url.terminal(quiet_zone=1))