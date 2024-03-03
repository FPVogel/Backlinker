import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

def check_backlink(backlink, site):
    url = backlink['url'].replace("h4link.duckdns.org", site)
    try:
        r = requests.get(url).status_code
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        r = "time out"
    print(site + " => Backlink Eklendi ==> " + re.search(r'http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:", "") + " status: " + str(r))

try:
    print("""
            _ ____             _    _ _       _
           | |  _ \           | |  | (_)     | |
 _   _ _ __| | |_) | __ _  ___| | _| |_ _ __ | | _____ _ __
| | | | '__| |  _ < / _` |/ __| |/ / | | '_ \| |/ / _ \ '__|
| |_| | |  | | |_) | (_| | (__|   <| | | | | |   <  __/ |
 \__,_|_|  |_|____/ \__,_|\___|_|\_\_|_|_| |_|_|\_\___|_|
                                              H4-cklinker - wmdark.com
  """)
    if sys.version_info.major == 3:
        site = input(" => Backlink Kasilcak Site\t: ")
    else:
        site = raw_input(" => Backlink Kasilcak Site\t: ")

    with open("urlbacklinks.json", "r") as file:
        data = json.loads(file.read())
        with ThreadPoolExecutor() as executor:
            executor.map(lambda backlink: check_backlink(backlink, site), data)

except Exception as e:
    print("\n\n => exit\n")
    print(e)

