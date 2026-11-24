def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.removeprefix("# ").strip()
            return title

    raise Exception("missing title")
