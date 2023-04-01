from website import create_app
from flask import send_from_directory

app = create_app()


@app.route('/static/<name>')
def display_file(name):
    print('Image request here')
    return send_from_directory('static', name)

if __name__ == '__main__':
    app.run(debug=True)