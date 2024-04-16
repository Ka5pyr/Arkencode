#!/usr/bin/env python3

# Imports
import argparse
import base64
import binascii
import html
import sys
from urllib.parse import quote, unquote


def url_encode(string):
    return quote(string)
    
def url_decode(string):
    return unquote(string)

def b64_encode(string):
    return base64.b64encode(string).decode()

def b64_decode(string):
    return base64.b64decode(string).decode()

def b64_url_encode(string): 
    return base64.urlsafe_b64encode(string).decode()

def b64_url_decode(string): 
    return base64.urlsafe_b64decode(string).decode()

def hex_encode(string):
    return binascii.hexlify(string).decode()
    
def hex_decode(string):
    return binascii.unhexlify(string).decode()

def html_encode(string):
    return html.escape(string, quote=True)
    
def html_decode(string):
    return html.unescape(string, quote=True)

def full_html_encode(string):
    return "".join([f"&#{byte};" for byte in string])

def parse_args():
    parser = argparse.ArgumentParser(
        description="Encode or Decode a string.")
    parser.add_argument('-e', '--encode', type=str,
            help='Encode a string',
            choices=['url', 'b64', 'b64url', 'hex', 'html', 'htmlfull'],
            default='url')
    return parser.parse_args()


def main():
    args = parse_args()
    input_string = sys.stdin.read()
    result = None

    if args.encode:
        encoded_string = input_string.encode()
        if args.encode == 'url':
            result = url_encode(encoded_string)
        elif args.encode == 'b64':
            result = b64_encode(encoded_string)
        elif args.encode == 'b64url':
            result = b64_url_encode(encoded_string)
        elif args.encode == 'hex':
            result = hex_encode(encoded_string)
        elif args.encode == 'html':
            result = html_encode(input_string)
        elif args.encode == 'htmlfull':
            result = full_html_encode(encoded_string)
            
    elif args.decode:
        if args.decode == 'url':
            result = url_decode(input_string)
        elif args.decode == 'b64':
            result = b64_decode(input_string)
        elif args.decode == 'b64url':
            result = b64_url_decode(input_string)
        elif args.decode == 'hex':
            result = hex_decode(input_string)
        elif args.decode == 'html':
            result = html_decode(input_string)

    print(result)

if __name__ == "__main__":
    main()