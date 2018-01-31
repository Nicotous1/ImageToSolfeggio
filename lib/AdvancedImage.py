from PIL import Image

class AdvancedImage:
    countAccess = 0
    currentImg = None

    def __init__(self, link = None):
        if link == None: return
        print "Ouverture de l'image '" + link + "'..."
        AdvancedImage.currentImg = Image.open(link)


    def get(self,x,y):
        AdvancedImage.countAccess += 1
        if x < 0 or self.getWidth() <= x or y < 0 or self.getHeight() <= y: #En dehors de l'image
            return 0
        r,g,b = AdvancedImage.currentImg.getpixel((x,y))
        return int (r < 170 and g < 170 and b < 170)

    def getImg(self):
        return AdvancedImage.currentImg

    def getWidth(self):
        return AdvancedImage.currentImg.size[0]

    def getHeight(self):
        return AdvancedImage.currentImg.size[1]

    def getLen(self):
        return self.getWidth()*self.getHeight()

    def getEfficacity(self):
        return AdvancedImage.countAccess*100.0/self.getLen()