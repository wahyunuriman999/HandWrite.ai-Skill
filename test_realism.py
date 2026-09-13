import textwrap
import urllib.request
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

FONT_URL = "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat%5Bwght%5D.ttf"
FONT_PATH = "handwriting_font.ttf"

def download_font():
    if not os.path.exists(FONT_PATH):
        urllib.request.urlretrieve(FONT_URL, FONT_PATH)

def add_noise(img):
    # Create a subtle noise layer to simulate paper texture
    import numpy as np
    img_array = np.array(img)
    noise = np.random.normal(0, 5, img_array.shape).astype(np.int16)
    noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_img)

def create_realistic_paper(width=800, height=1000, line_spacing=40):
    # slightly off-white, yellowish paper
    img = Image.new('RGB', (width, height), color=(245, 245, 238)) 
    img = add_noise(img)
    draw = ImageDraw.Draw(img)
    
    # Draw double left margin (like real indonesian notebooks)
    draw.line([(80, 0), (80, height)], fill=(220, 100, 100, 150), width=1)
    draw.line([(85, 0), (85, height)], fill=(220, 100, 100, 150), width=1)
    
    # Draw horizontal lines with slight opacity
    for y in range(100, height, line_spacing):
        draw.line([(0, y), (width, y)], fill=(120, 140, 200, 150), width=1)
        
    return img

def render_handwriting(text, style_options):
    download_font()
    
    font_size = 45 # Default
    if style_options['ukuran'] == '1':   font_size = 55
    elif style_options['ukuran'] == '3': font_size = 35
        
    line_spacing = 40
    if style_options['spasi'] == '2':   line_spacing = 60
    elif style_options['spasi'] == '1': line_spacing = 30
        
    thickness = 0
    if style_options['tekanan'] == '1': thickness = 1
        
    try: font = ImageFont.truetype(FONT_PATH, font_size)
    except: font = ImageFont.load_default()
        
    img = create_realistic_paper(height=1200, line_spacing=line_spacing)
    # create a transparent layer for text to allow ink blending
    txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)
    
    # wrapping logic
    max_chars_per_line = int(650 / (font_size * 0.40))
    lines = textwrap.wrap(text, width=max_chars_per_line)
    
    pen_color = (20, 25, 45, 230) # Dark blue ink with slight transparency
    
    for i, line in enumerate(lines):
        y_line = 100 + (i * line_spacing)
        words = line.split(' ')
        
        current_x = 95 + random.randint(-2, 2) # Random starting margin
        
        for word in words:
            # Add random jitter to Y to make it look like human handwriting
            jitter_y = random.choice([-1, 0, 1, 2])
            
            # draw word
            draw.text((current_x, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
            if thickness == 1:
                draw.text((current_x+1, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
            
            # calculate width of word and add space
            # getbbox returns (left, top, right, bottom)
            bbox = font.getbbox(word)
            word_width = bbox[2] - bbox[0]
            
            # Randomize space width slightly
            space_width = font.getsize(' ')[0] if hasattr(font, 'getsize') else font.getbbox(' ')[2]
            current_x += word_width + space_width + random.randint(-1, 3)
            
    # Apply slight blur to text to simulate ink spread
    txt_layer = txt_layer.filter(ImageFilter.GaussianBlur(radius=0.3))
    
    # Composite the text over the paper
    final_img = Image.alpha_composite(img.convert('RGBA'), txt_layer).convert('RGB')
    
    # Save
    final_img.save("output_real.jpg")

text = 'Agregat merupakan material granular, misalnya pasir, krikil, batu pecah dan kerak tungku pijar yang dipakai bersama-sama dengan suatu media pengikat untuk membentuk suatu beton atau adukan semen hidrolik. Secara garis besar agregat berfungsi sebagai bahan dari campuran mortar atau beton dan untuk menghasilkan kekuatan yang besar pada beton. Agregat dapat dikatakan baik apabila memiliki sifat berupa butiran yang keras, kompak, tidak pipih, dan kekal.'
opts = {'gaya': '1', 'ukuran': '2', 'miring': '3', 'tekanan': '1', 'bentuk': '1', 'spasi': '1'}
render_handwriting(text, opts)
