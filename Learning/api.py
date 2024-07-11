import requests

url = "https://dit.whatsapp.net/deidentified_telemetry"
 
payload = {
    "content": "hey girl"
}

header ={
    "access_token": "245118376424571|3e7d275052f1522bf3200afcf53841a7",
    "credential": "KJl7zNn9JhQxO6AShzCR0THl7SF7Y5JgN999LDThc48=+cT6KpfhzSo6bePg1We2wI3YEKGml6CmRk8T_9tMBlho="
}

msg = requests.post(url,payload,headers=header)

