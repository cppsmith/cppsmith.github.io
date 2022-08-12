copyright = u'2022, Eugene Kuznetsov'
extensions = [
    'sphinxext.opengraph',
    'sphinx_inline_tabs',
    'sphinx_copybutton'
]
templates_path = []
exclude_patterns = []

html_theme = 'furo'
html_theme_options = {
    'sidebar_hide_name': True,
    'source_repository': 'https://github.com/cppsmith/cppsmith.github.io',
    'source_branch': 'master',
    'source_directory': 'src'
}
html_title = 'cppsmith'
html_baseurl = 'https://cppsmith.dev'
html_logo = '_static/cppsmith.png'
html_static_path = ['_static']

ogp_site_url = html_baseurl
opg_image = html_logo
