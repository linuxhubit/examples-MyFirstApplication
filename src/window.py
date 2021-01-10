# window.py
#
# Copyright 2021 Mirko Brombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
import urllib.request, json

@Gtk.Template(resource_path='/com/mirko/MyFirstApplication/window.ui')
class MyfirstapplicationWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MyfirstapplicationWindow'

    btn_refresh = Gtk.Template.Child()
    label_text = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_fact()

        self.btn_refresh.connect("pressed", self.on_btn_refresh_pressed)

    def update_fact(self):
        self.on_btn_refresh_pressed()

    def on_btn_refresh_pressed(self, widget=False):
        text = self.get_facts().get("text")
        self.label_text.set_text(text)

    @staticmethod
    def get_facts():
        api_url = "https://cat-fact.herokuapp.com/facts/random?amount=1"
        with urllib.request.urlopen(api_url) as data:
            result = json.loads(data.read().decode())

        if len(result) > 0: # check for results
            return result

        # if not return helpful text
        return {"text": "Non ho trovato alcun fatto."}
