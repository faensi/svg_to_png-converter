#!/usr/bin/env python3

import os
import argparse
import cairosvg

def generate_icons(input_svg, sizes, output_dir):
    svg_filename = os.path.basename(input_svg)
    svg_name, _ = os.path.splitext(svg_filename)
    
    for size in sizes:
        output_png = os.path.join(output_dir, f'{svg_name}_{size}x{size}.png')
        if not os.path.exists(output_png):
            cairosvg.svg2png(url=input_svg, write_to=output_png, output_width=size, output_height=size)
            print(f'Generated {output_png}')
        else:
            print(f'Skipped {output_png}, already exists.')

def main():
    parser = argparse.ArgumentParser(description='Convert SVG files to PNG icons of specified sizes.')
    parser.add_argument('-i', '--input_dir', default='svgs', help='Input directory containing SVG files.')
    parser.add_argument('-o', '--output_dir', default='pngs', help='Output directory for PNG icons.')
    parser.add_argument('-s', '--sizes', nargs='+', type=int, default=[16, 32, 64, 128, 256],
                        help='List of icon sizes to generate.')
    
    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    sizes = args.sizes
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    svg_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.svg')]
    
    for svg_file in svg_files:
        input_svg_path = os.path.join(input_dir, svg_file)
        svg_name, _ = os.path.splitext(svg_file)
        
        # Check if any PNG files for this SVG exist in the output directory
        png_exists = any(
            os.path.exists(os.path.join(output_dir, f'{svg_name}_{size}x{size}.png')) for size in sizes
        )
        
        if not png_exists:
            generate_icons(input_svg_path, sizes, output_dir)
        else:
            print(f'Skipped {svg_file}, PNG versions already exist in output directory.')

if __name__ == "__main__":
    main()
