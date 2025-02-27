import os
import sys
import colorama as cr

def print_dir_structure(path, indent = "", prefix = ""):
    try:
        items = os.listdir(path)
        items.sort()
        for index, item in enumerate(items):
            full_path = os.path.join(path, item)
            is_last = (index == (len(items) - 1))
            current_prefix = ("└─ " if is_last else "├─ ")
            if os.path.isdir(full_path):
                print(f"{indent}{prefix}{current_prefix}{cr.Fore.BLUE}<{item}>{cr.Style.RESET_ALL}")
                new_indent = indent + ("   " if is_last else "│  ")
                print_dir_structure(full_path, new_indent, "")
            else:
                print(f"{indent}{prefix}{current_prefix}{cr.Fore.GREEN}{item}{cr.Style.RESET_ALL}")
    except Exception as e:
        print(f"{indent}{prefix}{current_prefix}{cr.Fore.RED}Error: {str(e)}{cr.Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{cr.Fore.RED}Use task_3.py <directory_path>{cr.Style.RESET_ALL}")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    if not os.path.exists(directory_path):
        print(f"{cr.Fore.RED}Path '{directory_path}' does not exist{cr.Style.RESET_ALL}")
        sys.exit(1)
    if not os.path.isdir(directory_path):
        print(f"{cr.Fore.RED}'{directory_path}' is not a directory{cr.Style.RESET_ALL}")
        sys.exit(1)
    
    root_name = os.path.basename(os.path.abspath(directory_path))
    print(f"{cr.Fore.BLUE}{root_name}{cr.Style.RESET_ALL}")
    print_dir_structure(directory_path)

if __name__ == "__main__":
    main()