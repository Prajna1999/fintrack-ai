from flask import Flask


app=Flask(__name__)


@app.route('/', methods=['GET'])
def fetch_data():
    return {"message":"successfully connected with openai service."}

@app.route('/qna',methods=['GET'])
def qna():
    
    return "OniChan"

@app.route('/helloThere',methods=['GET'])
def qna():
    
    return "Welcome General Kenobi"

if __name__=='__main__':
    app.run(port=5000)