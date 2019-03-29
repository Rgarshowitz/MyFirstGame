inFile = open ('test_img.jpg' , 'rb')
outFile = open ('output_img.jpg' , 'wb')

img = inFile.read()

while len(img):
    outFile.write(img)
    img = inFile.write()

inFile.close()
outFile.close()
