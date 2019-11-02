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

# https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def main():
    os.system("python -m xtrabot")
    return "Your bot is alive!"

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
    call("python -m xtrabot".split(" "))
