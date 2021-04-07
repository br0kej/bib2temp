# bib2temp

## What is this?

`bib2temp.py` is a simple utility script to convert a `.bibtex` files containg
a number of bibtex entries into individual markdown files. These markdown files
are generated from a hard coded template and can be used as a basis to create
paper synopses in a similar way to what is described in the book "Published: a 
guide to literature review, outlining, experimenting, visualization, writing, 
editing, and peer review for your first scientific journal article"

The script has been tested heavily on both prior and derivative work bibtex exports 
from [Connected Paper](https://www.connectedpapers.com/) - Your mileage may vary!

## Quickstart
```bash
python3 -m venv venv                # create virtualenv
source venv/bin/activate            # activate venv
pip install -r requirements.txt     # install requirements
python3 bib2temp.py <bibtex file>   # execute script and generate templates
```