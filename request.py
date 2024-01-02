import requests

# API_TOKEN = ""
# API_URL = "http://127.0.0.1:8000/predict-news"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "http://127.0.0.1:8000/predict-news"

def query(payload):
	response = requests.post(API_URL, json=payload)
	return response.json()
	
output = query({
	"text": "Mau Liburan 5 Hari ke Jepang Lihat Sakura? Yuk Simak Itinerary-nya"
})

print(output)
