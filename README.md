# Mappa CLI

Mappa is a command-line interface tool that allows you to quickly perform operations on CSV and XLSX files, such as renaming header keys, remapping header positions, stripping columns, and converting headers to lowercase.

## Installation
You can install Mappa VIA pip
```bash
pip install mappa-cli
```

## Usage
The tool can be invoked using the mappa command. Below is an example of how to use Mappa, along with the available options.

### Examples
```bash
mappa --filepath [filepath] --output [output path] [options]
```

The input path and output path are optional arguments. If not provided, you will be prompted to enter the file paths during runtime. The default output file will be named filepath.mapped.csv.

You can stack multiple options in one command. However, the options will always be executed in a predefined order, regardless of how you input them. For example:

```bash
mappa --rename --remap --strip
```

## Options
`--rename`: Rename header keys
`--remap`: Remap header position
`--strip`: Strip specified columns from the table
`--lower`: Set all headers to lowercase
`--inplace`: Save changes to the same input file
`--help`: Display help

# License
This package is free to use and open for contributions under the GLWTS License, which prohibits the use of this repo for any AI or non human based training.






