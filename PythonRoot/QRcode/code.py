from MyQR import myqr
import os

version, level, qr_name = myqr.run(words = 'http://love.zxgnz.com/html/20200212/15814955946899.html',
                                    version = 1,
                                    level = 'H',
                                    picture = 'maomi.gif',
                                    colorized= True,
                                    save_name= 'qrcode.gif',
                                    save_dir=os.getcwd())