from io import BytesIO

import qrcode
import requests
from tqdm.asyncio import tqdm

hshop_url = "https://hshop.erista.me/"
download_url = "https://download4.erista.me/content/"


def gen_qr_code(id):
    """Generates a QR Code with a link to a content download from URL, for usage in FBI."""

    game_id = str(id)
    req = requests.get(download_url + "request?id=" + game_id)
    data = req.json()
    token = data["token"]
    token_url = download_url + game_id + "?token=" + token
    img = qrcode.make(token_url)
    buf = BytesIO()
    img = img.resize((200, 200))
    img.save(buf, format="PNG")
    return buf.getvalue()


def download(id, download_path):
    """Downloads content from ID (obtained in the details url of content)"""
    game_id = str(id)
    req = requests.get(download_url + "request?id=" + game_id)
    data = req.json()
    token = data["token"]
    token_url = download_url + game_id + "?token=" + token
    print("URL: " + token_url)
    print("Downloading content with ID " + game_id + ", please wait...")
    response = requests.get(token_url, stream=False)

    with open(f"{download_path}/{game_id}.cia", "wb") as handle:
        for data in tqdm(
            response.iter_content(), unit="B", unit_scale=True, unit_divisor=1024
        ):
            handle.write(data)
    print(f"Done with {game_id}!")


def search(query, **kwargs):
    query_dict = {"query": query}
    if kwargs.get("category"):
        query_dict["xc"] = kwargs.get("category")
    if kwargs.get("region"):
        query_dict["xs"] = kwargs.get("region")
    req = requests.get("https://hshop.erista.me/api/title/search", params=query_dict)
    return req.json()
