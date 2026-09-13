import textwrap
import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont

# 1. URL for handwriting font (Caveat)
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat%5Bwght%5D.ttf"
FONT_PATH = "handwriting_font.ttf"

def download_font():
    """Downloads the required font if it doesn't exist in the directory."""
    if not os.path.exists(FONT_PATH):
        print("[System] Downloading handwriting font...")
        urllib.request.urlretrieve(FONT_URL, FONT_PATH)

def create_lined_paper(width=800, height=1000, line_spacing=40):
    """Creates a realistic lined paper background."""
    img = Image.new('RGB', (width, height), color=(248, 248, 242)) # Slightly yellowish/off-white
    draw = ImageDraw.Draw(img)
    
    # Draw left double margin (Red lines, typical in Indonesian notebooks)
    draw.line([(80, 0), (80, height)], fill=(220, 100, 100), width=1)
    draw.line([(85, 0), (85, height)], fill=(220, 100, 100), width=1)
    
    # Draw horizontal lines (Blue notebook lines, slightly transparent/lighter)
    for y in range(100, height, line_spacing):
        draw.line([(0, y), (width, y)], fill=(160, 170, 220), width=1)
        
    return img

def render_handwriting(text, style_options):
    """Renders text onto the lined paper based on user preferences."""
    download_font()
    
    # --- STYLE PROCESSING BASED ON USER INPUT ---
    # Font Size
    font_size = 50 # Default (Medium)
    if style_options['ukuran'] == '1':   # Besar / Large
        font_size = 65
    elif style_options['ukuran'] == '3': # Kecil / Small
        font_size = 35
        
    # Spacing
    line_spacing = 40
    if style_options['spasi'] == '2':    # Lebar / Wide
        line_spacing = 60
    elif style_options['spasi'] == '1':  # Rapat / Tight
        line_spacing = 30
        
    # Pressure (Thickness simulation)
    thickness = 0
    if style_options['tekanan'] == '1':  # Kuat / Heavy
        thickness = 1
        
    # ---------------------------------------------
    
    # Load Font
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except IOError:
        print("[Error] Font not found, using default font.")
        font = ImageFont.load_default()
        
    # Create Canvas
    img = create_lined_paper(line_spacing=line_spacing)
    
    # Create transparent text layer for ink blending
    txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
    draw_txt = ImageDraw.Draw(txt_layer)
    
    # Wrapping text to prevent overflow
    max_chars_per_line = int(650 / (font_size * 0.40))
    lines = textwrap.wrap(text, width=max_chars_per_line)
    
    # Pen color (Dark blue/black ink with slight transparency)
    pen_color = (15, 20, 40, 240)
    
    import random
    
    for i, line in enumerate(lines):
        y_line = 100 + (i * line_spacing)
        words = line.split(' ')
        
        # Random starting margin for each line
        current_x = 90 + random.randint(0, 8) 
        
        for word in words:
            # Jitter Y coordinate slightly for each word to simulate human imperfection
            jitter_y = random.choice([-2, -1, 0, 1, 2])
            
            draw_txt.text((current_x, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
            
            if thickness == 1:
                draw_txt.text((current_x+1, y_line - jitter_y), word, font=font, fill=pen_color, anchor="ls")
                
            # Get word width
            bbox = font.getbbox(word)
            word_width = bbox[2] - bbox[0]
            
            # Randomize space between words
            space_width = font.getbbox(' ')[2] - font.getbbox(' ')[0]
            if space_width == 0: space_width = font_size // 4
            
            current_x += word_width + space_width + random.randint(-2, 5)
            
    # Apply slight blur to simulate ink spread onto paper
    from PIL import ImageFilter
    txt_layer = txt_layer.filter(ImageFilter.GaussianBlur(radius=0.4))
    
    # Composite
    img = Image.alpha_composite(img.convert('RGBA'), txt_layer).convert('RGB')
    
    # Save output
    output_path = "output_handwriting.jpg"
    img.save(output_path)
    print(f"\n[SUCCESS] Handwriting image saved as '{output_path}'")

def main():
    print("="*40)
    print("🤖 HANDWRITE.AI GENERATOR")
    print("="*40)
    
    text = input("\n📝 Enter text to convert:\n>> ")
    
    print("\n✨ Select your preferred handwriting style:")
    
    print("\n1. Base Style:")
    print("   [1] Print  [2] Cursive  [3] Mixed  [4] Calligraphy")
    gaya = input("   Choose (1/2/3/4): ")
    
    print("\n2. Size:")
    print("   [1] Large  [2] Medium  [3] Small")
    ukuran = input("   Choose (1/2/3): ")
    
    print("\n3. Slant:")
    print("   [1] Right  [2] Left  [3] Straight")
    miring = input("   Choose (1/2/3): ")
    
    print("\n4. Pen Pressure:")
    print("   [1] Heavy  [2] Medium  [3] Light")
    tekanan = input("   Choose (1/2/3): ")
    
    print("\n5. Shape:")
    print("   [1] Rounded  [2] Pointed")
    bentuk = input("   Choose (1/2): ")
    
    print("\n6. Spacing:")
    print("   [1] Tight  [2] Wide")
    spasi = input("   Choose (1/2): ")
    
    # Options dictionary
    options = {
        'gaya': gaya, 'ukuran': ukuran, 'miring': miring,
        'tekanan': tekanan, 'bentuk': bentuk, 'spasi': spasi
    }
    
    print("\n⏳ Rendering handwriting...")
    render_handwriting(text, options)

if __name__ == "__main__":
    main()
