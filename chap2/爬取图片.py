import requests
url='https://www.baidu.com/img/doodlegaokaokaohou_5b0f886d182bfd1761854cb4dfa72fa8.gif'

resp=requests.get(url)

#保存到本地
with open('logo.png','wb')as file:
    file.write(resp.content)

import openpyxl   