#!/usr/bin/env python3

# Imports
import argparse
import base64
import binascii
import html
from urllib.parse import quote


def url_encode(string):
    return quote(string)

def b64_encode(string):
    return base64.b64encode(string).decode()
    
def b64_url_encode(string): 
    return base64.urlsafe_b64encode(string).decode()
    
def hex_encode(string):
    return binascii.hexlify(string).decode()
    
def html_encode(string):
    return html.escape(string, quote=True)

def full_html_encode(string):
    return "".join([f"&#{byte};" for byte in string])

def parse_args():
    parser = argparse.ArgumentParser(
        description="Encode or Decode a string.")
    parser.add_argument('string', type=str,
        help='String to encode or decode.')
    parser.add_argument('-e', '--encode', type=str, 
        action='store_true', help='Encode a string',
        choices=['url', 'b64', 'b64url', 'hex', 'html', 'htmlfull'],
        default='url')
    return parser.parse_args()


def main():
    args = parse_args()
    string_to_encode = args.string

    if args.encoding == 'url':
        encoded_result = url_encode(string_to_encode)
    elif args.encoding == 'b64':
        encoded_result = b64_encode(string_to_encode)
    elif args.encoding == 'b64url':
        encoded_result = b64_url_encode(string_to_encode)
    elif args.encoding == 'hex':
        encoded_result = hex_encode(string_to_encode)
    elif args.encoding == 'html':
        encoded_result = html_encode(string_to_encode)
    elif args.encoding == 'htmlfull':
        encoded_result = full_html_encode(string_to_encode)
    else:
        encoded_result = string_to_encode

    print(encoded_result)
    
if __name__ == "__main__":
    main()