"""
Configuration and validation for HandWrite.ai engine.
"""

class HandwritingConfig:
    def __init__(self, style_options):
        """
        Parses and validates the 6-parameter dictionary into workable rendering values.
        Expected keys: 'gaya', 'ukuran', 'miring', 'tekanan', 'bentuk', 'spasi'
        """
        self.raw_options = style_options
        
        # 1. Base Style (Future expansion for multiple fonts)
        self.style = style_options.get('gaya', '2')
        
        # 2. Font Size
        size_choice = style_options.get('ukuran', '2')
        if size_choice == '1':   self.font_size = 55 # Large
        elif size_choice == '3': self.font_size = 35 # Small
        else:                    self.font_size = 45 # Medium
            
        # 3. Slant
        # (Usually requires different TTF weights/italics, default to Caveat base)
        self.slant = style_options.get('miring', '3')
        
        # 4. Pressure
        self.thickness = 1 if style_options.get('tekanan', '2') == '1' else 0
        
        # 5. Shape
        self.shape = style_options.get('bentuk', '1')
        
        # 6. Spacing
        spacing_choice = style_options.get('spasi', '2')
        if spacing_choice == '2':   self.line_spacing = 60 # Wide
        elif spacing_choice == '1': self.line_spacing = 30 # Tight
        else:                       self.line_spacing = 40 # Medium

        # Base font config
        self.font_url = "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat%5Bwght%5D.ttf"
        self.font_path = "assets/handwriting_font.ttf"
