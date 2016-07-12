#!/usr/bin/python
import argparse
import pylatex
import time


def generate(recipient, address=None):
    date = time.strftime('%Y,%m,%d')
    doc = pylatex.Document(documentclass="letter")

    with doc.create(pylatex.Opening("Dear " + recipient + " :")):
        pass
    # letter goes here

    with doc.create(pylatex.Closing("Best regards, ")):
        doc.append('Nathaniel Grevatt')

    path = (recipient + date + '.tex').replace(' ', '')
    doc.generate_tex(filepath=path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--recipient', default='Sir or Madam', help='Input letter recipient', required=False, type=str)
    # parser.add_argument('-a', '--recipient_address', help='Input recipient\'s address', required=False, type=str)
    args = parser.parse_args()

    generate(recipient=args.recipient, address=args.recipient)


if __name__ == '__main__':
    main()
