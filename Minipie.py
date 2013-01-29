from os import path

from rjsmin import jsmin
from cssmin import cssmin

import sublime
import sublime_plugin

class Minipie(sublime_plugin.TextCommand):

	def __init__(self, view):
		self.view = view
		self.window = sublime.active_window()

	def run(self, edit):

		current_file = self.view.file_name()

		if current_file is None:
			return None
		else:
			file_parts = path.splitext(current_file)

		if file_parts[1] == '.js':
			fileType='js'
		elif file_parts[1] == '.css':
			fileType='css'
		else:
			fileType=None

		if fileType is None:
			sublime.error_message('Please focus on the .js or .css file you wish to minify.')
			return None

		#do stuff
		region = sublime.Region(0, self.view.size())
		text = self.view.substr(region)
		if fileType=='js':
			result = jsmin(text)
		elif fileType=='css':
			result = cssmin.cssmin(text)

		#write stuff
		min_file_suffix = '.min'
		file_name = file_parts[0] + min_file_suffix + file_parts[1]

		file_path = path.join(
			path.dirname(current_file),
			file_name
		)

		with open(file_path, 'w+', 0) as min_file:
			min_file.write(result)

		sublime.status_message("Minipie saved %s" % (file_path))