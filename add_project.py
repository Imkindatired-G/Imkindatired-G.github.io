import argparse
import os
import re

TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{title}</title>
  <link rel=\"stylesheet\" href=\"./css/style.css\">
  <link rel=\"stylesheet\" href=\"./css/mobile_style.css\">
</head>
<body>
  <header>
    <a href=\"index.html\" class=\"logo\" aria-label=\"Home\">
      <img src=\"./images/logofull.png\" alt=\"NW Logo\">
    </a>
    <nav aria-label=\"Main navigation\">
      <a href=\"index.html\">Home</a>
      <a href=\"resume.html\">Resume</a>
      <a href=\"projects.html\">Projects</a>
      <a href=\"contact.html\">Contact</a>
    </nav>
  </header>

  <main class=\"content\">
    <h1>{title}</h1>
    <img src=\"{thumbnail}\" alt=\"{title} thumbnail\" class=\"project-thumb\">
    <p>{description}</p>
  </main>

  <footer>
    &copy; 2025 Nolan White - Don't Look at my code, it's a mess!
  </footer>
  <script src=\"script.js\"></script>
</body>
</html>
"""

PROJECT_LIST_START = "<!-- PROJECTS-START -->"
PROJECT_LIST_END = "<!-- PROJECTS-END -->"


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip('-')


def create_project_page(slug, title, description, thumbnail):
    html = TEMPLATE.format(title=title, description=description, thumbnail=thumbnail)
    with open(f"{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)


def add_listing_to_projects(slug, title, description, thumbnail, projects_file="projects.html"):
    if not os.path.exists(projects_file):
        raise FileNotFoundError(projects_file)

    with open(projects_file, "r", encoding="utf-8") as f:
        content = f.read()

    if PROJECT_LIST_START not in content:
        # create container if not present
        insertion = f"\n<ul class=\"project-list\">\n{PROJECT_LIST_START}\n{PROJECT_LIST_END}\n</ul>\n"
        content = content.replace("<h1>Projects</h1>", "<h1>Projects</h1>" + insertion)

    listing = (
        f"  <li class=\"project-item\">\n"
        f"    <a href=\"{slug}.html\">\n"
        f"      <img src=\"{thumbnail}\" alt=\"{title} thumbnail\">\n"
        f"      <h2>{title}</h2>\n"
        f"      <p>{description}</p>\n"
        f"    </a>\n"
        f"  </li>\n")

    # insert before end marker
    new_content = content.replace(PROJECT_LIST_END, listing + PROJECT_LIST_END)

    with open(projects_file, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    parser = argparse.ArgumentParser(description="Add a project entry and page")
    parser.add_argument("title", help="Project title")
    parser.add_argument("description", help="Short description")
    parser.add_argument("thumbnail", help="Path to thumbnail image")
    args = parser.parse_args()

    slug = slugify(args.title)
    create_project_page(slug, args.title, args.description, args.thumbnail)
    add_listing_to_projects(slug, args.title, args.description, args.thumbnail)
    print(f"Created {slug}.html and updated projects.html")


if __name__ == "__main__":
    main()
