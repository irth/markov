#!/usr/bin/env python3
import pathlib
import re
import sys

from bs4 import BeautifulSoup

# TODO: use argparse
export_dir = pathlib.Path(sys.argv[1])
person = sys.argv[2].strip()
output = pathlib.Path(sys.argv[3])

output_file = output.open('w')


def extract_number(s: pathlib.Path):
    if s.name == "messages.html":
        return 0
    return int(re.sub('[^\\d]', '', str(s.name)))

message_files = list(sorted(export_dir.glob("messages*.html"), key=extract_number))


if len(message_files) == 0:
    print(f"No message files in {export_dir.absolute()}")


for message_file in message_files:
    print(message_file)
    with message_file.open('r') as f:
        body = BeautifulSoup(f.read())

    msgs = body.find_all(attrs={"class": "message"})
    for msg in msgs:
        content = msg.find(attrs={"class": "text"})
        from_name = msg.find(attrs={"class": "from_name"})
        if content is None or from_name is None:
            continue
        content = content.get_text().strip()
        from_name = from_name.get_text().strip()
        if from_name.lower() == person.lower():
            output_file.write(content + "\n")
    
