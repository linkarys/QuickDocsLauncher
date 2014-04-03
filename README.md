# Quick Docs Launcher
* Provides a command for launching a quick search and launch docs base on current environment
* Quick search anything via input panel

## Features
* Provides a command for launching a quick search and launch docs base on current environment
* Quick search anything via input panel

## Installing

You can install it via Package Control or install manually as follow:

- cd {user sublime folder}/Packages
- git clone https://github.com/linkarys/QuickDocsLauncher

## Usage

- Place the cursor around or select the tag/function to be searched/loaded
- Use `shift + alt + h` to load the doc page for specific tag/function directly
- Use `shift + alt+ s`  to perform an search operation against specific word
- Use `shift + alt + ;` to open the input panel and use the following syntax to perform search

------
## About Quick search
Use `shift + alt + ; ` (or `ctrl + shift + p` on windows, `cmd + shift + p` on mac and select "Search via input panel" to open input panel

### Syntax
```bash
search engine arg:value [arg:value ...] keyword
```

### Example
search array by google:

<img src="https://raw.githubusercontent.com/linkarys/img/master/QuickDocsLauncher/array.png" alt="array" width="525" height="34">

search array on mdn with language zh-CN and topic javascript:

<img src="https://raw.githubusercontent.com/linkarys/img/master/QuickDocsLauncher/mdn.png" alt="mdn" width="525" height="34">

search array on python official docs within edition 2.7:

<img src="https://raw.githubusercontent.com/linkarys/img/master/QuickDocsLauncher/py.png" alt="py" width="525" height="34">

search array on stackoverflow within topic python:

<img src="https://raw.githubusercontent.com/linkarys/img/master/QuickDocsLauncher/st.png" alt="st" width="525" height="34">

search sublime packages on https://sublime.wbond.net/:

<img src="https://raw.githubusercontent.com/linkarys/img/master/QuickDocsLauncher/wb.png" alt="wb" width="525" height="34">

------
All the available abbr for search engine are:
- g or nothing for google
- py for python
- php for php
- st for stackoverflow
- jq for jquery
- mdn for mdn
- subl for sublime text
- wb for wbond
- cf for coldfusion
- git for github
- gist for gist


Quick load and quick search action will detect your environment automatically and load or search the on the proper source.
You Should pre-define the source via Preferences->Package Settings->Quick Docs Launcher->
Settings - User

## Settings
Here is a demo
```
{
	// The following source will be used when plug-in could not find a specific source base on current environment
	"default": "https://www.google.com/search?q=",

	/**
	 * Use of quick launch and quick search
	 *
	 * doc_url is use for quick launch
	 * search_url is use for quick search
	 * ---------------------------------------------------------------------------
	 */

	"python": {
		"doc_url": "http://docs.python.org/3.4/library/",
		"search_url": "http://docs.python.org/3.4/search.html?check_keywords=yes&area=default&q=",
	},

	/**
	 * Use for quick panel search
	 *
	 * You should defined the source pattern following the following format:
	 *  "prefix": {
	 *  	"pattern": "http://xxxxx/${keyname:defaultValue}/xxxx?q="
	 *  }
	 *
	 *  The when you type in the input panel (ctrl + shift + ; by default) with
	 *  	prefix keyname:val querystring
	 *  It will launch a search at http://xxxxx/var/xxxx?q=querystring
	 *  ---------------------------------------------------------------------------
	 */
	"search_patterns": {
		"g": {
			"pattern": "https://www.google.com/search?hl=${l:en}&q="
		},
		"mdn": {
			"pattern": "https://developer.mozilla.org/${l:en-US}/search?topic=${t:}&q="
		},
		...
	}
}
```

# License

All of Sublime Text Quick Docs Launcher Plugin is licensed under the MIT license.

Copyright (c) 2012 linkarys <linkarys@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
