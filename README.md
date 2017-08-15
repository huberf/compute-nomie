# compute-nomie
A utility for processing and making Nomie data accessible.

System works by retrieving data from Nomie via CouchDB and then performing
computations and delivering info based upon query parameters.

Not all dependencies of this project currently support Python 3.x.

## Installation
* Clone the repo via `git clone https://github.com/huberf/compute-nomie' and
  then `cd` into the directory by typing `cd compute-nomie`
* Install dependencies via `pip install -r dependencies.txt`
* Open `config.json` and modify the server location of the CouchDB as well as
  your username there.
* To start the server, run `python web.py`

## Routes
* `GET /count` - Parameters: `label` - Name of tracker; `start` - Start of
  period as a UNIX timestamp; (optional) `end` - Timestamp for end of period.

## Contribution
This is just the early stages of this project and any help or feedback would be
appreciated. Feel free to open an issue or a pull request if you have a
critique, question, wish or addition.
