import requests

url = "https://businesses-scoop-moving-few.trycloudflare.com/ring"

def ring_my_pc():
    try:
        response = requests.get(url, timeout=5)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e)