import pyqrcode
import png
from pyqrcode import QRCode

#Starting which represents the Qr code
s="https://www.hackerrank.com/profile/ayushkumar_sing5"

#Generate QR code
url = pyqrcode.create(s)

#Create and save the svg file naming "Ayushqr.svg"
url.svg("Ayushqr.svg",scale=8)

#create and save the png file naming "ayushqr.png"
url.png("Ayushqe.png",scale = 6)