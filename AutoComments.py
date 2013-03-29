'''
    - Created with Sublime Text 2.
    - User: song.chen
    - Date: 2013-03-29
    - Time: 11:32:50
    - Contact: song.chen@qunar.com
'''
import sublime, sublime_plugin
import time, re

file_type_reg = re.compile('(.*?)\.(css|js|py)$')
settings      = sublime.load_settings('AutoComments.sublime-settings')

class AutoCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_type = self.get_file_type()
        user_data = self.get_data()
        comments  = self.get_comments(user_data, file_type)
        self.view.insert(edit, 0, comments)

    def get_file_type(self):
        file_name       = self.view.file_name()
        file_type_match = file_type_reg.search(file_name)
        return file_type_match.group(2)

    def get_data(self):
        Date = time.strftime('%Y-%m-%d')
        Time = time.strftime('%H:%M:%S')

        return {
            "user"    : settings.get("user"),
            "contact" : settings.get("contact"),
            "date"    : Date,
            "time"    : Time
        }
    
    def get_comments(self, user_data, file_type):

        comments_map = {
            'js'  : ['/*', ' * ', ' */'],
            'css' : ['/*', ' * ', ' */'],
            'py'  : ['\'\'\'', '    - ', '\'\'\'']
        }

        comments_start = comments_map[file_type][0]
        line_start     = comments_map[file_type][1]
        comments_end   = comments_map[file_type][2]
        comments       = []

        comments.append(comments_start);
        comments.append(line_start + 'Created with Sublime Text 2.')
        comments.append(line_start + 'User: ' + user_data["user"])
        comments.append(line_start + 'Date: ' + user_data["date"])
        comments.append(line_start + 'Time: ' + user_data["time"])
        comments.append(line_start + 'Contact: ' + user_data["contact"])
        comments.append(comments_end + '\n')

        return '\n'.join(comments)