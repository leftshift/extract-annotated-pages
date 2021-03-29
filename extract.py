import sys
import subprocess

res = subprocess.run(['pdftk', sys.argv[1], 'dump_data_annots'], capture_output=True, text=True)
if res.returncode != 0:
    print('Error from pdftk:\n{}'.format(res.stderr))

wantedPages = []

wanted = False
for line in res.stdout.split('\n'):
    if line.startswith('---'):
        wanted = False
    elif line.startswith("AnnotSubtype"):
        _, subtype = line.split(":")
        # ignore links
        if subtype.strip() != "Link":
            wanted = True
    elif line.startswith("AnnotPageNumber") and wanted:
        _, number = line.split(":")
        wantedPages.append(number.strip())

command = ['pdftk', sys.argv[1], 'cat', *wantedPages, 'output', sys.argv[2]]
print(command)
res = subprocess.run(command)
