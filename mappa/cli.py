import click

from .FileHandler import FileHandler
from .help import print_help

@click.command()
@click.option('--filepath', type=str, help='Specify input file path', required=False)
@click.option('--output', type=str, help='Specify output file path', required=False)
@click.option('-rename', is_flag=True, help='Rename header keys')
@click.option('-remap', is_flag=True, help='Remap header position')
@click.option('-strip', is_flag=True, help='Strip specified columns')
@click.option('-lower', is_flag=True, help='Set headers to lowercase')
@click.option('--inplace', is_flag=True, help='Save changes to the same file')
@click.option('--help', is_flag=True, help='Display help')


def main(rename, remap, strip, lower, help, filepath, output, inplace):
    if not rename and not remap and not strip and not lower and not help:
        print("No actions executed, please select an available action for execution")
        print("Use --help for more information")
        exit()
    
    if help:
        print_help()

    if not filepath:
        file_path = input("Enter the csv path: ")
    else:
        file_path = filepath

    handler = FileHandler(file_path)

    if output:
        handler.OutputPath = output + ".mapped.csv"

    if inplace:
        handler.OutputPath = file_path
    
    if rename:
        for header in handler.rename_dict:
            new_name = input(f"Enter new name for '{header}', or leave blank to leave unchanged: ")
            if new_name != "":
                handler.rename_dict[header] = new_name
        print("Confirm the following changes:")
        print(handler.rename_dict)
        confirm = input("Confirm changes? (y/n): ")
        if confirm.lower() == "y":
            handler.trigger_rename()
            handler.save_df_to_csv()
            handler.DataFrame = handler.OutputDataframe
            rename = False
        else:
            main()

    if remap:
        print("Current Header Order")
        print(handler.headers)
        new_order = input("Enter new header order separated by commas: ")
        new_order = new_order.split(",")
        if len(new_order) != len(handler.headers):
            print("New order length does not match current header length")
            main()
        for string in new_order:
            if string not in handler.headers:
                print(f"'{string}' not found in headers")
                main()
        else:
            handler.trigger_remap(new_order)
            handler.save_df_to_csv()
            handler.DataFrame = handler.OutputDataframe
            remap = False

    if strip:
        dropped_headers = []
        print(handler.headers)
        for column in handler.headers:
            drop = input(f"Drop {column}? (y/n): ")
            if drop.lower() == "y":
                dropped_headers.append(column)
        if dropped_headers:
            print("Confirm the following columns to drop:")
            print(dropped_headers)
            confirm = input("Confirm changes? (y/n): ")
            if confirm.lower() == "y":
                handler.trigger_strip(dropped_headers)
                handler.save_df_to_csv()
                handler.DataFrame = handler.OutputDataframe
                strip = False
            else:
                main()
    
    if lower:
        handler.trigger_lowercase()
        handler.save_df_to_csv()
        handler.DataFrame = handler.OutputDataframe
        lower = False
    
if __name__ == '__main__':
    main()
    

