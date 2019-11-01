#    X-tra-Telegram (userbot for telegram)
#    Copyright (C) 2019-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from xtrabot import client, Var, MOD_LIST, ModLogger
from telethon import events
import traceback
import re
xconfig = {}
func_name = {}

class FuncS:
    pass

class Module():
    def __init__(self, funct):
        try:
            self.name
        except NameError:
            self.name = "untitled"
        if type(funct) is not list:
            funct = [funct]
        for func in funct:
            if 1==1:
                funcmd = re.compile("^."+func.__name__)
                try:
                    func_name[self.name].append(func)
                except KeyError:
                    func_name.update({self.name: [func]})
                self.xconfig = xconfig
                self.logger = ModLogger.log(self.name)
                self.client = client
                self.config = Var
                MOD_LIST[list(MOD_LIST.keys())[-1]].append("^."+func.__name__)
                exec("""async def {}(event):
    try:
        await func(event)
    except Exception as error:
        await event.reply("__Error occured on the current__ `{}`, __do__ `.log` __to show the latest log.__")
        self.logger.exception(error)
        print(traceback.format_exc())""".format(func.__name__, "."+func.__name__))
                client.add_event_handler(locals()[func.__name__], events.NewMessage(pattern=funcmd, outgoing=True))

    def addxconfig(self, name, value, about=""):
        self.xconfig.update({name: [value, about]})

def command(**args):
    try:
        MOD_LIST[list(MOD_LIST.keys())[-1]].append(args["pattern"])
    except:
        pass
    def decorator(func):
        client.add_event_handler(func, events.NewMessage(**args))
    return decorator
