#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sample.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import glut_ui
import glbase
import baseview
import triangle

if __name__=="__main__":
    glut_ui.run(glbase.BaseController(
        baseview.BaseView(), 
        triangle.Triangle()))