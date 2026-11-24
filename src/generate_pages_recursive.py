from generate_page import generate_page
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    content_dir_contents = os.listdir(dir_path_content)

    for entry in content_dir_contents:
        full_entry_path = os.path.join(dir_path_content, entry)

        if os.path.isdir(full_entry_path):
            generate_pages_recursive(
                full_entry_path,
                template_path,
                os.path.join(dest_dir_path, entry),
                basepath
            )

        if os.path.isfile(full_entry_path):
            if entry.endswith(".md"):
                destination_file = os.path.join(
                    dest_dir_path,
                    entry.replace(".md", ".html")
                )

                generate_page(full_entry_path, template_path, destination_file, basepath)
