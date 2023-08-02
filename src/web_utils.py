CDN_URL = "https://cdn.cloudflare.steamstatic.com/steam/apps"
IMAGE_NAME = "library_600x900.jpg"


def get_image_url(app_id):
    return f"{CDN_URL}/{app_id}/{IMAGE_NAME}"
