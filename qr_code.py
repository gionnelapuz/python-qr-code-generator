import os
from os import path
import json

import qrcode
import qrcode.image.svg

export_folder = 'Exports/'

def generateQRCode(folder_path, data):
    qr_code_url = data['url']
    qr = qrcode.QRCode(
            version=1,
            box_size=100,
            border=5
        )
    qr.add_data(qr_code_url)
    img = qr.make_image(fill='black', back_color='white', image_factory=qrcode.image.svg.SvgImage)
    img.save(folder_path + '/'+ data['name'] + '.svg')


def getJsonData():  
    for data in json.load(open('json_files/example.json')):
        generateQRCode(export_folder, data)


getJsonData()