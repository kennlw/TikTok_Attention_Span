import requests
import time
import pandas as pd

user_ls = ["abbyroberts", "kylethomas", "klwp_3", "hollyh",  "rhia.official", "neffatibrothers"
           , "thistrippyhippie", "itzshauni", "nintendo.grl", "rilacchi", "charluiu", "liverpoolfc",
           "playadoptme", "yungblud", "jasleenxbeauty",
           "charlidamelio", "bellapoarch", "willsmith", "zachking", "jasonderulo", "spencerx"]

data_array = []
data_heads = [
    "aweme_id",
    "comment_count",
    "digg_count",
    "download_count",
    "share_count",
]

for user in user_ls:
    try:
        print(user)
        url = f"https://tiktok-best-experience.p.rapidapi.com/user/{user}/feed"

        querystring = {}

        headers = {
            "X-RapidAPI-Key": "0ae27abe0cmsha7512d2059572d1p136488jsn01d8cf8cc1ea",
            "X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring).json()["data"]["aweme_list"]
        for i in range(len(response)):
                temp_dict = {head: response[i]["statistics"][head] for head in data_heads}
                temp_dict["duration"] = response[i]["video"]["duration"]
                data_array.append(temp_dict)

        df = pd.DataFrame(data_array)

    except IndexError:
        print("Index Error")
    except KeyError:
        print("Key Error")
    except requests.exceptions.RequestException as e:
        print("Request Error")
    except Exception as e:
        print("Catch-all error", e)

    time.sleep(3)

save_data = df.to_csv("new_vid_data.csv", index=True)
print("Finished.")