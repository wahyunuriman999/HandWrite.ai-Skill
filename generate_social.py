import sys
import os
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from engine.config import HandwritingConfig
from engine.core import download_font, create_lined_paper

def generate_social():
    print("Generating 1280x640 Social Preview...")
    
    # 1. Configuration
    opts = {'gaya': '2', 'ukuran': '1', 'miring': '3', 'tekanan': '1', 'bentuk': '1', 'spasi': '2'}
    cfg = HandwritingConfig(opts)
    download_font(cfg)
    
    # Very large font for social preview
    font_size = 90
    line_spacing = 110
    
    try: font = ImageFont.truetype(cfg.font_path, font_size)
    except: font = ImageFont.load_default()
    
    # 2. Canvas 1280 x 640
    img = create_lined_paper(width=1280, height=640, line_spacing=line_spacing)
    
    # 3. Text layer
    txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
    draw_txt = ImageDraw.Draw(txt_layer)
    
    # Text content
    text = "HandWrite.ai"
    sub_text = "Universal AI Skill for Realistic Handwriting Generation"
    
    pen_color = (15, 20, 50, 240)
    
    # Draw Main Title (HandWrite.ai)
    y_line1 = 100 + line_spacing * 2
    current_x = 120
    for word in text.split(' '):
        jitter_y = random.choice([-2, -1, 0, 1, 2])
        draw_txt.text((current_x, y_line1 - jitter_y), word, font=font, fill=pen_color, anchor="ls")
        # Boldness
        draw_txt.text((current_x+2, y_line1 - jitter_y), word, font=font, fill=pen_color, anchor="ls")
        current_x += font.getbbox(word)[2] - font.getbbox(word)[0] + 30
        
    # Draw Subtitle (smaller font)
    sub_font_size = 50
    try: sub_font = ImageFont.truetype(cfg.font_path, sub_font_size)
    except: sub_font = ImageFont.load_default()
    
    y_line2 = 100 + line_spacing * 3
    current_x = 140
    for word in sub_text.split(' '):
        jitter_y = random.choice([-1, 0, 1])
        draw_txt.text((current_x, y_line2 - jitter_y), word, font=sub_font, fill=pen_color, anchor="ls")
        current_x += sub_font.getbbox(word)[2] - sub_font.getbbox(word)[0] + 15
        
    # Apply Blur
    txt_layer = txt_layer.filter(ImageFilter.GaussianBlur(radius=0.5))
    final_img = Image.alpha_composite(img.convert('RGBA'), txt_layer).convert('RGB')
    
    # Save
    final_img.save("assets/social_preview.png")
    print("Saved as assets/social_preview.png")

if __name__ == '__main__':
    generate_social()
