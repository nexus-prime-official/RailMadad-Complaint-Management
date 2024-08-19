import requests
from env_var import apiSecret, deviceId, phone

def send_sms(message):

    payload = {
        "secret": apiSecret,
        "mode": "devices",
        "device": deviceId,
        "sim": 1,
        "priority": 1,
        "phone": phone,
        "message": message
    }

    response = requests.post(url="https://www.cloud.smschef.com/api/send/sms", params=payload)
    
    result = response.json()

    return result

