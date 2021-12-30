from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {
        'Greeting': 'This is root "/" handler'
    }
