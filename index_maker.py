import os
EXCLUDE_DIR=['.git']
def generate_index(path, indent=0):
    """Recursively generates a Markdown index of files in the specified directory."""
    # Get a list of entries in the directory
    entries = os.listdir(path)
    entries.sort()  # Sort entries for consistent ordering

    index = []

    for entry in entries:
        if entry in EXCLUDE_DIR:
            continue
        full_path = os.path.join(path, entry)
        # Check if the entry is a directory
        if os.path.isdir(full_path):
            # Add a link to the directory
            index.append(' ' * indent + f"- [{entry}]({full_path}/README.md)".replace('\\','/'))  # Assuming each directory has a README.md
            # Recursively generate index for the directory
            index.extend(generate_index(full_path, indent + 2))
        else:
            # Add a link to the file
            index.append(' ' * indent + f"- [{entry}]({full_path})")

    return index

def save_index_to_md(index, output_file):
    """Saves the generated index to a Markdown file."""
    with open(output_file, 'w') as f:
        f.write("# PYTHON CHEAT SHEET INDEX\n\n")
        f.write('\n'.join(index))

if __name__ == "__main__":
    # Specify the path to your project folder
    project_folder = "./"  # Change this to your project folder path
    output_file = "README.md"  # Output file for the index

    # Generate the index
    index = generate_index(project_folder)

    # Save the index to a Markdown file
    save_index_to_md(index, output_file)

    print(f"Index created successfully in '{output_file}'")
