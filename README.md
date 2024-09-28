# README

## SVG to PNG Converter (`svg_to_png.py`)

A Python script to batch convert SVG files into PNG icons of specified sizes (only x by x sizes).

### Features

- **Batch Processing**: Converts all SVG files in the input directory.
- **Customizable Sizes**: Generate PNGs in multiple sizes.
- **Idempotent**: Skips conversion if the PNG already exists.
- **Command-Line Interface**: Easy to integrate into scripts or workflows.

## Prerequisites

- **Python 3.x**
- **CairoSVG**: Install via pip.

  ```bash
  pip install cairosvg
  ```

## Usage

### Basic Usage

Run the script with default settings:

```bash
python3 svg_to_png.py
```

- **Input Directory**: Current directory (`svgs/`)
- **Output Directory**: `pngs/`
- **Sizes**: `16`, `32`, `64`, `128`, `256`

### Custom Input and Output Directories

Specify custom directories using `-i` and `-o`:

```bash
python3 svg_to_png.py -i /path/to/input -o /path/to/output
```

### Custom Icon Sizes

Specify custom sizes using `-s` followed by space-separated integers:

```bash
python3 svg_to_png.py -s 24 48 96
```

### Full Example

Combine all options:

```bash
python3 svg_to_png.py -i ./svgs -o ./icons -s 16 32 64 128 256
```

## Command-Line Arguments

- `-i`, `--input_dir`: Input directory containing SVG files (default: `.`).
- `-o`, `--output_dir`: Output directory for PNG icons (default: `icons`).
- `-s`, `--sizes`: Space-separated list of icon sizes to generate (default: `16 32 64 128 256`).

## Notes

- **File Naming Convention**: Output files are named `[original_name]_[size]x[size].png`.
- **Skipping Existing Files**: The script will skip generating a PNG if it already exists in the output directory.
- **Permissions**: Ensure you have read/write permissions for the input and output directories.

## Troubleshooting

- **Module Not Found**: If `cairosvg` is not found, ensure it's installed in your Python environment.
- **Dependency Issues**: If you encounter errors related to Cairo or Pango, verify that all dependencies are correctly installed.
- **WSL Specifics**: In WSL, ensure your Linux environment is updated and has access to necessary system libraries.

  ```bash
  sudo apt-get update
  sudo apt-get install libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0
  ```

## License

This script is released under the MIT License.

## Acknowledgments

- **CairoSVG**: For SVG to PNG conversion capabilities.

# Shortcuts

If you're in a hurry:

1. **Install Dependencies**

   ```bash
   pip install cairosvg
   sudo apt-get install libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0
   ```

2. **Run Script with Defaults**

   ```bash
   python3 svg_to_png.py
   ```

3. **Find Your PNG Icons**

   Icons will be in the `icons/` directory.

---

Enjoy your newly generated PNG icons!