#!/usr/bin/env python3


import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("modulename", metavar="<modulename>", help="Name of module that generated")
parser.add_argument("-i", "--ignorefile", help="Generate ignorefile", action="store_true")
parser.add_argument("-d", "--delay-ignorefile", help="Delay generate ignorefile", action="store_true")
args = parser.parse_args()

subdirs = ["Model", "View", "Controller"]
dirs = [args.modulename] + [os.path.sep.join([args.modulename, x]) for x in subdirs]
for dirname in dirs:
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    else:
        print("directionary %s is exist" % dirname)

if args.ignorefile:
    if args.delay_ignorefile:
        input("Press any key to generate .gitignore files ...")

    ignores = [os.path.sep.join([x, ".gitignore"]) for x in dirs]

    for ignore_file_name in ignores:
        if os.path.isfile(ignore_file_name):
            print("file %s is exist" % ignore_file_name)
        else:
            with open(ignore_file_name, "w") as _:
                pass
