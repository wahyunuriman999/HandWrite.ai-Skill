import sys
import os

# Add parent directory to path so it can import the engine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.core import render_handwriting

def test_render():
    print("Running automated test for HandWrite.ai Engine...")
    text = "This is an automated test to ensure the engine works in CI/CD pipelines."
    options = {
        'gaya': '2', 'ukuran': '2', 'miring': '3',
        'tekanan': '1', 'bentuk': '1', 'spasi': '2'
    }
    
    # Run the engine
    output_path = "test_output.jpg"
    result = render_handwriting(text, options, output_path=output_path)
    
    assert os.path.exists(result), "Output image was not generated!"
    print("Test passed successfully!")

if __name__ == "__main__":
    test_render()
