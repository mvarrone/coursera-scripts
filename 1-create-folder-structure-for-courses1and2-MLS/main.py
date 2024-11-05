import os
import json
import re
import time


def load_json_file(file_path):
    """Loads a JSON file and returns the data."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"The file '{file_path}' is not a valid JSON file.")
    return None


def get_nested_data(data, keys):
    """Retrieves nested data from a dictionary given a list of keys."""
    for key in keys:
        print(f"key: {key}")
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data


def sanitize_name(name):
    """Sanitizes a string to be a valid directory name."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " -", name)
    name = re.sub(r"[^a-zA-Z0-9 \-_]", "", name)
    return name.strip()


def create_folders(data, file_path):
    """Creates numbered folders and subfolders based on the elements in the data list."""
    folder_name = sanitize_name(
        os.path.splitext(os.path.basename(file_path))[0])
    main_folder_path = folder_name
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
        print(f"\nMain folder '{main_folder_path}' created.")
        create_readme_file(main_folder_path)
    else:
        print(f"Main folder '{main_folder_path}' already exists.")

    if data:
        for i, info in enumerate(data):
            week_folder_name = f"week{i + 1}-{sanitize_name(info.get('name'))}"
            if week_folder_name:
                week_folder_path = os.path.join(
                    main_folder_path, week_folder_name)
                if not os.path.exists(week_folder_path):
                    os.makedirs(week_folder_path)
                    print(f"Folder '{week_folder_path}' created.")
                    create_readme_file(week_folder_path)
                else:
                    print(f"Folder '{week_folder_path}' already exists.")

                # Create numbered subfolders for nested elements
                for j, element in enumerate(info.get("elements", [])):
                    subfolder_name = f"{
                        j + 1:02d}-{sanitize_name(element.get('name'))}"
                    if subfolder_name:
                        subfolder_path = os.path.join(
                            week_folder_path, subfolder_name)
                        if not os.path.exists(subfolder_path):
                            os.makedirs(subfolder_path)
                            print(f"Subfolder '{subfolder_path}' created.")
                            create_readme_file(subfolder_path)
                        else:
                            print(f"Subfolder '{
                                  subfolder_path}' already exists.")


def create_readme_file(folder_path):
    """Creates a README.md file inside the given folder."""
    readme_file_path = os.path.join(folder_path, "README.md")
    with open(readme_file_path, "w") as readme_file:
        readme_file.write("# Empty Folder\n\nThis folder is currently empty.")
        print(f"README.md created inside '{folder_path}'.")


def main() -> None:
    files: list[str] = ["course1.json", "course2.json"]
    nested_keys: list[str] = [
        "context",
        "dispatcher",
        "stores",
        "CourseStore",
        "rawCourseMaterials",
        "courseMaterialsData",
        "elements",
    ]

    for file_path in files:
        data = load_json_file(file_path)
        if data:
            result = get_nested_data(data, nested_keys)
            if result is not None:
                create_folders(result, file_path)
            else:
                print("Key not found")
                print(data)


if __name__ == "__main__":
    start = time.time()

    main()

    total = (time.time() - start) * 1000
    print(f"\nElapsed time: {total:.2f} ms")
