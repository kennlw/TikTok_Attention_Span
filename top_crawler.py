import requests
import pandas as pd
import time
import json
import random

data_heads = [
    "aweme_id",
    "comment_count",
    "digg_count",
    "download_count",
    "share_count",
]

data_array = []
cursor = 1

for i in range(2):
    print(f"Current cycle: {i+1}")

    try:
        url = "https://tiktok-best-experience.p.rapidapi.com/trending/US"

        querystring = {"custom_cursor":""}

        headers = {
            "X-RapidAPI-Key": "0ae27abe0cmsha7512d2059572d1p136488jsn01d8cf8cc1ea",
            "X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com",
        }
        
        response = requests.get(url, headers=headers, params=querystring).json()["data"]["list"]

        print(response)
        for i in range(len(response)):
            temp_dict = {head: response[i]["statistics"][head] for head in data_heads}
            temp_dict["duration"] = response[i]["video"]["duration"]
            data_array.append(temp_dict)

        df = pd.DataFrame(data_array)

        time.sleep(60)

    except IndexError:
        print("Index Error")
    except KeyError:
        print("Key Error")
    except requests.exceptions.RequestException as e:
        print("Request Error")
    except Exception as e:
        print("Catch-all error", e)
    
save_data = df.to_csv("Video_Data7.csv", index=True)
print("Finished.")
