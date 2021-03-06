# -*- coding: utf-8 -*-
import csv 
import os 

class FeedCsvPipeline(object):
    def process_item(self, item, spider):
        filename = os.getcwd() + '\\data\\%s_%s.csv' % (spider.name, item['updatetime'])
        if not os.path.exists(filename):
            with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
                f = csv.writer(csvfile)
                f.writerow(sorted(item.keys()))
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            f = csv.writer(csvfile)
            f.writerow([item[key] for key in sorted(item.keys())])
        return item
