import subprocess
import json
from scrapy.crawler import CrawlerRunner
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    spider_names = ["bike1_spider", "bike2_spider"]
    data = {'bike_name': [], 'price': [], 'site_url': []}
    for spider_name in spider_names:
        subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "bikecrawler.json"])
        items_file = open("bikecrawler.json", "r").read()
        # print(items_file)
        for line in items_file:
            for key in data.keys():
                data[key] = list(data[key])
                data[key].append(line[key])
        # items_file.close()
    
    with open('bikecrawler.json', 'w') as f:
        json.dump(data, f)
        # for d in data:
        #     d_str = ''.join(str(d))
        #     print(d_str)
        #     # json_acceptable_str = d_str.replace("'", "\"")
        #     f.write(json.dumps(json.loads(d_str)))
        return f

if __name__ == '__main__':
    app.run(debug=True)