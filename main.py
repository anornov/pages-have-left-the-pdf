from pypdf import PdfReader, PdfWriter


def delete_pdf_pages(input_pdf, output_pdf, individual_pages, ranges):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        total_pages = len(reader.pages)

        indices_to_delete = set()

        for p in individual_pages:
            indices_to_delete.add(p - 1)

        for start, end in ranges:
            for p in range(start, end + 1):
                indices_to_delete.add(p - 1)

        for i in range(total_pages):
            if i not in indices_to_delete:
                writer.add_page(reader.pages[i])

        with open(output_pdf, "wb") as final_file:
            writer.write(final_file)

        final_pages = total_pages - len(indices_to_delete)
        print(f"\n[SUCCESS] Process completed."
              f"The new PDF '{output_pdf}' has {final_pages} pages.")

    except FileNotFoundError:
        print(f"\n[ERROR] File Not Found '{input_pdf}'."
              " Make sure you are in the correct folder.")
    except Exception as e:
        print(f"\n[ERROR] Something goes wrong: {e}")


print("--- Fill in the following form ---\n")

prompt1 = (
    "1. Name of the original PDF file (e.g., entry.pdf): "
)
source_file = input(prompt1).strip()

prompt2 = (
    "2. Name of the new PDF to be generated (e.g., result.pdf): "
)
resulting_file = input(prompt2).strip()

prompt3 = (
    "3. Individual pages to delete (e.g., 3, 6)"
    "or press Enter if there are none: "
)
input_pages = input(prompt3).strip()
loose_pages_to_delete = []
if input_pages:
    loose_pages_to_delete = [
        int(p.strip()) for p in input_pages.split(",") if p.strip().isdigit()]

prompt4 = (
    "4. Ranges to delete (e.g., 10-14)"
    "or press Enter if there are none: "
)
ranges_input = input(prompt4).strip()
ranges_to_delete = []
if ranges_input:
    for rango in ranges_input.split(","):
        if "-" in rango:
            start, end = rango.split("-")
            if start.strip().isdigit() and end.strip().isdigit():
                ranges_to_delete.append((int(start), int(end)))

delete_pdf_pages(
    source_file,
    resulting_file,
    loose_pages_to_delete,
    ranges_to_delete
)
