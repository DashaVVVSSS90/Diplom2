import config
import requests


def create_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json = order_body)

def get_order_info(track):
    return requests.get(config.URL_SERVICE + config.ORDER_INFO + str(track))