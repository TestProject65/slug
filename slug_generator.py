import sys

def generate_slug(text):
    if not text:
        return ""
    # Initial basic version: leaves punctuation and special characters in place!
    return text.lower().replace(" ", "-")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_title = sys.argv[1]
        print(f"Slug: {generate_slug(input_title)}")
    else:
        print("Please provide a title string to slugify.")