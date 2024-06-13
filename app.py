from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시로 메시지를 저장하기 위한 리스트
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    if username and message:
        messages.append({'username': username, 'message': message})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
