# did-you-mean
Did you mean this?


## How to
- install dependencies using `pip install -r requirements.txt`
- install NLTK coupse using `nltk.download()`
    - go to python shell
    - `import nltk`
    - run `nltk.download()`
    - download `punkt` punkt Tokeniser model 
    or just run `python -m nltk.downloader punkt`
- `cd` into `did-you-mean`
- run Flask development server using `python main.py`

it will run a development server on `localhost:2000`, you can change that by changing `WEB_SERVER_PORT` in `config.py`