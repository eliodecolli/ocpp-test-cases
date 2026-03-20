from pypdf import PdfReader
from os import path
import re

if __name__ == "__main__":
    reader = PdfReader("ocpp.pdf")

    pages = []

    # TODO: Rename this to the module you want to encounter
    folder = "datatransfer"
    file_name = path.join(folder, "intro.txt")

    for i in range(356, 362):
        pages.append(reader.pages[i].extract_text())

    buffer = "\n".join(pages)

    # Split on section headers like "B01 - ", "B02 - ", etc.

    # TODO: Replace the literal "P" here with the index character of the module you want to use.
    pattern = r'(?=P\d{2}\s*-\s)'

    first_match = re.search(pattern, buffer)
    intro = buffer[:first_match.start()] if first_match else buffer

    raw_sections = re.split(pattern, buffer[first_match.start():]) if first_match else []

    # Merge chunks that share the same <Index>XX id (caused by repeated page headers)
    merged = {}
    order = []
    for chunk in raw_sections:

        # TODO: Same as above.
        m = re.match(r'(P\d{2})', chunk)

        if not m:
            continue
        key = m.group(1)
        if key not in merged:
            merged[key] = chunk
            order.append(key)
        else:
            merged[key] += chunk

    sections = [merged[k] for k in order]

    for section_id, section in zip(order, sections):
        name = f"{section_id}.txt"
        with open(path.join(folder, name), "w", encoding="utf-8") as f:
            f.write(section)

    with open(file=file_name, mode="w", encoding="utf-8") as f:
        f.write(intro)
