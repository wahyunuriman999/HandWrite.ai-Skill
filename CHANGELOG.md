# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-13
### Added
- **Human Jitter Engine**: Word-by-word rendering with random Y-axis jitter.
- **Dynamic Spacing**: Randomized X-axis spacing to mimic natural human writing rhythm.
- **Ink Bleed Effect**: Micro Gaussian Blur applied to text layer for realistic ink-on-paper look.
- **Realistic Paper**: Off-white/yellowish base paper with double-lined red margins (standard Indonesian notebook style).
- **Strict Interactive Mode**: Overhauled `SYSTEM_PROMPT.md` to aggressively block autonomous ChatGPT execution, forcing questionnaire compliance.

## [1.0.0] - 2026-09-13
### Added
- Initial release of HandWrite.ai Master Prompt.
- `handwrite_engine.py` script for basic Pillow-based text rendering.
- 6 parameter configuration system (Style, Size, Slant, Pressure, Shape, Spacing).
- SVG fallback for AIs without Code Interpreter.
