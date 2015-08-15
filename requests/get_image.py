#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StringIO import StringIO

import requests
from PIL import Image


def main():
    url = 'http://docs.python-requests.org/en/latest/_static/requests-sidebar.png'
    res = requests.get(url)
    img = Image.open(StringIO(res.content))
    img.save('requests-sidebar.png')


if __name__ == '__main__':
    main()