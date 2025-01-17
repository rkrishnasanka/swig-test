#!/usr/bin/env python

from distutils.core import setup, Extension

example_module = Extension('_example', sources = ['example_wrap.cxx',  'example.cpp'])

setup( name = 'example',
        version = '0.1',
        author = 'krishna',
        description = """Test Wrapper""",
        ext_modules = [example_module],
        py_modules = ["example"],
        )