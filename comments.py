import requests
import pandas as pd
import numpy as np
import time
import random

querystring = {"max_cursor":"10"}

headers = {
	"X-RapidAPI-Key": "0ae27abe0cmsha7512d2059572d1p136488jsn01d8cf8cc1ea",
	"X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
}

df = pd.read_csv("final.csv")
aweme_ids = df.loc[:,"aweme_id"].values.tolist()

vid_id = ""
all_data = []
dead_vids = []
for i in range(200):
	try:
		print(f"Cycle: {i+1}")
		vid_id = aweme_ids[i]
		data = []
		url = "https://tiktok-best-experience.p.rapidapi.com/comments/" + str(vid_id)

		response = requests.get(url, headers=headers, params=querystring).json()["data"]["comments"]
		
		for k in range(10):
			data.append(response[k]["text"].encode("ascii","ignore"))

		all_data.append(str(data) + ",")

	except IndexError: print("Index Error"), all_data.append("IndexError, "), dead_vids.append("index_error")
	except KeyError: print("Key Error")
	except requests.exceptions.RequestException as e: print("Request Error")
	except TypeError: all_data.append(str(vid_id) + ","), print("TypeError: " + str(vid_id)), dead_vids.append(str(vid_id))
	except Exception as e: print("Catch-all error", e)

	time.sleep(random.randint(3,4))

np.savetxt("Comments3.csv", 
           all_data,
           delimiter =", ",
           fmt ='% s')
np.savetxt("removed_vids3.csv", 
           dead_vids,
           delimiter =", ",
           fmt ='% s')