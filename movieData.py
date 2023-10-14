import requests
from dotenv import load_dotenv
import os

load_dotenv()


url = "https://streaming-availability.p.rapidapi.com/countries"

headers = {
	"X-RapidAPI-Key": os.getenv('API_KEY'),
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers)



result= {
        "12": "Adventure",
        "14": "Fantasy",
        "16": "Animation",
        "18": "Drama",
        "27": "Horror",
        "28": "Action",
        "35": "Comedy",
        "36": "History",
        "37": "Western",
        "53": "Thriller",
        "80": "Crime",
        "99": "Documentary",
        "878": "Science Fiction",
        "9648": "Mystery",
        "10402": "Music",
        "10749": "Romance",
        "10751": "Family",
        "10752": "War",
        "10763": "News",
        "10764": "Reality",
        "10767": "Talk Show"
    }