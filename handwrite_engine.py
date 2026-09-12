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
    img = Image.new('RGB', (width, height), color=(250, 250, 245)) 
    draw = ImageDraw.Draw(img)
    
    # Draw left margin (Red line)
    draw.line([(80, 0), (80, height)], fill=(255, 120, 120), width=2)
    
    # Draw horizontal lines (Blue notebook lines)
    for y in range(100, height, line_spacing):
        draw.line([(0, y), (width, y)], fill=(150, 150, 220), width=1)
        
    return img

def render_handwriting(text, style_options):
    """Renders text onto the lined paper based on user preferences."""
    download_font()
    
    # --- STYLE PROCESSING BASED ON USER INPUT ---
    # Font Size
    font_size = 35
    if style_options['ukuran'] == '1':   # Besar / Large
        font_size = 45
    elif style_options['ukuran'] == '3': # Kecil / Small
        font_size = 25
        
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
    draw = ImageDraw.Draw(img)
    
    # Wrapping text to prevent overflow
    max_chars_per_line = int(650 / (font_size * 0.45))
    lines = textwrap.wrap(text, width=max_chars_per_line)
    
    # Starting coordinates (Right of the red margin, just above the first blue line)
    x_start = 100
    y_start = 100 - font_size + (line_spacing // 3)
    
    # Pen color (Dark blue/black ink)
    pen_color = (15, 20, 40)
    
    for i, line in enumerate(lines):
        y = y_start + (i * line_spacing)
        
        # Draw text
        draw.text((x_start, y), line, font=font, fill=pen_color)
        
        # If Heavy Pressure is selected, redraw slightly offset
        if thickness == 1:
            draw.text((x_start+1, y), line, font=font, fill=pen_color)
            draw.text((x_start, y+1), line, font=font, fill=pen_color)
            
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
