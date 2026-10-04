import argparse
from urllib.request import urlopen
import csv
import re

def main(url):
    print(f"Running main with URL = {url}...")

    lines = []

# part 1 downloading the file
    with urlopen(url) as fh:
        for line in fh:
            line = line.decode("utf-8")
            line = line.rstrip()
            lines.append(line)

#part 2
    rows = []
    reader = csv.reader(lines, delimiter=',')
    for row in reader:
        rows.append(row)

        total = len(rows)


#part  3
    imgs = 0
    for r in rows:
        path = r[0].lower()
        if re.search(r"\.(jpg|jpeg|gif|png)$", path):
            imgs = imgs + 1

    pct = round((imgs / total) * 100, 2)
    print("Image requests account for " + str(pct) + "% of all requests")

# part 4
    ff = 0
    chrome = 0
    ie = 0
    saf = 0

    for r in rows:
        browser = r[2]
        if re.search(r"Firefox", browser):
            ff = ff + 1
        elif re.search(r"Chrome", browser):
            chrome = chrome + 1
        elif re.search(r"MSIE", browser):
            ie = ie + 1
        elif re.search(r"Safari", browser):
            saf = saf + 1


    if ff >= chrome and ff >= saf and ff >= ie:
        top = "Firefox"
        most = ff
    elif chrome >= ie and chrome >= saf:
        top = "Chrome"
        most = chrome
    elif ie >= saf:
        top = "Internet Explorer"
        most = ie
    else:
        top = "Safari"
        most = saf

    print("The most popular browser is " + top + " with " + str(most) + " hits")



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
