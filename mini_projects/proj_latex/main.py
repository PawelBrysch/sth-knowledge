import os
import os.path as op
import shutil
from pathlib import Path
from pdf2image import convert_from_path
import PIL
import subprocess
import sys
import argparse


def convert_from_pdf_to_png(path_to_pdf, path_to_png):
    pages = convert_from_path(path_to_pdf, 500)
    pages[0].save(path_to_png, 'PNG')


def trim_png(path_to_input, path_to_output):
    im = PIL.Image.open(path_to_input)
    bg = PIL.Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = PIL.ImageChops.difference(im, bg)
    diff = PIL.ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        im.crop(bbox).save(path_to_output)

def convert_tex_to_trimmedpng(path_to_input):
    # paths refs
    # path_to_input = rf"C:\Users\devoted_w\Documents\snippets_tops\sth-knowledge\mini_projects\proj_latex\input\test2.tex"
    input_filename = op.basename(path_to_input)
    cwd = op.abspath(op.join(path_to_input, op.pardir, op.pardir))
    path_to_tempdir = op.join(cwd, "temp")
    path_to_input_copy = op.join(path_to_tempdir, input_filename)
    path_to_intermediate = Path(path_to_input_copy).with_name("intermediate").with_suffix(".png")
    path_to_output = Path(cwd).joinpath("output").joinpath(input_filename).with_suffix(".png")

    # proper work
    os.mkdir(path_to_tempdir)
    shutil.copyfile(path_to_input, path_to_input_copy)
    os.system(f'cd temp && pdflatex -shell-escape {input_filename}')
    convert_from_pdf_to_png(Path(path_to_input_copy).with_suffix(".pdf"), path_to_intermediate)
    trim_png(path_to_intermediate, path_to_output)
    shutil.rmtree(path_to_tempdir)
    subprocess.Popen(rf'explorer /select,"{path_to_output}"')


def parse_arguments(input_):
    input_ = input_[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_input', type=str)
    return parser.parse_args(input_)


def main(input):
    parsed_args = parse_arguments(input)
    convert_tex_to_trimmedpng(**vars(parsed_args))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))