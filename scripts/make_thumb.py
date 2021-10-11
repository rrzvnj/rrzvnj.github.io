import sys
import subprocess
import glob
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='absolute path to source folder', required=False)
    parser.add_argument('-d', '--destination', help='absolute path to destination folder', required=False)
    args = parser.parse_args()
    return vars(args)

def run_command(command_str, split=True):
        try:
            print(command_str)
            # subprocess needs to receive args seperately
            if split:
                res = subprocess.call(command_str.split())
            else:
                res = subprocess.call(command_str, shell=True)
            if res == 1:
                print("Errors while executing: {0}".format(command_str))
                sys.exit()
        except OSError as e:
            print("Unable to run {0} command".format(command_str))
            sys.exit()

def main(args):
    all_images = glob.glob(args['source']+"/*")
    for src_image in all_images:
        file_name = src_image[:-4].split("/")[-1]
        file_format = src_image[-3:]
        dst_image = args['destination'] + "/{}.{}".format(file_name, file_format)
        dst_image = dst_image.replace("//", "/")
        cmd = "convert {} -resize 20% {}".format(src_image, dst_image)
        run_command(cmd)
        # print(dst_image)

if __name__ == '__main__':
    args = parse_args()
    main(args)
