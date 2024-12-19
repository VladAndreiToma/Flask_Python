from ast import Raise
import sys
import qrcode
from reportlab.pdfgen import canvas

def Generate_Instagram_QR( whatIsYourInstaName ):
    # whatsyourname is for instagram page
    instaURL = f"https://www.instagram.com/{whatIsYourInstaName}"

    thisQRCode = qrcode . QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    thisQRCode . add_data( instaURL )
    thisQRCode . make( fit = True )

    thisImg = thisQRCode . make_image( fill_color="black" , back_color="orange" )

    thisImg . save( "QR_Alexandra_HairStyle.png" )
    thisImg . show()

    pdfFile = f"{whatIsYourInstaName}QR.pdf"
    pdf = canvas . Canvas( pdfFile )
    pdf . drawInlineImage( thisImg , 100 , 300 )
    pdf . save()


if __name__ == "__main__":
    if len( sys.argv ) != 2:
        print( "provide 1 compilation string username argument or less arguments" )
        sys . exit(1)
    
    instaName = sys.argv[1]

    Generate_Instagram_QR( instaName )