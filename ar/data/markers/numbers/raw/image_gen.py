#Credit: https://code-maven.com/create-images-with-python-pil-pillow

from PIL import Image, ImageFont, ImageDraw

pic_dimension = (512, 512)
base_color = (244, 244, 244)
pic_filename_base = "%02d.png"
fnt_color = (0, 0, 0)
dot_size = (60, 60)
cell_wh = 140
x_offset = int((cell_wh - dot_size[0])/2)
y_offset = int((cell_wh - dot_size[1])/2)
dot_list = [(((cell_wh*(i % 3)) + x_offset, (cell_wh*int(i/3)) + y_offset), ((cell_wh*(i % 3)) + x_offset + dot_size[0], (cell_wh*int(i/3)) + y_offset + dot_size[1])) for i in range(0, 9)]
            
print(dot_list)


for i in range(0, 10):
    
    pic_filename = pic_filename_base % i
    t = str(i)
    
    img = Image.new('RGB', pic_dimension, color = base_color)
    d = ImageDraw.Draw(img)
    
    for j in range(0, i):
        d.rectangle(dot_list[j], fill=fnt_color, outline=None, width=1)
    

    print("---- Saving {}.".format(pic_filename))
    img.save(pic_filename)