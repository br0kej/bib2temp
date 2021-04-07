import argparse
from tqdm import tqdm
from pybtex.database import parse_file
from mdutils.mdutils import MdUtils


def generate_singular_templates(bib_data):
    """
    Parses a .bibtex file and creates a singular
    markdown write-up template for each entry.

    Args:
        bib_data: A pybtex parsed file

    Returns:
        Outputs singular markdown write-up templates

    """

    for entry in tqdm(bib_data.entries.values()):
        title = entry.fields['title']
        year = entry.fields['year']
        url = entry.fields['url']

        authors = str(entry.persons['author'][0])

        if 'journal' in entry.fields:
            journal = entry.fields['journal']

        file_name = authors.lower() + '-' + str(year)
        if 'journal' in locals():
            title = authors + ', ' + title + ', ' + year + ', ' + journal
        else:
            title = authors + ', ' + title + ', ' + year

        mdfile = MdUtils(file_name=file_name, title=title)

        # Add the correct header information
        mdfile.new_header(level=1, title='TLDR')
        mdfile.new_header(level=1, title='Links')
        mdfile.new_line('Paper - ' + mdfile.new_inline_link(text='Link to Paper', link=url))
        mdfile.new_header(level=1, title='Summary')
        mdfile.new_header(level=1, title='Comments')
        mdfile.new_header(level=1, title='Reference')

        mdfile.insert_code(entry.to_string(bib_format='bibtex'))

        mdfile.create_md_file()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts a .bibtex file into markdown templates')
    parser.add_argument('file', help='.bib file to be processed')

    args = parser.parse_args()

    parsed_bitex = parse_file(args.file, bib_format="bibtex")
    if parsed_bitex:
        generate_singular_templates(parsed_bitex)
