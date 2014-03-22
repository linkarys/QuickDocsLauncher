import sublime, sublime_plugin, webbrowser
import subprocess
import urllib.request as urllib
import contextlib
import json
import os, re
from html.parser import HTMLParser

global settings

def init_settings(self):
    self.settings = sublime.load_settings("CFDocsLauncher.sublime-settings")

def get_syntax(view):
    scope = view.scope_name(view.sel()[0].end())
    res = re.search('\\bsource\\.([a-z+\-]+)', scope)
    return res.group(1) if res else None

def get_word(view):
    return view.substr(view.word( view.sel()[0] ))

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):
        init_settings(self)

        url = build_load_url(self)

        # if (len(word.strip())):
        #     url += word.strip()

        webbrowser.open(url)
        # # print (filename, {'content': text}) for filename, text in list('abbbbc')
        # # dict((filename, {'content': text}) for filename, text in list('abbbbc'))
        # language = 'C'
        # syntax = os.path.join('C++', "{0}.tmLanguage".format(language))
        # file_loc = os.path.join(sublime.packages_path(), syntax)
        # print (os.path.exists(file_loc))
        # sublime.status_message("Gist: GitHub token isn't provided in Gist.sublime-settings file. All other authorization methods is deprecated.")
def get_lan_settings(self):
    syntax = get_syntax(self.view)

    return self.settings.get(syntax)

def build_load_url(self):
    keyword = get_word(self.view)
    syntax = get_syntax(self.view)

    lan_settings = self.settings.get(syntax)

    if 'doc_url' in lan_settings:
        url = lan_settings['doc_url']

    edition = lan_settings['edition']

    if syntax == 'python':
        return url % edition

def build_search_url(self):

    keyword = get_word(self.view)
    syntax = get_syntax(self.view)

    lan_settings = self.settings.get(syntax)

    if 'search_url' in lan_settings:
        url = lan_settings['search_url']

    edition = lan_settings['edition']

    if syntax == 'python':
        return url % (edition, keyword.strip())

class SearchCfDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        init_settings(self)

        url = build_search_url(self)

        webbrowser.open(url)

class SearchInputCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        self.window.show_input_panel('Search Stack Overflow for', '',
            self.on_done, self.on_change, self.on_cancel)
        def on_done(self, input):
            SearchFor(input)

        def on_change(self, input):
            pass

        def on_cancel(self):
            pass

        # url = "http://www.baidu.com"
        # parser = MyHTMLParser()
        # try:
        #     with contextlib.closing(urllib.urlopen(url)) as response:
        #         if response.code == 204:  # No Content
        #             return None
        #         else:
        #             parser.feed(response.read().decode('utf8', 'ignore'))
        #             view.insert(edit, 0, parser.get_result())
        #             # return json.loads(response.read().decode('utf8', 'ignore'))
        # except urllib.HTTPError as err:
        #     with contextlib.closing(err):
        #         raise SimpleHTTPError(err.code, err.read())
        # for link in page.xpath("//a"):
        #     view.insert(edit, 0, x.text)

        # self.window.show_quick_panel(['abc', 'bac'], self.show)


