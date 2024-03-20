import base64

text_toEncode = "we are to encode this text"
encoded_text = text_toEncode.encode("ascii")

encodebase64 = base64.b64encode(encoded_text)

print(encodebase64)

# encoding image file into text
with open('suv.jpeg', 'rb') as file:
    suv = file.read()

with open('savedsub.jpeg', 'wb') as file:
    file.write(suv)

"""
The above looks ok, but for some protocols that accept only string base, this will be a problem as the image will not
be intepreted as required. hence the need for the base64 encoding system. lets encode the above and decode as well
"""
# from the byes obtained {suv}, take those bytes into a base64 encoding system
b64Encode = base64.b64encode(suv)

decodedval = base64.b64decode(b64Encode)
with open('suv_encoded_string', 'w') as f:
    f.write(str(b64Encode))
    