import os
import sys
import pwd
import argparse

def count_files_by_owner(directory):
    owner_counts = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            owner = os.stat(file_path).st_uid
            owner_name = pwd.getpwuid(owner).pw_name  # Get the username from UID

            if owner_name not in owner_counts:
                owner_counts[owner_name] = 0
            owner_counts[owner_name] += 1

    return owner_counts

def main():
    parser = argparse.ArgumentParser(description="Count files by owner and list files for a specific user.")
    parser.add_argument("directory", help="The directory to search for files.")
    parser.add_argument("-u", "--user", help="Specify a user to filter files by owner.")
    args = parser.parse_args()

    search_dir = args.directory
    owner_filter = args.user

    if owner_filter:
        owned_files = []
        for root, _, files in os.walk(search_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                owner = os.stat(file_path).st_uid
                owner_name = pwd.getpwuid(owner).pw_name  # Get the username from UID
                if owner_name == owner_filter:
                    owned_files.append(file_path)

        if not owned_files:
            print(f"No files found for owner: {owner_filter}")
        else:
            print(f"Files owned by {owner_filter}:")
            for file in owned_files:
                print(file)
    else:
        for owner, count in count_files_by_owner(search_dir).items():
            print(f"Owner: {owner}, File Count: {count}")

if __name__ == "__main__":
    main()
