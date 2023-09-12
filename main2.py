from tkinter import *

font_size = 48

def perform(address,watermark):
    from PIL import Image,ImageDraw,ImageFont
    image = Image.open(address)
    text = ImageDraw.Draw(image)
    x = image.size[0] - 300
    y = image.size[1] - 200
    font = ImageFont.truetype("Summer_Dreams.ttf",size=font_size)
    text.text((x,y),watermark,font=font)
    image.show()
    image.save("imaghe.jpg")


def convert():
    address = address_entry.get()
    watermark = watermark_entry.get()
    perform(address,watermark)


window = Tk()
window.title("WaterMark App")
window.minsize(width=200,height=200)


label1 = Label(text="Address")
label1.grid(column=0,row=0)

address_entry = Entry()
address_entry.grid(column=1,row=0)



label2 = Label(text="WaterMark")
label2.grid(column=0,row=1)

watermark_entry = Entry()
watermark_entry.grid(column=1,row=1)


button = Button(text="Add WaterMark",command=convert)
button.grid(column=1,row=2)




window.mainloop()



