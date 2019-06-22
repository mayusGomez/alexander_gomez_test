import logging

from  trlu_cache_server.web_socket import server_master


class CacheApp:
    def __init__(self, settings=None):
        self.settings = settings

    def run(self):
        logging.basicConfig(
            level=self.settings['LOGGING'],
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        if self.settings['SERVER']['type'] == 'master':
            server_master.execute(self.settings)
        else:
            logging.info(f"Only work for master")
