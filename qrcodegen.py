import qrcode
from PIL import Image
def generateDownloadQRCode(id):
    '''Generates a QR Code with a link to a content download from URL, for usage in FBI.'''

    dID = str(id)
    downloadurl = "https://download4.erista.me/content/"
    req = requests.get(downloadurl + "request?id=" + dID)
    data = req.json()
    token = data["token"]
    completedownloadurl = downloadurl + dID + "?token=" + token
    print("URL: " + completedownloadurl)

    img = qrcode.make(completedownloadurl)
    openimg = Image.open(img)
    openimg.show()
