#! /usr/bin/env python
# -*- coding: utf-8 -*-
# hello_world.py

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello, World!"

cherrypy.quickstart(HelloWorld())