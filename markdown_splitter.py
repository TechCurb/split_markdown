#!/usr/bin/env python3
"""
markdown_splitter.py - Split a Markdown file into multiple files based on header levels

Usage:
    python markdown_splitter.py --input filename.md --tag h2 --output ./split_markdown

This script reads a markdown file and splits it into multiple files,
creating a new file for each header of the specified level (H1, H2, H3, etc.).
The content under each header will be placed in its own file. Content before 
the first header will be placed in a file named "00_introduction.md".

Arguments:
    --input           - The markdown file to split (required)
    --tag            - Header level to split on: h1, h2, h3, h4, h5, h6 (default: h2)
    --output         - Directory where the split files will be saved (default: ./split_markdown)
"""

import os
import sys
import re
import argparse
from pathlib import Path

def split_markdown_by_header(input_file, output_dir='split_markdown', header_level='h2'):
    """
    Split a markdown file into separate files based on specified header level.
    
    Args:
        input_file (str): Path to the input markdown file
        output_dir (str): Directory to save the output files
        header_level (str): Header level to split on (h1, h2, h3, h4, h5, h6)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Map header level to number of # symbols
    header_map = {
        'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6
    }
    
    if header_level.lower() not in header_map:
        raise ValueError(f"Invalid header level: {header_level}. Must be one of: h1, h2, h3, h4, h5, h6")
    
    header_count = header_map[header_level.lower()]
    header_pattern = '#' * header_count
    
    # Split by specified header level
    # Regex looks for lines starting with the appropriate number of # symbols
    parts = re.split(rf'(?m)^[ \t]*{re.escape(header_pattern)}\s+', content)
    
    # The first part is content before any header of the specified level
    intro = parts[0].strip()
    if intro:
        with open(os.path.join(output_dir, '00_introduction.md'), 'w', encoding='utf-8') as f:
            f.write(intro)
    
    # Process each header section
    for i, part in enumerate(parts[1:], 1):
        # Split the first line (header) from the rest of the content
        lines = part.split('\n', 1)
        header = lines[0].strip()
        
        # Create a file name from the header
        # Replace spaces and special characters with underscores
        file_name = re.sub(r'[^\w\s-]', '', header).strip().replace(' ', '_').lower()
        file_name = f"{i:02d}_{file_name}.md"
        
        # Write the content with the header to a new file
        with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as f:
            # Add the header back with correct number of # symbols
            f.write(f"{header_pattern} {header}\n")
            # Add the rest of the content if any
            if len(lines) > 1:
                f.write(lines[1])

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description='Split a markdown file into multiple files based on header levels',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python markdown_splitter.py --input document.md
  python markdown_splitter.py --input document.md --tag h1 --output ./chapters
  python markdown_splitter.py --input document.md --tag h3 --output ./sections
        """)
    
    parser.add_argument('--input', required=True, 
                       help='Input markdown file to split')
    parser.add_argument('--tag', default='h2', 
                       choices=['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                       help='Header level to split on (default: %(default)s)')
    parser.add_argument('--output', default='split_markdown',
                       help='Directory to save the split files (default: %(default)s)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        sys.exit(1)
    
    # Split the markdown file
    split_markdown_by_header(args.input, args.output, args.tag)
    
    # Count the number of files created
    file_count = len([f for f in os.listdir(args.output) 
                     if f.endswith('.md') and os.path.isfile(os.path.join(args.output, f))])
    
    print(f"Successfully split markdown file into {file_count} files using {args.tag.upper()} headers.")
    print(f"Files saved in: {os.path.abspath(args.output)}")

if __name__ == '__main__':
    main()