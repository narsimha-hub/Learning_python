import qrcode
url=input("enter url").strip()
# def urltoqr(url):
file_path=r"C:\\Users\\narsi\\OneDrive\\Pictures\\qr_codess\\overleaf resume.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)
# res=urltoqr(url)
# print(res)www.linkedin.com/in/narsimha1906

    
    