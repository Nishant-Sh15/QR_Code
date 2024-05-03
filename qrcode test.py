#importing the qrcode module required
import qrcode

#asking for the file we want to convert into a qrcode 
name=str(input("enter name of the file u want to convert into a qrcode"))

#opening and reading the file
f=open(name+".txt","r")
data=f.read()

#creating a qrcode object
qr=qrcode.QRCode(version=10,box_size=20)

#adding data to the qrcode object
qr.add_data(data)

#creating and saving the qrcode image 
img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")

#closing the file
f.close()
