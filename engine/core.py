import textwrap
import urllib.request
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from engine.config import HandwritingConfig

def download_font(config):
    """Downloads the required font if it doesn't exist."""
    # Ensure assets dir exists
    os.makedirs(os.path.dirname(config.font_path), exist_ok=True)
    if not os.path.exists(config.font_path):
        print(f"[System] Downloading font to {config.font_path}...")
        urllib.request.urlretrieve(config.font_url, config.font_path)

def create_lined_paper(width=800, height=1200, line_spacing=40):
    """Creates a highly realistic lined paper background with double red margins."""
    # Slightly yellowish/off-white paper color
    img = Image.new('RGB', (width, height), color=(248, 248, 242)) 
    draw = ImageDraw.Draw(img)
    
    # Draw left double margin (Red lines, typical in notebooks)
    draw.line([(80, 0), (80, height)], fill=(220, 100, 100), width=1)
    draw.line([(85, 0), (85, height)], fill=(220, 100, 100), width=1)
    
    # Draw horizontal lines (Blue notebook lines)
    for y in range(100, height, line_spacing):
        draw.line([(0, y), (width, y)], fill=(160, 170, 220), width=1)
        
    return img

def render_handwriting(text, style_options, output_path="output.jpg"):
    """
    Main engine function. Renders text onto realistic notebook paper
    using human-like jitter, varied spacing, and ink bleed effects.
    """
    cfg = HandwritingConfig(style_options)
    download_font(cfg)
    
    try:
        font = ImageFont.truetype(cfg.font_path, cfg.font_size)
    except IOError:
        print("[Error] Font not found, using default.")
        font = ImageFont.load_default()
        
    # 1. Create Base Paper Canvas
    img = create_lined_paper(line_spacing=cfg.line_spacing)
    
    # 2. Create Transparent Text Layer (for ink blending)
    txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
    draw_txt = ImageDraw.Draw(txt_layer)
    
    # Text Wrapping Logic (Adjusted for Caveat font width ratio)
    max_chars_per_line = int(650 / (cfg.font_size * 0.40))
    lines = textwrap.wrap(text, width=max_chars_per_line)
    
    # Pen color (Dark blue/black ink with slight transparency)
    pen_color = (15, 20, 40, 240)
    
    for i, line in enumerate(lines):
        y_line = 100 + (i * cfg.line_spacing)
        words = line.split(' ')
        
        # Random starting margin for each line
        current_x = 90 + random.randint(0, 8) 
        
        for word in words:
            # Jitter Y coordinate slightly for each word to simulate human imperfection
            jitter_y = random.choice([-2, -1, 0, 1, 2])
            
            # Draw primary text
            draw_txt.text((current_x, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
            
            # Simulate heavy pen pressure by slightly offsetting the draw
            if cfg.thickness == 1:
                draw_txt.text((current_x+1, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
                
            # Calculate width to move current_x forward
            bbox = font.getbbox(word)
            word_width = bbox[2] - bbox[0]
            
            # Randomize space between words to break the "computer font" feel
            space_width = font.getbbox(' ')[2] - font.getbbox(' ')[0]
            if space_width == 0: space_width = cfg.font_size // 4
            
            current_x += word_width + space_width + random.randint(-2, 5)
            
    # 3. Apply Micro-Blur (Simulates ink spread/bleed on paper fibers)
    txt_layer = txt_layer.filter(ImageFilter.GaussianBlur(radius=0.4))
    
    # 4. Composite Text over Paper
    final_img = Image.alpha_composite(img.convert('RGBA'), txt_layer).convert('RGB')
    
    # Save output
    final_img.save(output_path)
    print(f"[SUCCESS] HandWrite output saved to {output_path}")
    return output_path
