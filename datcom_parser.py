#!/usr/bin/env python3

"""
Created on Mon Apr 29 00:16:41 2013
'Main Scripting Function'
author: Ruben Di Battista <ruben.dibattista@skywarder.eu>
version: 0.01a
License: Read LICENSE File
"""

from os import path


if __name__ == "__main__":
    import functions as f
    import argparse

    parser = argparse.ArgumentParser(description="Parse the DATCOM output file")

    parser.add_argument(
        "-f",
        "--filename",
        nargs="?",
        help='The name of the DATCOM output file. Default: "for006.dat"',
        default="for006.dat",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="+",
        help="Output type(s): 'csv' to output csv+json files, 'mat' to output Matlab data (.mat) file. "
             "Default: output both 'mat' and 'csv'",
        default=["csv", "mat"],
    )

    args = parser.parse_args()

    state_dict, final_data, coeffs = f.parse006(args.filename)

    name, ext = path.splitext(args.filename)

    if "mat" in args.output:
        f.saveMat(name, state_dict, final_data)

    if "csv" in args.output:
        f.saveCSV(name, state_dict, final_data, coeffs)
