import sublime, sublime_plugin, webbrowser

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):
        word = ""
        for s in self.view.sel():
                word = self.view.word( s )
        
        s = sublime.load_settings("CFDocsLauncher.sublime-settings")
        search_url = s.get('search_url', 'https://wikidocs.adobe.com/wiki/display/coldfusionen/')

        webbrowser.open(search_url + self.view.substr(word))