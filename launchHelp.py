import sublime, sublime_plugin, webbrowser
import subprocess
import urllib.request as urllib
import contextlib
import json
import os, re
from html.parser import HTMLParser

class fn:
    settings = sublime.load_settings("CFDocsLauncher.sublime-settings")

    # match pattern like google lan:en key:python other:ot
    full_arg = re.compile('^[\w]+([^\S\n]+\w+[^\S\n]*:[^\S\n]*\w+)+[^\S\n]*$')
    # match pattern like google lan:en key:python other:ot
    short_arg = re.compile('^[\w]+([^\S\n]+\w+)+[^\S\n]*$')
    # match pattern like php
    single_word = re.compile('^[^\S\n][\w]+[^\S\n]*$')

    baseurl = 'https://www.google.com/search?q='


    @staticmethod
    def get_url(input):
        m = fn.full_arg.search(input)
        if m is None:
            m = fn.short_arg.match(input)
            if m is None:
                m = fn.single_word.match(input)

        if m is not None:
            return (m.groups())

    @staticmethod
    def get(attr):
        return fn.settings.get(attr, fn.baseurl)

def get_syntax(view):
    scope = view.scope_name(view.sel()[0].end())
    res = re.search('\\bsource\\.([a-z+\-]+)', scope)
    return res.group(1) if res else None

def get_word(view):
    return view.substr(view.word( view.sel()[0] ))

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):

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

    return fn.settings.get(syntax)

def build_load_url(self):
    keyword = get_word(self.view)
    syntax = get_syntax(self.view)

    lan_settings = fn.settings.get(syntax)

    if 'doc_url' in lan_settings:
        url = lan_settings['doc_url']

    edition = lan_settings['edition']

    if syntax == 'python':
        return url % edition

def build_search_url(self):

    keyword = get_word(self.view)
    syntax = get_syntax(self.view)

    lan_settings = fn.settings.get(syntax)

    if 'search_url' in lan_settings:
        url = lan_settings['search_url']

    edition = lan_settings['edition']

    if syntax == 'python':
        return url % (edition, keyword.strip())

class SearchCfDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        url = build_search_url(self)

        webbrowser.open(url)

class InputSearchCommand(sublime_plugin.TextCommand):

    def on_done(self, word):
        print (word)
    def run(self, edit):
        url = build_search_url(self)

        webbrowser.open(url)

class SearchInputCommand(sublime_plugin.WindowCommand):

    def on_done(self, input):
       url = fn.get_url(input)
       # print (url)
       webbrowser.open(url)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

    def run(self):

        # self.window.show_quick_panel(['xinju', 'yang', 'jiujiu'], self.on_done)
        self.window.show_input_panel('Search ju for', '', self.on_done, self.on_change, self.on_cancel)


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


