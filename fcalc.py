#!/bin/env python3

import sys
from source import commons
from source.fcalc import main as fcalc

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for index, item in enumerate(sys.argv):
            if index == 0:
                continue

            match item:
                case '--verbose' | '-v':
                    commons.is_verbose = True

                case '--language' | '-l':
                    if len(sys.argv) - 1 > index:
                        commons.app_language = sys.argv[index+1]
                        index += 1
                        break
                    
                    else:
                        print('ERROR: "{}": Not enout arguments. Continuing the execution.'.format(item))
                case _:
                    print('Unrecognized argument: "{}"'.format(item))
                    exit(1)
    
    fcalc.main()