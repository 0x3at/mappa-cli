def print_help():
    print("""
    ___  ___                            _____            ___  ___            _             _       _             
    |  \/  |                        _  /  __ \           |  \/  |           (_)           | |     | |             
    | .  . | __ _ _ __  _ __   __ _(_) | /  \/_____   __ | .  . | __ _ _ __  _ _ __  _   _| | __ _| |_ ___  _ __ 
    | |\/| |/ _` | '_ \| '_ \ / _` |   | |   / __\ \ / / | |\/| |/ _` | '_ \| | '_ \| | | | |/ _` | __/ _ \| '__|
    | |  | | (_| | |_) | |_) | (_| |_  | \__/\__ \\ V /  | |  | | (_| | | | | | |_) | |_| | | (_| | || (_) | |   
    \_|  |_/\__,_| .__/| .__/ \__,_(_)  \____|___/ \_/   \_|  |_/\__,_|_| |_|_| .__/ \__,_|_|\__,_|\__\___/|_|   
                | |   | |                                                    | |                                
                |_|   |_|                                                    |_|                                
    """)
    print("Mappa allows you to perform quick operations on csv and xlsx files:")
    print("1. Rename header keys")
    print("2. Remap header position")
    print("3. Strip specified columns from the table")
    print("4. Set all headers to lowercase\n")
    print("""
    _   _                        
    ( ) ( )                       
    | | | | ___   _ _   __    __  
    | | | /',__)/'_` )/'_ `\/'__`\ 
    | (_) \__, ( (_| ( (_) (  ___/ 
    (_____(____`\__,_`\__  `\____) 
                    ( )_) |       
                    \___/'      
            """)
    print("Input path and output path are optional arguments, input will be captured during runtime and output will be default (filepath.mapped.csv) if not provided")
    print("EX: mappa --filepath [filepath] --output [output] [options]")
    print("Options can be stacked but will be executed in the below order regardless of input order")
    print("EX: mappa --rename --remap --strip")
    print("""
    _____       _                       
    (  _  )     ( )_ _                  
    | (_) |  ___| ,_(_)  _    ___   ___ 
    |  _  |/'___| | | |/'_`\/' _ `/',__)
    | | | ( (___| |_| ( (_) | ( ) \__, \ 
    (_) (_`\____`\__(_`\___/(_) (_(____/
                                                                             
    """)
    print("-rename: Rename header keys")
    print("-remap: Remap header position")
    print("-strip: Strip specified columns")
    print("-lower: Set headers to lowercase")
    print("""
 _____       _                      
(  _  )     ( )_ _                  
| ( ) |_ _  | ,_(_)  _    ___   ___ 
| | | ( '_`\| | | |/'_`\/' _ `/',__)
| (_) | (_) | |_| ( (_) | ( ) \__, \)
(_____| ,__/`\__(_`\___/(_) (_(____/
      | |                           
      (_)                                                    
    """)
    print("--inplace: Save changes to the same input file")
    print("--help: Display help")
    exit()
