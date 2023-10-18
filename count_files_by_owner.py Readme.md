
# File Count by Owner and List Files (Python)

## Overview

This Python script allows you to count files in a directory and its subdirectories based on their ownership. It can also list files owned by a specific user if provided. This tool can be useful for identifying the distribution of files among different users in a directory.

## Usage

To use this script, follow the instructions below:

1. Ensure you have Python installed on your system.

2. Download the `count_files_by_owner.py` script to your desired location.

3. Open a terminal and navigate to the directory where the script is located.

4. Run the script with the following command:

   ```bash
   python count_files_by_owner.py <directory> [-u <username>]
   ```

   - `<directory>`: The directory to search for files.
   - `-u, --user <username>` (Optional): Specify a user to filter files by owner.

   If you provide the `-u` flag followed by a username, the script will display the files owned by that specific user. If the `-u` flag is not provided, the script will display counts for all owners and list their respective files.

5. If the `-u` flag is used, the script will display the files owned by the specified user.

## Expected Output Examples

### Count Files by Owner (Default)

If you run the script without specifying the `-u` flag, it will display counts for all owners and list the counts for each owner. For example:

```bash
$ python count_files_by_owner.py /path/to/directory

Owner: user1, File Count: 10
Owner: user2, File Count: 7
Owner: user3, File Count: 5
Owner: user4, File Count: 12
```

### List Files for a Specific User

If you use the `-u` flag to specify a user, the script will display the files owned by that user. For example:

```bash
$ python count_files_by_owner.py /path/to/directory -u user1

Files owned by user1:
/path/to/directory/file1.txt
/path/to/directory/subdir/file2.txt
```

### No Files Found for a Specific User

If you specify a user with the `-u` flag, but there are no files owned by that user in the directory, the script will inform you:

```bash
$ python count_files_by_owner.py /path/to/directory -u non_existent_user

No files found for owner: non_existent_user
```

## License

This script is provided under an open-source license. Feel free to modify and use it as needed.

## Issues and Contributions

If you encounter any issues with this script or have suggestions for improvements, please create an issue or pull request on the GitHub repository.

You can replace `/path/to/directory` with the actual directory path when running the script, and the script's behavior will match the provided examples.