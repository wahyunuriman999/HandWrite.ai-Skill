import handwrite_engine
text = 'HandWrite.ai is a universal AI skill (System Prompt) and Python backend engine designed to convert digital text into highly realistic handwriting on lined notebook paper. It avoids the common alien text pitfalls of standard AI Image Generators by using precise programmatic rendering or SVG generation.'

# Example 1: Cursive, Medium, Medium Pressure
opts1 = {'gaya': '2', 'ukuran': '2', 'miring': '1', 'tekanan': '2', 'bentuk': '1', 'spasi': '2'}
handwrite_engine.render_handwriting(text, opts1)
import os
os.rename('output_handwriting.jpg', 'example1.jpg')

# Example 2: Print, Small, Heavy Pressure
opts2 = {'gaya': '1', 'ukuran': '3', 'miring': '3', 'tekanan': '1', 'bentuk': '2', 'spasi': '1'}
handwrite_engine.render_handwriting(text, opts2)
os.rename('output_handwriting.jpg', 'example2.jpg')
