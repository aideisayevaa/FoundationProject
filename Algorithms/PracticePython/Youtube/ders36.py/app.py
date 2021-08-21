from flask import Flask #flask papkasindan Flask clasini cagiririq

app = Flask(__name__) #instance yaradiriq

@app.route('/')
def index():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug=True)  #bu kodu terminalda kodu run ede  