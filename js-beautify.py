import requests
import jsbeautifier
import argparse

parser = argparse.ArgumentParser(description='js-beautify')
parser.add_argument('-u', '--url', type=str, help='url to beautify')
parser.add_argument('-o', '--output', type=str, help='output file name')
args = parser.parse_args()


response = requests.get(args.url)
js_code = response.text

beautified_code = jsbeautifier.beautify(js_code)

if args.output:
    with open(args.output, 'w') as f:
        f.write(beautified_code)
else:
    print(beautified_code)
