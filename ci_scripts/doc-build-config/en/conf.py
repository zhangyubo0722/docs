import sys
import os
import subprocess

# sys.path.insert(0, os.path.abspath('@PADDLE_BINARY_DIR@/python'))
import shlex
from recommonmark import parser, transform
import sys
import inspect
import ast
import time
import configparser
import re

try:
    import paddle
except:
    print("import paddle error")

breathe_projects = {"PaddlePaddle": "/docs/doxyoutput/xml"}
breathe_default_project = "PaddlePaddle"
MarkdownParser = parser.CommonMarkParser
AutoStructify = transform.AutoStructify

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- General configuration ------------------------------------------------

# General information about the project.
project = 'PaddlePaddle'
author = '%s developers' % project
copyright = '%d, %s' % (time.localtime(time.time()).tm_year, author)
github_doc_root = 'https://github.com/PaddlePaddle/docs/docs'

# add markdown parser
MarkdownParser.github_doc_root = github_doc_root

os.environ['PADDLE_BUILD_DOC'] = '1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinx_sitemap',
    'sphinx.ext.linkcode',
    'recommonmark',
    'sphinx_markdown_tables',
    'breathe',
    'exhale',
    'sphinx.ext.autosectionlabel',
    'sphinx_design',
]

exhale_args = {
    # These arguments are required
    "containmentFolder": "/FluidDoc/docs/inference_api",
    "rootFileName": "library_root.rst",
    "rootFileTitle": "Inference API",
    "doxygenStripFromPath": "..",
    # "listingExclude": [r"*CMakeLists*", 0],
    # Suggested optional arguments
    "createTreeView": True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin": "INPUT=/FluidDoc/docs/inference_api/\nMACRO_EXPANSION=NO\nSKIP_FUNCTION_MACROS=YES",
    "verboseBuild": True,
    "generateBreatheFileDirectives": True,
}

MARKDOWN_EXTENSIONS = [
    'markdown.extensions.fenced_code',
    'markdown.extensions.tables',
    'pymdownx.superfences',
    'pymdownx.escapeall',
]

html_baseurl = 'https://www.paddlepaddle.org.cn/documentation/docs/'

autodoc_member_order = 'bysource'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index_en'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"
version = ''
templates_path = ["/templates"]

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# html_permalinks_icon='P'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    '**/*_cn*',
    'book/*',
    'design/*',
    '*_cn.rst',
    '**/*.cn*',
    '*.cn*',
    '**/*hidden.*',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_context = {
    'display_github': True,
    'github_user': 'PaddlePaddle',
    'github_repo': 'docs',
    'github_version': 'develop',
    'conf_py_path': '/docs/',
}

if 'VERSIONSTR' in os.environ and os.environ['VERSIONSTR'] != 'develop':
    try:
        float(os.environ['VERSIONSTR'])
        html_context['github_version'] = 'release/' + os.environ['VERSIONSTR']
    except ValueError:
        print(
            "os.environ['VERSIONSTR']={} is not releases's name".format(
                os.environ['VERSIONSTR']
            )
        )
        html_context['github_version'] = os.environ['VERSIONSTR']

# if lang == 'en' and 'pagename' in html_context and html_context['pagename'].startswith('api/'):
#     html_context['display_github'] = False

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 10,
    'includehidden': True,
    'titles_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    'fncychap': '',
    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''\usepackage{ctex}
    ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '%s.tex' % project, project, author, 'manual'),
]
numfig = True
highlight_language = 'python'
html_experimental_html5_writer = True
# Use the .. admonition:: directive for Notes sections.
# False to use the .. rubric:: directive instead.
napoleon_use_admonition_for_notes = True


def change_variable_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)
    return "".join(lst).lower()


doc_version = os.environ.get('VERSIONSTR', 'develop')
if len(doc_version) == 0:
    doc_version = 'develop'

GITHUB_REPO_URL = 'https://github.com/PaddlePaddle/Paddle/blob/'
if doc_version != 'develop':
    GITHUB_REPO_URL += 'release/'


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['fullname']:
        return None
    class_names = info['fullname'].split('.')
    api_title = class_names[len(class_names) - 1]
    class_name = info['fullname'].replace('.' + api_title, '')
    if info['module']:
        class_name = info['module']
        if len(class_names) > 1:
            class_name = info['module'] + '.' + ''.join(class_names[:-1])
    try:
        # current_class = sys.modules[class_name]
        current_class = eval(class_name)
        api = getattr(current_class, api_title)
        line_no = None

        if type(api).__name__ == 'module':
            module = os.path.splitext(api.__file__)[0] + '.py'
        else:
            node_definition = (
                ast.ClassDef if inspect.isclass(api) else ast.FunctionDef
            )
            if type(api).__name__ == 'property':
                return None
            else:
                if api.__module__ not in [
                    'paddle.fluid.core',
                    'paddle.fluid.layers.layer_function_generator',
                ]:
                    module = (
                        os.path.splitext(sys.modules[api.__module__].__file__)[
                            0
                        ]
                        + '.py'
                    )
                    with open(module) as module_file:
                        module_ast = ast.parse(module_file.read())

                        for node in module_ast.body:
                            if (
                                isinstance(node, node_definition)
                                and node.name == api_title
                            ):
                                line_no = node.lineno
                                break

                        # If we could not find it, we look at assigned objects.
                        if not line_no:
                            for node in module_ast.body:
                                if isinstance(
                                    node, ast.Assign
                                ) and api_title in [
                                    target.id for target in node.targets
                                ]:
                                    line_no = node.lineno
                                    break
                else:
                    module = os.path.splitext(current_class.__file__)[0] + '.py'
        url = GITHUB_REPO_URL + os.path.join(
            doc_version, 'python', module[module.rfind('paddle') :]
        )
        if line_no:
            return url + '#L' + str(line_no)
        return url
    except Exception as e:
        print("conf.py(en) linkcode_resolve error", e)
        return None


def handle_api_aliases():
    """
    因为api定义和导入的各种关系，导致部分api定义的地方和导出的地方不一致被sphinx认为是alias，如paddle.device.cuda.Event等
    对这部分API做单独的重命名处理，而这部分api的列表，就放在 /FluidDoc/docs/api/api_aliases.ini中吧
    see https://console.cloud.baidu-int.com/devops/icafe/issue/DLTP-35024/show?source=drawer-header
    see https://stackoverflow.com/a/58982001/1738613
    """
    ini_file = '/FluidDoc/docs/api/api_aliases.ini'
    if not os.path.exists(ini_file):
        return
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(ini_file)

    if language in config:
        for target_name, origin_name in config[language].items():
            print(
                f'conf.py(en) handle_api_aliases: {target_name}={origin_name}'
            )
            tname = target_name.strip()
            tmn, tn = tname.rsplit('.', 1)
            oname = origin_name.strip()
            exec(f'{oname}.__module__ = "{tmn}"')
            exec(f'{oname}.__name__ = "{tn}"')


def remove_doctest_directives(app, what, name, obj, options, lines):
    """
    Remove `doctest` directives from docstring
    """
    pattern_doctest = re.compile(r"\s*>>>\s*#\s*doctest:\s*.*")

    # Modify the lines inplace
    lines[:] = [
        line
        for line in lines
        if not (pattern_doctest.match(line) or line.strip() == ">>>")
    ]


def setup(app):
    # Add hook for building doxygen xml when needed
    # no c++ API for now
    try:
        handle_api_aliases()
        # paddle.device.cuda.Event.__module__ = 'paddle.device.cuda'
        # paddle.device.cuda.Stream.__module__ = 'paddle.device.cuda'
    except Exception as e:
        print("conf.py handle_api_aliases error", e)
    app.add_config_value(
        'recommonmark_config',
        {
            # 'url_resolver': lambda url: github_doc_root + url,
            'enable_math': True,
            'enable_inline_math': True,
            'enable_eval_rst': True,
            # 'enable_auto_doc_ref': True,
            'auto_toc_tree_section': True,
            'known_url_schemes': ['http', 'https'],
        },
        True,
    )
    app.add_transform(AutoStructify)

    # remove doctest directives
    app.connect("autodoc-process-docstring", remove_doctest_directives)
