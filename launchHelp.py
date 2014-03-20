import sublime, sublime_plugin, webbrowser
import subprocess
import urllib

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):
        word = ""
        for s in self.view.sel():
            word = self.view.word( s )

        s = sublime.load_settings("CFDocsLauncher.sublime-settings")
        doc_chanel = s.get('doc_chanel', 'https://wikidocs.adobe.com/wiki/display/coldfusionen/')

        webbrowser.open(doc_chanel + self.view.substr(word))


class SearchCfDocsCommand(sublime_plugin.TextCommand, sublime_plugin.WindowCommand):
    def show(self, index):
        print (index)

    def run(self, edit):
        # word = ""
        # for s in self.view.sel():
        #     word = self.view.word( s )

        settings = sublime.load_settings("CFDocsLauncher.sublime-settings")
        # search_chanel = s.get('search_chanel', 'https://wikidocs.adobe.com/wiki/dosearchsite.action?where=coldfusionen&search-filter-button=Filter&queryString=')
        # sublime.error_message(search_chanel)
        view = sublime.active_window().new_file()
        # edit = view.begin_edit()
        view.insert(edit, 0,'asdfasfasdfasd')

        url = "http://www.infolanka.com/miyuru_gee/art/art.html"
        page = html.fromstring(urllib.urlopen(url).read())

        for link in page.xpath("//a"):
            view.insert(edit, 0, x.text)

        # self.window.run_command('exec', {'cmd': "launch_cf_help"})
        # self.window.show_quick_panel(['abc', 'bac'], self.show)
        # webbrowser.open(search_chanel + self.view.substr(word))

    def api_request_curl(url, data=None, method=None):
        command = ["curl", '-K', '-', url]
        settings = sublime.load_settings("CFDocsLauncher.sublime-settings")
        config = ['--header "Authorization: token "',
                  '--header "Accept: application/json"',
                  '--header "Content-Type: application/json"',
                  "--silent"]

        if method:
            config.append('--request "%s"' % method)

        if settings.get('https_proxy'):
            config.append(settings.get('https_proxy'))

        with named_tempfile() as header_output_file:
            config.append('--dump-header "%s"' % header_output_file.name)
            header_output_file.close()
            with named_tempfile() as data_file:
                if data is not None:
                    data_file.write(bytes(data.encode('utf8')))
                    data_file.close()
                    config.append('--data-binary "@%s"' % data_file.name)

                process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                response, _ = process.communicate(bytes('\n'.join(config).encode('utf8')))
                returncode = process.returncode

                if returncode != 0:
                    raise subprocess.CalledProcessError(returncode, 'curl')

                with open(header_output_file.name, "r") as headers:
                    _, responsecode, message = headers.readline().split(None, 2)
                    responsecode = int(responsecode)

                    if responsecode == 204:  # No Content
                        return None
                    elif 200 <= responsecode < 300 or responsecode == 100:  # Continue
                        return json.loads(response.decode('utf8', 'ignore'))
                    else:
                        raise SimpleHTTPError(responsecode, response)
