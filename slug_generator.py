import sys
import re

def generate_slug(text):
    if not text:
        return ""


    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    return slug

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_title = sys.argv[1]
        print(f"Slug: {generate_slug(input_title)}")
    else:
        print("Please provide a title string to slugify.")