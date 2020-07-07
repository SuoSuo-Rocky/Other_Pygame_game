

import requests

data = requests.get(
    url="https://github.com/coderShenhy/python-games/archive/master.zip",
    timeout= 222000)
with open("master.zip", "wb") as f:
    f.write(data.content)

