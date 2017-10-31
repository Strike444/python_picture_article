import argparse
import os

parser = argparse.ArgumentParser(prog='Convert pictures and docs to article', description='This is help')

def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

parser.add_argument('-p', '--path', help='path to dir with input files', type=readable_dir, default='/tmp/non_existent_dir')
args = parser.parse_args()
paramerts = vars(args)
path = paramerts['path']
print(path)