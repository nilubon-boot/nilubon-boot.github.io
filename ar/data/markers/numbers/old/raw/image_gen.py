#Credit: https://code-maven.com/create-images-with-python-pil-pillow

from PIL import Image, ImageFont, ImageDraw

pic_dimension = (512, 512)
base_color = (244, 244, 244)
fnt_size = 400
fnt_color = (0, 0, 0)
fnt = ImageFont.truetype('./Open_Sans/OpenSans-Regular.ttf', fnt_size)
pic_filename_base = "%02d.png"

dot_pos_list = [[(15, 15), (45, 45)], 
                [(452, 452), (497, 497)], 
                [(437, 15), (497, 75)], 
                [(15, 447), (60, 497)], 
                [(467, 152), (497, 182)],
                [(15, 319), (60, 364)],
                [(15, 141), (75, 201)],
                [(452, 319), (497, 364)],
                [(241, 15), (271, 45)]
                ]

for i in range(0, 10):
    
    pic_filename = pic_filename_base % i
    t = str(i)
    
    img = Image.new('RGB', pic_dimension, color = base_color)
    d = ImageDraw.Draw(img)
    w, h = d.textsize(t, font=fnt)
    d.text((int(pic_dimension[0]/2) - int(w/2), pic_dimension[1] - h - 15), t, font=fnt, fill=fnt_color)
    
    if(i > 0):
        point_pos = dot_pos_list[i - 1]
        d.rectangle(point_pos, fill=fnt_color, outline=None, width=1)

    print("---- Saving {}.".format(pic_filename))
    img.save(pic_filename)