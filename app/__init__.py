import os
import sys

from flask import Flask

template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************' + template_folder)

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)
