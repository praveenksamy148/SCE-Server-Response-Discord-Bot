import requests 
import json
import os
import time 
from dhooks import Webhook 
hook = Webhook("https://discord.com/api/webhooks/1093235362538729586/kgYWdKUiLWfS8K0H7-nTfgrwjbZk-ZWyEpzpyFFgK7fkC1J-fM0piGqwKZKLraAcr2fa")
def getStatusCode(): 
    url = f"http://localhost:3000"
    currentTime = time.ctime()
    try:
       get = requests.get(url)
       status = get.status_code
       if status == 200 or 300: 
        serverStatus = "Server Up"
       print(serverStatus)
    #    hook.send(f"Server Up {currentTime}")
    except: 
        print("server Down")
        hook.send(f"SCE SERVER DOWN AT {currentTime}")

getStatusCode()
# data = "SCE SERVER DOWN!"
# hook.send(data)








