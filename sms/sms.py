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

if __name__ == "__main__":
    test_message = 'Rail madad complaint management test 2'
    result = send_sms(test_message)
    print(result)
