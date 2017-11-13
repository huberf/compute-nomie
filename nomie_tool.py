# Main Nomie processing file
import nomiepy
import json
import os

class NomieComp:
    NomieInterface = None
    def __init__(self):
        config = json.loads(open('config.json').read())
        self.NomieInterface = nomiepy.Nomie(config['url'], config['username'])

    # Helper methods
    def __verify_tracker_cache(self):
        # method is redundant and not of use right now
        if os.path.isfile('trackernames.json'):
            return True
        else:
            self.NomieInterface.saveTrackers()
            return True

    # Primary functions
    def count(self, label, start, end=None, cached=None):
        events = None
        if not cached:
            events = self.NomieInterface.eventList()['rows']
        else:
            events = json.loads(open('event_cache.json').read())

        instances = []
        for i in events:
            if i['name'] == label:
                instances += [i]

        count = 0
        for i in instances:
            if int(i['time']) > int(start):
                if end == None or int(i['time']) < int(end):
                    count += 1

        return { 'count': count }
