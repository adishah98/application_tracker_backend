from project import app
from project import db



if __name__=='__main__':
    app.run(debug=False,threaded=True, port=8000)