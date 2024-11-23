import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def create_auth_file(directory):
    auth_file_path = os.path.join(directory, "auth.txt")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    try:
        with open(auth_file_path, "w") as file:
            file.write(f"{username}\n{password}\n")
        print(f"'auth.txt' created or updated at: {auth_file_path}")
        return auth_file_path
    except Exception as e:
        print(f"Error creating or updating 'auth.txt': {e}")
        return None

def modify_ovpn_file(file_path, auth_file_absolute_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        line_modified = False
        for i, line in enumerate(lines):
            if line.strip().startswith("auth-user-pass"):
                lines[i] = f"auth-user-pass {auth_file_absolute_path}\n"
                line_modified = True
                break
        
        if not line_modified:
            lines.append(f"auth-user-pass {auth_file_absolute_path}\n")
        
        with open(file_path, "w") as file:
            file.writelines(lines)
        
        print(f"Modified: {file_path}")
    except Exception as e:
        print(f"Error modifying '{file_path}': {e}")

def modify_ovpn_files(directory, auth_file_path):
    auth_file_absolute_path = os.path.abspath(auth_file_path)
    ovpn_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".ovpn")]

    with ThreadPoolExecutor() as executor:
        executor.map(modify_ovpn_file, ovpn_files, [auth_file_absolute_path] * len(ovpn_files))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify .ovpn files in the specified directory.")
    parser.add_argument("-d", "--directory", required=True, help="Directory containing .ovpn files.")
    parser.add_argument("-a", "--auth", help="Path to the auth.txt file to set.")
    parser.add_argument("-ac", "--auth-create", action="store_true", help="Create or update auth.txt in the directory.")

    args = parser.parse_args()
    directory_absolute_path = os.path.abspath(args.directory)

    if args.auth_create:
        auth_file_path = create_auth_file(directory_absolute_path)
        if auth_file_path:
            modify_ovpn_files(directory_absolute_path, auth_file_path)
    elif args.auth:
        modify_ovpn_files(directory_absolute_path, args.auth)
    else:
        print("Error: You must specify --auth or --auth-create.")
