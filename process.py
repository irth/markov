#!/usr/bin/env python3
import pathlib
import sys

from bs4 import BeautifulSoup

export_dir = pathlib.Path(sys.argv[1])

message_files = export_dir.glob("messages*.html")

for message_file in message_files:
    print(message_file)
else:
    print(f"No message files in {export_dir.absolute()}")
