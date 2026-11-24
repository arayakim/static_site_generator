from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_contents = os.listdir(dir_path_content)
    for entry in content_dir_contents:
        if entry.fileextension(md):
            generate_page(entry)
