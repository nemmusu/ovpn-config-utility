
# OVPN Config Utility

This script is designed to simplify the management of `.ovpn` files by adding or modifying the `auth-user-pass` line in each file within a specified directory. It is particularly useful when you have multiple `.ovpn` files and need to configure them to use a specific `auth.txt` file for authentication.

## Features

- **Modify Existing `auth-user-pass` Lines**: Updates the `auth-user-pass` line in `.ovpn` files to use a specific `auth.txt` file.
- **Add `auth-user-pass` Line**: If the line doesn't exist, it appends the correct configuration to the file.
- **Create an `auth.txt` File**: Use the interactive mode to create an `auth.txt` file directly in the directory.

## Prerequisites

- Python 3 installed on your system.

## Usage

### 1. Modify `.ovpn` Files with an Existing `auth.txt`
If you already have an `auth.txt` file, use the following command:
```bash
python ovpn_utility.py -d /path/to/ovpn_files -a /path/to/auth.txt
```
This will modify all `.ovpn` files in the `/path/to/ovpn_files` directory to point to the specified `auth.txt` file.

### 2. Create an `auth.txt` File and Modify `.ovpn` Files
If you want to create a new `auth.txt` file interactively and apply it to your `.ovpn` files:
```bash
python ovpn_utility.py -d /path/to/ovpn_files --auth-create
```
You will be prompted to enter a username and password. The script will:
1. Create an `auth.txt` file in the `/path/to/ovpn_files` directory.
2. Modify all `.ovpn` files to use the newly created `auth.txt`.

### Example
Suppose you have a directory `/home/user/ovpn_configs` containing multiple `.ovpn` files and you want to create or use an `auth.txt` file for them:
- To create a new `auth.txt` file and update all `.ovpn` files:
  ```bash
  python ovpn_utility.py -d /home/user/ovpn_configs --auth-create
  ```
- To use an existing `auth.txt` file:
  ```bash
  python ovpn_utility.py -d /home/user/ovpn_configs -a /home/user/auth.txt
  ```

### After Execution
Each `.ovpn` file in the directory will have the line:
```
auth-user-pass /absolute/path/to/auth.txt
```
If the line already exists, it will be updated. If not, it will be appended to the file.

## Notes

- Ensure you have the necessary permissions to modify `.ovpn` files in the specified directory.
- The script will only process files with the `.ovpn` extension.

