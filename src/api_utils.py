import requests

# Reference: https://github.com/woctezuma/steam-store-snapshots
API_URL = "https://api.steampowered.com/ISteamApps/GetAppList/v2"


def get_app_ids(url=API_URL):
    r = requests.get(url)

    if r.ok:
        data = r.json()
        app_ids = {app["appid"] for app in data["applist"]["apps"]}
    else:
        app_ids = {}

    return sorted(app_ids)
