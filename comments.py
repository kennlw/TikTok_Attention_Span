import requests
import pandas as pd
import numpy as np
import time
import random

querystring = {"max_cursor":"20"}

headers = {
	"X-RapidAPI-Key": "_",
	"X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
}

df = pd.read_csv("new_vid_data.csv")
aweme_ids = df.loc[:,"aweme_id"].values.tolist()

vid_id = ""
all_data = []

for i in range(635):
	try:
		print(f"Cycle: {i+1}")
		vid_id = aweme_ids[i]
		data = []
		url = "https://tiktok-best-experience.p.rapidapi.com/comments/" + str(vid_id)

		response = requests.get(url, headers=headers, params=querystring).json()["data"]["comments"]
		
		for k in range(len(response)):
			data.append(str(response[k]["text"].encode("ascii","ignore"))[2:][:-1])

		all_data.append(str(data) + ",")

	except IndexError: print("Index Error"), all_data.append("IndexError")
	except requests.exceptions.RequestException as e: print("Request Error"), all_data.append("Request Error")
	except TypeError: all_data.append(str(vid_id) + ","), print("TypeError: " + str(vid_id))
	except Exception as e: print("Catch-all error", e), all_data.append(e)

	time.sleep(random.randint(3,5))

np.savetxt("new_vid_comments.csv", 
           all_data,
           delimiter =", ",
           fmt ='% s')
