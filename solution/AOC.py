import os
import time
import requests

class Advent:

    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../aoc2019token.txt")), "r") as f:
        session = f.read()

    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../input/input{:0>2}.txt".format(self.day)))
        self.output_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../output/output{:0>2}.txt".format(self.day)))
        self.download_input()
        self.load_input()

    def download_input(self):
        if os.path.isfile(self.input_filename):
            print("Input exists at {}".format(self.input_filename))
            return

        print("Downloading and saving input at {}".format(self.input_filename))

        input_url = "https://adventofcode.com/{}/day/{}/input".format(self.year, self.day)
        result = requests.get(input_url, cookies={'session': self.session})
        print(self.session)
        if result.status_code == 200:
            self.input_data = result.text
            with open(self.input_filename, 'w') as f:
                f.write(result.text)
            print("Input saved at {}".format(os.path.abspath(self.input_filename)))
        else:
            raise ConnectionError("Download Error. Code {}: {}".format(result.status_code, result.text))
    
    def load_input(self):
        if not os.path.isfile(self.input_filename):
            print("Input does not exist at {}".format(self.input_filename))
            return
        
        with open(self.input_filename, 'r') as f:
            self.input_data = f.read().splitlines()