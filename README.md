# Markdown Splitter

A Python utility for splitting large markdown files into smaller, organized files based on header levels (H1, H2, H3, etc.).

## Overview

This tool takes a markdown file and splits it into multiple files, creating a new file for each header of the specified level. Content before the first header is saved as `00_introduction.md`. Each subsequent section is saved with a sequential number and the header text as the filename.

## Features

- Split by any header level (H1, H2, H3, H4, H5, H6)
- Automatic file naming based on header content
- Sequential numbering for predictable organization
- UTF-8 encoding support
- Customizable output directory
- Preserves original headers in split files

## Installation

No additional dependencies required - uses Python standard library only.

```bash
git clone <repository-url>
cd split_markdown
```

## Usage

### Basic Usage

```bash
python markdown_splitter.py --input filename.md --tag h2 --output ./split_markdown
```

### Parameters

- `--input` (required): Path to the input markdown file to split
- `--tag` (optional): Header level to split on (h1, h2, h3, h4, h5, h6). Default: h2
- `--output` (optional): Directory where split files will be saved. Default: `./split_markdown`

### Examples

Split a file by H2 headers (default):
```bash
python markdown_splitter.py --input my-document.md
```

Split by H1 headers with custom output directory:
```bash
python markdown_splitter.py --input large-doc.md --tag h1 --output ./chapters
```

Split by H3 headers:
```bash
python markdown_splitter.py --input detailed-guide.md --tag h3 --output ./sections
```

## Output Structure

The tool creates files with the following naming convention:

- `00_introduction.md` - Content before the first header
- `01_header_name.md` - First header section
- `02_another_header.md` - Second header section
- `03_final_section.md` - Third header section
- etc.

### File Naming Rules

- Header text is converted to lowercase
- Spaces and special characters are replaced with underscores
- Sequential numbering ensures predictable ordering
- `.md` extension is automatically added

## Example

Given an input file `project-plan.md`:

```markdown
# Project Overview
This is the introduction to our project.

## Phase 1: Planning
Details about planning phase...

## Phase 2: Development  
Development phase information...

## Phase 3: Testing
Testing procedures and guidelines...
```

Running:
```bash
python markdown_splitter.py --input project-plan.md --tag h2
```

Creates:
- `split_markdown/00_introduction.md` (contains "# Project Overview" and intro text)
- `split_markdown/01_phase_1_planning.md`
- `split_markdown/02_phase_2_development.md`
- `split_markdown/03_phase_3_testing.md`

## Help

For help and available options:
```bash
python markdown_splitter.py --help
```

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT