#Credit: https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python

from PIL import Image

img_list = ['pattern-0{}.png'.format(i) for i in range(0, 10)] + ['pattern-01.png']

img_pos_list = [((i % 4)*200, int(i/4)*200) for i in range(0, 11)]

visible_list = [[i] for i in range(0, 10)]
visible_list = visible_list + [[1, 10], [1, 3]]
print(visible_list)

for i, v in enumerate(visible_list):
    output_filename = "markertest_%d.png" % i
    background = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
    
    for j in v:
        img = Image.open(img_list[j], 'r')
        img.thumbnail((200, 200), Image.ANTIALIAS)
        
        offset = img_pos_list[j]
        
        background.paste(img, offset)
        
    background.save(output_filename)