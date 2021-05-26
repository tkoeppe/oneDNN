# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess

def whereis(binary):
    command = 'which' if os.name != 'nt' else 'where'
    try:
        sub = subprocess.run([command, binary], text=True, capture_output=True)
        return sub.stdout
    except BaseException as e:
        print(f"Warning: {binary} is not found")
        return ''

doxyrest_bin_path = whereis('doxyrest')
doxyrest_dir_path = os.path.dirname(doxyrest_bin_path)
doxyrest_share_path = doxyrest_dir_path + "/../share/doxyrest/sphinx"
sys.path.insert(1, os.path.abspath(doxyrest_share_path))


# -- Project information -----------------------------------------------------

project = 'oneDNN'
copyright = '© Copyright 2016 - 2021, Intel Corporation'
author = 'Intel'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Specify the path to Doxyrest extensions for Sphinx:

# Add Doxyrest extensions ``doxyrest`` and ``cpplexer``:

extensions = ['doxyrest', 'cpplexer']

# If you used INTRO_FILE in 'doxyrest-config.lua' to force-include it
# into 'index.rst', exclude it from the Sphinx input (otherwise, there
# will be build warnings):


imgmath_latex_preamble = '''\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{textgreek}
\\newcommand{\\src}{\\operatorname{src}}
\\newcommand{\\srclayer}{\\operatorname{src\\_layer}}
\\newcommand{\\srciter}{\\operatorname{src\\_iter}}
\\newcommand{\\srciterc}{\\operatorname{src\\_iter\\_c}}
\\newcommand{\\weights}{\\operatorname{weights}}
\\newcommand{\\weightslayer}{\\operatorname{weights\\_layer}}
\\newcommand{\\weightsiter}{\\operatorname{weights\\_iter}}
\\newcommand{\\weightspeephole}{\\operatorname{weights\\_peephole}}
\\newcommand{\\weightsprojection}{\\operatorname{weights\\_projection}}
\\newcommand{\\bias}{\\operatorname{bias}}
\\newcommand{\\dst}{\\operatorname{dst}}
\\newcommand{\\dstlayer}{\\operatorname{dst\\_layer}}
\\newcommand{\\dstiter}{\\operatorname{dst\\_iter}}
\\newcommand{\\dstiterc}{\\operatorname{dst\\_iter\\_c}}
\\newcommand{\\diffsrc}{\\operatorname{diff\\_src}}
\\newcommand{\\diffsrclayer}{\\operatorname{diff\\_src\\_layer}}
\\newcommand{\\diffsrciter}{\\operatorname{diff\\_src\\_iter}}
\\newcommand{\\diffsrciterc}{\\operatorname{diff\\_src\\_iter\\_c}}
\\newcommand{\\diffweights}{\\operatorname{diff\\_weights}}
\\newcommand{\\diffweightslayer}{\\operatorname{diff\\_weights\\_layer}}
\\newcommand{\\diffweightsiter}{\\operatorname{diff\\_weights\\_iter}}
\\newcommand{\\diffweightspeephole}{\\operatorname{diff\\_weights\\_peephole}}
\\newcommand{\\diffweightsprojection}{\\operatorname{diff\\_weights\\_projection}}
\\newcommand{\\diffbias}{\\operatorname{diff\\_bias}}
\\newcommand{\\diffdst}{\\operatorname{diff\\_dst}}
\\newcommand{\\diffdstlayer}{\\operatorname{diff\\_dst\\_layer}}
\\newcommand{\\diffdstiter}{\\operatorname{diff\\_dst\\_iter}}
\\newcommand{\\diffdstiterc}{\\operatorname{diff\\_dst\\_iter\\_c}}
\\newcommand{\\diffgamma}{\\operatorname{diff\\_\\gamma}}
\\newcommand{\\diffbeta}{\\operatorname{diff\\_\\beta}}
\\newcommand{\\workspace}{\\operatorname{workspace}}'''



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',]

exclude_patterns += ['page_index.rst']
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
#html_js_files = [('dnnl.js', {'defer': 'defer'})]


mathjax3_config = {
'tex': {
    'macros': {
        'src': '\\operatorname{src}',
        'srclayer': '\\operatorname{src\\_layer}',
        'srciter': '\\operatorname{src\\_iter}',
        'srciterc': '\\operatorname{src\\_iter\\_c}',
        'weights': '\\operatorname{weights}',
        'weightslayer': '\\operatorname{weights\\_layer}',
        'weightsiter': '\\operatorname{weights\\_iter}',
        'weightspeephole': '\\operatorname{weights\\_peephole}',
        'weightsprojection': '\\operatorname{weights\\_projection}',
        'bias': '\\operatorname{bias}',
        'dst': '\\operatorname{dst}',
        'dstlayer': '\\operatorname{dst\\_layer}',
        'dstiter': '\\operatorname{dst\\_iter}',
        'dstiterc': '\\operatorname{dst\\_iter\\_c}',
        'diffsrc': '\\operatorname{diff\\_src}',
        'diffsrclayer': '\\operatorname{diff\\_src\\_layer}',
        'diffsrciter': '\\operatorname{diff\\_src\\_iter}',
        'diffsrciterc': '\\operatorname{diff\\_src\\_iter\\_c}',
        'diffweights': '\\operatorname{diff\\_weights}',
        'diffweightslayer': '\\operatorname{diff\\_weights\\_layer}',
        'diffweightsiter': '\\operatorname{diff\\_weights\\_iter}',
        'diffweightspeephole': '\\operatorname{diff\\_weights\\_peephole}',
        'diffweightsprojection': '\\operatorname{diff\\_weights\\_projection}',
        'diffbias': '\\operatorname{diff\\_bias}',
        'diffdst': '\\operatorname{diff\\_dst}',
        'diffdstlayer': '\\operatorname{diff\\_dst\\_layer}',
        'diffdstiter': '\\operatorname{diff\\_dst\\_iter}',
        'diffdstiterc': '\\operatorname{diff\\_dst\\_iter\\_c}',
        'diffgamma': '\\operatorname{diff\\_\\gamma}',
        'diffbeta': '\\operatorname{diff\\_\\beta}',
        'workspace': '\\operatorname{workspace}'
        }
    }
}

def setup(app):
    app.connect('env-before-read-docs', fixFileNameRefs)
    app.connect('env-before-read-docs', addTocTrees)

def fixFileNameRefs(app, env, docnames):

    replacements = {"page_dev_guide": "dev_guide", "group_Dnnl":"group_dnnl"}
    targetDir = "rst"

    fileExtension = ".rst"


    for dirpath, dirnames, filenames in os.walk(targetDir):
        for filename in [f for f in filenames if f.endswith(fileExtension)]:
            filePath = os.path.join(dirpath,filename)
            print("replacing strings in " + filePath)
            outdata = None
            with open(filePath) as f:
                read_data = f.read()
                outdata = read_data
                for replacement in replacements:
                    outdata = outdata.replace(replacement,replacements[replacement])
            with open(filePath,"w") as f:
                f.write(outdata)



def addTocTrees(app, env, docnames):

    trees2Add = {'rst/dev_guide_inference_and_training_aspects.rst':['dev_guide_inference.rst','dev_guide_inference_int8.rst','dev_guide_training_bf16.rst'],
                 'rst/dev_guide_attributes.rst':['dev_guide_attributes_scratchpad.rst','dev_guide_attributes_quantization.rst','dev_guide_attributes_post_ops.rst']}


    for rstFile in trees2Add:
        with open(rstFile, 'r') as f:
            fContents = f.read()
            if '.. toctree::' in fContents:
                continue
        with open(rstFile, 'a+') as f:
            tocTree = '\n.. toctree::\n   :hidden:\n\n'
            for file in trees2Add[rstFile]:
                tocTree += "   " + file + "\n"
            tocTree += "\n\n"
            f.write(tocTree)
