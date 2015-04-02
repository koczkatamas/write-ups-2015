def decrypt_RSA(private_key_loc, package):
    from Crypto.PublicKey import RSA 
    from Crypto.Cipher import PKCS1_OAEP 
    from base64 import b64decode 
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    rsakey = PKCS1_OAEP.new(rsakey) 
    decrypted = rsakey.decrypt(b64decode(package)) 
    return decrypted
flag = 'oizSSgh67kNHywSsIaSw6oPqPq4IYOVJloOXDJryDAa1bleXqtB0h0mzb971b02xZcaAulyCbGR5wDIco0fHPyPWVEZ3xRY0o8AF/fmuo3MZeN30UpIIBE/zwEDMASyCoArrY0GXWGTavibULyOQ4ZHB1xE/GdQTkwy47TASQzVvdBxzHx/qRG7izYTDfEbo4NLR35AmUbFavxRpGQvHfbJWARbdGzJRQwvB9FCqbZDetM2S8O2s2LVj5+EZ91WDUU4VyAsGopytJCOR2TYlX2ctiS4SrEb07VCFEXLmI+uiDfl4HSK6spzj02CHYf/IVz3qLRpCYShO3vmJ+3XiQQ=='
print decrypt_RSA('private.pem', flag)
