import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.core import render_handwriting

def main():
    print("="*40)
    print("🤖 HANDWRITE.AI - BASIC DEMO")
    print("="*40)
    
    text = input("\n📝 Enter text to convert:\n>> ")
    if not text:
        text = "This is a basic demo of HandWrite.ai engine. It turns normal text into handwriting!"
    
    print("\n[Using default style: Medium, Medium Pressure, Normal Spacing]")
    
    # Options dictionary (Using all defaults)
    options = {
        'gaya': '2', 'ukuran': '2', 'miring': '3',
        'tekanan': '2', 'bentuk': '1', 'spasi': '2'
    }
    
    print("\n⏳ Rendering handwriting...")
    render_handwriting(text, options, output_path="basic_output.jpg")

if __name__ == "__main__":
    main()
