import qrcode 
qr=qrcode.QRCode( 
    version=5, 
    box_size=5,
    border=7
)
print("Welcome to QR Code Generator \n") 
data=input("Please enter the link or the data that needs to be converted in QR\n")
# data="https://www.facebook.com/rajzdkl99" 
# This was previous code which specify the data to be generated beforehand but in new code user have access to change the data that needs to make qrcode.
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("generatedqr.png")
# line 1 : This is the first Step to make QRcode // here we will import module named qrcode 
# line 2 : here we will create object( QRCode ) and we are giving refrence to the the module (qrcode)
# line 3 : here we can make the size of qr by specifying the version
# line 4 : here we can make the box size of qr by specifying the box_size
# line 5 : here we can give desire outside border 
# line 9 : we are creating a variable for storing the data that needs to be generated as QR  
# line 11 : this is a method add_data which stores the data   
# line 13 : this is also a method which will make image and we can change the colors
# line 14 : and the last step we will call a method save or we can also give another variable that allows user to choose the desired name for the QR 





  