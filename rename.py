import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('Nyx', 'Operon')
        new_content = new_content.replace('nyx', 'operon')
        new_content = new_content.replace('NYX', 'OPERON')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated content in {filepath}")
    except Exception as e:
        print(f"Could not process {filepath}: {e}")

def rename_paths(root_dir):
    # Rename files and directories bottom-up
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if '.git' in root:
            continue
            
        # Rename files
        for filename in files:
            if 'nyx' in filename.lower():
                old_path = os.path.join(root, filename)
                new_filename = filename.replace('Nyx', 'Operon').replace('nyx', 'operon').replace('NYX', 'OPERON')
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed file {old_path} -> {new_path}")
                
        # Rename directories
        for dirname in dirs:
            if 'nyx' in dirname.lower():
                old_path = os.path.join(root, dirname)
                new_dirname = dirname.replace('Nyx', 'Operon').replace('nyx', 'operon').replace('NYX', 'OPERON')
                new_path = os.path.join(root, new_dirname)
                os.rename(old_path, new_path)
                print(f"Renamed directory {old_path} -> {new_path}")

root_dir = r"d:\NYX-main"
# First update file contents
for root, dirs, files in os.walk(root_dir):
    if '.git' in root:
        continue
    for file in files:
        if file == 'rename.py':
            continue
        filepath = os.path.join(root, file)
        replace_in_file(filepath)

# Then rename files and directories
rename_paths(root_dir)
