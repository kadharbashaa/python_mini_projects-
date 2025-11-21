import qrcode

text = input("enter text / URL to generate qr :")

qr_img=qrcode.make(text)
qr_img.save("qrcode.img")

print("qr code generated successfully qr code .png")