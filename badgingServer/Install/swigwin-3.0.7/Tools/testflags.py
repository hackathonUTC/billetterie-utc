#!/usr/bin/env python

def get_cflags(language, std):
    if std == None or len(std) == 0:
        std = "gnu89"
    c_common = "-fdiagnostics-show-option -std=" + std + " -Wno-long-long -Wreturn-type -Wdeclaration-after-statement"
    cflags = {
        "csharp":"-Werror " + c_common,
             "d":"-Werror " + c_common,
            "go":"-Werror " + c_common,
         "guile":"-Werror " + c_common,
          "java":"-Werror " + c_common,
    "javascript":"-Werror " + c_common,
           "lua":"-Werror " + c_common,
        "octave":"-Werror " + c_common,
         "perl5":"-Werror " + c_common,
           "php":"-Werror " + c_common,
        "python":"-Werror " + c_common,
          "ruby":"-Werror " + c_common,
        "scilab":"-Werror " + c_common,
           "tcl":"-Werror " + c_common,
    }

    if language not in cflags:
        raise RuntimeError("{} is not a supported language".format(language))

    return cflags[language]

def get_cxxflags(language, std):
    if std == None or len(std) == 0:
        std = "c++98"
    cxx_common = "-fdiagnostics-show-option -std=" + std + " -Wno-long-long -Wreturn-type"
    cxxflags = {
        "csharp":"-Werror " + cxx_common,
             "d":"-Werror " + cxx_common,
            "go":"-Werror " + cxx_common,
         "guile":"-Werror " + cxx_common,
          "java":"-Werror " + cxx_common,
    "javascript":"-Werror " + cxx_common + " -Wno-error=unused-function", # Until overload_rename is fixed for node
           "lua":"-Werror " + cxx_common,
        "octave":"-Werror " + cxx_common,
         "perl5":"-Werror " + cxx_common,
           "php":"-Werror " + cxx_common,
        "python":"-Werror " + cxx_common,
          "ruby":"-Werror " + cxx_common,
        "scilab":             cxx_common,
           "tcl":"-Werror " + cxx_common,
    }

    if language not in cxxflags:
        raise RuntimeError("{} is not a supported language".format(language))

    return cxxflags[language]

import argparse
parser = argparse.ArgumentParser(description="Display CFLAGS or CXXFLAGS to use for testing the SWIG examples and test-suite.")
parser.add_argument('-l', '--language', required=True, help='set language to show flags for')
flags = parser.add_mutually_exclusive_group(required=True)
flags.add_argument('-c', '--cflags', action='store_true', default=False, help='show CFLAGS')
flags.add_argument('-x', '--cxxflags', action='store_true', default=False, help='show CXXFLAGS')
parser.add_argument('-s', '--std', required=False, help='language standard flags for the -std= option')
args = parser.parse_args()

if args.cflags:
    print("{}".format(get_cflags(args.language, args.std)))
elif args.cxxflags:
    print("{}".format(get_cxxflags(args.language, args.std)))
else:
    parser.print_help()
    exit(1)
