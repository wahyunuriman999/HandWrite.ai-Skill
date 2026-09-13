from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (800, 300), color=(250, 250, 245))
draw = ImageDraw.Draw(img)

# Line at y=150
draw.line([(0, 150), (800, 150)], fill=(150, 150, 220), width=1)

try:
    font = ImageFont.truetype('handwriting_font.ttf', 40)
except:
    font = ImageFont.load_default()

# Draw text with anchor='ls'
draw.text((100, 150), "Testing baseline alignment", font=font, fill=(0,0,0), anchor="ls")

img.save('test_anchor.jpg')
