# HandWrite.ai Skill

**HandWrite.ai** is a universal AI skill (System Prompt) and Python backend engine designed to convert digital text into highly realistic handwriting on lined notebook paper. It avoids the common "alien text" pitfalls of standard AI Image Generators by using precise programmatic rendering or SVG generation.

## Repository Contents

* `SYSTEM_PROMPT.md`: The Master Prompt. Copy and paste this into any Custom GPT, Claude, or Telegram bot backend to instantly give the AI the ability to intelligently generate handwriting. It automatically falls back to SVG if the AI lacks Python execution capabilities.
* `handwrite_engine.py`: The Python backend. Use this script if you are building your own Telegram, WhatsApp, or Web Bot. It uses the `Pillow` library to render the text onto a procedurally generated lined notebook paper background using Google Fonts.

## The 6 Customization Options
The AI will ask users to select their preferred style based on:
1. Base Style (Print, Cursive, Mix, Calligraphy)
2. Size (Large, Medium, Small)
3. Slant (Right, Left, Straight)
4. Pressure (Heavy, Medium, Light)
5. Shape (Rounded, Pointed)
6. Spacing (Tight, Wide)

## How to Use the Python Script

1. Install Pillow:
   ```bash
   pip install Pillow
   ```
2. Run the script:
   ```bash
   python handwrite_engine.py
   ```
3. Follow the CLI prompts to input text and styling options. The script will output an `output_handwriting.jpg` file.
