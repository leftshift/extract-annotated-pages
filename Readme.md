Extracts the pages containing annotations from the given pdf file.

Requires `pdftk`. You may also need to install `bcprov` and `java-commons-lang` or similarly named packages if pdftk yells at you.

## Usage:
```
python extract.py in.pdf out.pdf
```
Generates a new pdf file `out.pdf` containing only the pages with annotations from `in.pdf`.
