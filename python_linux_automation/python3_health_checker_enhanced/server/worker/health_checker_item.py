#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: health_checker_item.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 15:24:41
############################

import itertools

class HealthCheckItem(object):
    all_check_items = {
        'CheckParamter' : ['CheckBinaryLog', 'CheckConnections'],
    }

    all_health_points = list(itertools.chain(*all_check_items.viewvalues()))

    @staticmethod
    def get_health_check_catalog():
        return HealthCheckItem.all_check_items.keys()

    @staticmethod
    def get_health_check_point():
        return HealthCheckItem.all_health_points

    @staticmethod
    def get_health_check_point_in_catalog(catalog):
        return HealthCheckItem.all_check_items[catalog]

def main():
    print(HealthCheckItem,get_health_chech_catalog())
    print(len(HealthCheckItem.get_health_check_point()))

    for catalog in HealthCheckItem.get_health_check_catalog():
        for point in
        HealthCheckItem.get_health_check_point_in_catalog(catalog):
            print("{0}:{1}".format(catalog, point))

if __name__ == '__main__':
    main()

