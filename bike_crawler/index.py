import subprocess

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    spider_name = "bike1_spider"
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "bikecrawler.json"])
    with open("bikecrawler.json") as items_file:
        return items_file.read()

if __name__ == '__main__':
    app.run(debug=True)