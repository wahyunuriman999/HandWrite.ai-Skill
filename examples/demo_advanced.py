import sys
import os

# Add parent directory to path so it can import the engine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.core import render_handwriting

def main():
    print("="*40)
    print("🤖 HANDWRITE.AI - ADVANCED INTERACTIVE DEMO")
    print("="*40)
    
    text = input("\n📝 Enter text to convert:\n>> ")
    if not text:
        print("Text cannot be empty. Exiting.")
        return
    
    print("\n✨ Select your preferred handwriting style:")
    
    print("\n1. Base Style:")
    print("   [1] Print  [2] Cursive  [3] Mixed  [4] Calligraphy")
    gaya = input("   Choose (1/2/3/4) [Default 2]: ") or '2'
    
    print("\n2. Size:")
    print("   [1] Large  [2] Medium  [3] Small")
    ukuran = input("   Choose (1/2/3) [Default 2]: ") or '2'
    
    print("\n3. Slant:")
    print("   [1] Right  [2] Left  [3] Straight")
    miring = input("   Choose (1/2/3) [Default 3]: ") or '3'
    
    print("\n4. Pen Pressure:")
    print("   [1] Heavy  [2] Medium  [3] Light")
    tekanan = input("   Choose (1/2/3) [Default 2]: ") or '2'
    
    print("\n5. Shape:")
    print("   [1] Rounded  [2] Pointed")
    bentuk = input("   Choose (1/2) [Default 1]: ") or '1'
    
    print("\n6. Spacing:")
    print("   [1] Tight  [2] Wide")
    spasi = input("   Choose (1/2) [Default 2]: ") or '2'
    
    options = {
        'gaya': gaya, 'ukuran': ukuran, 'miring': miring,
        'tekanan': tekanan, 'bentuk': bentuk, 'spasi': spasi
    }
    
    print("\n⏳ Rendering handwriting...")
    render_handwriting(text, options, output_path="advanced_output.jpg")

if __name__ == "__main__":
    main()
