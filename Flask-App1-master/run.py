from python import create_app

app = create_app()
app.static_folder = '../web/static'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)


