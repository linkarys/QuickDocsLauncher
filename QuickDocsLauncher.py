import sublime, sublime_plugin, webbrowser, re

def get_url(input):

    settings = sublime.load_settings("QuickDocsLauncher.sublime-settings")
    s_patterns = settings.get('search_patterns')
    arg_pair = re.compile(r'^(\w+):([\w\d.-]*)$')

    words = input.split()
    pattern = words.pop(0)

    def repl_fun(key, val):
        def repl(matchobj):
            if matchobj.group(1) == key:
                return str(val)
            return matchobj.group(0)
        return repl

    def fillin_default(matchobj):
        return matchobj.group(2)

    # build search url with given params, if fail search by devdocs by default
    try:
        s_pattern = s_patterns[pattern]['pattern']
        reg_repl = re.compile(r'\$\{\s*([\w\d+]+)\s*:([^\}]*)\}')
        keyword = []
        for word in words:
            match = arg_pair.match(word)
            if match:
                key = match.group(1)
                val = match.group(2)

                repl = repl_fun(key, val)
                s_pattern = reg_repl.sub(repl, s_pattern)
            else:
                keyword.append(word)

        s_pattern = reg_repl.sub(fillin_default, s_pattern)
        return s_pattern + ' '.join(keyword)

    except:
        return settings.get('default_site', 'http://devdocs.io/#q=') + input.replace(' ', '%20')

# get syntax of current dev
def get_syntax(view):
    scope = view.scope_name( view.sel()[0].end() )
    res = re.search( '\\bsource\\.([a-z+\-]+)', scope )
    return syntax_mapping( res.group(1) ) if res else None

# map to syntax shorthand to full name
def syntax_mapping(ext):
    mappings = {
        'js': 'javascript'
    }

    return mappings[ext] if ext in mappings else ext

# get word around current cursor
def get_word(view):
    return view.substr( view.word( view.sel()[0] ) )

# build the search/load url
def build_url(self, type):
    keyword = get_word(self.view)
    syntax = get_syntax(self.view)

    settings = sublime.load_settings("QuickDocsLauncher.sublime-settings")

    if syntax:
        default_site = settings.get('default_site')
        lan_settings = settings.get(syntax)

        if type == 'load':
            if lan_settings and 'doc_url' in lan_settings:
                return lan_settings['doc_url'] + keyword
            else:
                return default_site + keyword

        elif type == 'search':
            if lan_settings and 'search_url' in lan_settings:
                return lan_settings['search_url'] + keyword
            else:
                return settings.get('default_search_engine') + keyword

    else:
        return settings.get('default_search_engine') + keyword

# search via quick launch command
class LaunchHelpCommand(sublime_plugin.TextCommand):

    def run(self, edit, forward = True):
        url = build_url(self, 'load')
        webbrowser.open(url)

# search via quick search command
class SearchDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        url = build_url(self, 'search')
        webbrowser.open(url)

# search via input panel
class SearchInputCommand(sublime_plugin.WindowCommand):

    def on_done(self, input):
        webbrowser.open(get_url(input))

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

    def run(self):
        self.window.show_input_panel('Search for', '', self.on_done, self.on_change, self.on_cancel)

