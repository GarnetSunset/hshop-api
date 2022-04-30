import qrcode
import requests
from os import startfile

from tqdm.asyncio import tqdm

hshop_url = "https://hshop.erista.me/"
download_url = "https://download4.erista.me/content/"


def generateQRCode(id, path):
    """Generates a QR Code with a link to a content download from URL, for usage in FBI."""

    game_id = str(id)
    req = requests.get(download_url + "request?id=" + game_id)
    data = req.json()
    token = data["token"]
    token_url = download_url + game_id + "?token=" + token
    qr = qrcode.make(token_url)
    qrimagepath = path + game_id + ".png"
    qr.save(qrimagepath)
    print("QR Code saved to: " + qrimagepath)
    startfile(qrimagepath)


def download(id, path):
    """Downloads content from ID (obtained in the details url of content)"""
    game_id = str(id)
    req = requests.get(download_url + "request?id=" + game_id)
    data = req.json()
    token = data["token"]
    token_url = download_url + game_id + "?token=" + token
    print("URL: " + token_url)
    print("Downloading content with ID " + game_id + ", please wait...")
    response = requests.get(token_url, stream=False)

    with open(downloadpath + game_id + ".cia", "wb") as handle:
        for data in tqdm(
            response.iter_content(), unit="B", unit_scale=True, unit_divisor=1024
        ):
            handle.write(data)


def search(title, **kwargs):
    req = requests.get(
        "https://hshop.erista.me/api/title/search", params={"query": f"{query}"}
    )
    print("")
