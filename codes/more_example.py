#using stepic
import stepic
import os
from PIL import Image

os.chdir("F:\\graduation-project\\codes")
img=Image.open("exampleimage\\lena.png")
stego=stepic.encode(img,"excited!")
stego.save("output\\another.png")
print(stepic.decode(stego))
