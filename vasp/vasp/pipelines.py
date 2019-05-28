# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VaspPipeline(object):

    # the domain url
    domain = 'https://cms.mpi.univie.ac.at'

    def process_item(self, item, spider):

        # Replace the spaces in tag name with underscore
        if ' ' in item['tag']:
            item['tag'] = '_'.join(item['tag'].split())

        # Convert the relative url to the absolute url
        item['link'] = self.domain + item['link']

        return item
