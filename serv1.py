import requests
import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response, current_app, \
    send_from_directory, session, escape
from werkzeug.utils import secure_filename
import re
import bs4

def PathFinder(url):
    page = requests.get(url)
    tree = str(bs4.BeautifulSoup(page.text, 'lxml'))
    # string = '"outpoint":"3ea97f5041538201ad7dc2580edfc8a20d6104a5645577868512be163ef4c6b9:0"'
    pattern = r'"outpoint":"[\w\d]+:\d*"'
    x = re.search(pattern, tree)
    find1 = str(x.group()).replace('"', '')
    pat2 = r"https://spee.ch/@\w+:\d"
    pat2 = r"(https://spee.ch/@\w+:[\d\w])[\w\d]+(/[\w\-]*)"
    x = re.search(pat2, url)
    find2 = str(x.group(1))
    find3 = str(x.group(2)) + '.mp4?'
    urlx = find2 + find3 + find1
    return urlx

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    target = os.path.join(APP_ROOT, 'images/')
    target2 = os.path.join(APP_ROOT, 'templates/')
    print(target)
    return render_template('ralph_lauren.html')

@app.route('/school6.html', methods=['GET', 'POST'])
def school6():
    return render_template('school6.html')


@app.route('/selectfile', methods=['GET', 'POST'])
def sel_file():
    if request.method == 'POST':
        stat = request.form['idx']
        print(stat)
        return redirect(url_for('load_file',stat = stat))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=text name=idx>
      <p><input type=submit value=Upload>
    </form>
    '''

@app.route('/load/<stat>', methods=['GET', 'POST'])
def load_file(stat):
    url = []
    stat = int(stat)
    print(stat)
    url.append("https://spee.ch/@KhanAcademy:5fc52291980268b82413ca4c0ace1b8d749f3ffb/algebra-linear-equations-1-linear")
    url.append("https://spee.ch/@KhanAcademy:5fc52291980268b82413ca4c0ace1b8d749f3ffb/algebra-linear-equations-2-linear")
    url.append("https://spee.ch/@KhanAcademy:5fc52291980268b82413ca4c0ace1b8d749f3ffb/algebra-linear-equations-3-linear")
    urlx = PathFinder(url[stat])
    print(urlx)
    return '<!doctype html><head><title>Upload new File</title><meta http-equiv="refresh" content="50"> </head><body><video width="320" controls><source src="' + urlx + '" type="video/mp4"></video></body>'


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
