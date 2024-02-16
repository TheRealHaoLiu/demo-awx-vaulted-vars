# read all std in

import sys
import json
import yaml


def main():
    # read the data from stdin
    data = sys.stdin.read()

    # split the string by end of line
    lines = data.split('\n')

    # split string into "key" and "value"
    var_name, vault_tag = lines[0].split(': ', 1)

    if vault_tag != "!vault |":
        raise ValueError("Not a ansible vaulted string")

    lines = [line.strip() for line in lines]

    dict_data = {
        var_name: {
            "__ansible_vault": "\n".join(lines[1:])
        }
    }

    # if --json is passed, output as json
    if len(sys.argv) > 1 and sys.argv[1] == '--json':
        print(json.dumps(dict_data))
    else:
        print(yaml.safe_dump(dict_data, default_style="|"))

if __name__ == '__main__':
    main()
