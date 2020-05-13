import logging
from _datetime import datetime
import os


class LoggingHelper:

    @staticmethod
    def setup_logger():
        date_time = datetime.now().strftime("%d-%m-%Y  %H-%M-%S")
        cur_path = os.getcwd()
        path_groups = cur_path.split("Music-Onboarder")
        dyn_path = cur_path
        rel_path = ""
        if path_groups[1] != '':
            counter = path_groups[1].count("\\")
            for i in range(0, counter):
                rel_path = rel_path + "../"
            dyn_path = rel_path
        fileh = dyn_path +"/tmp/" + "Run Executed at [" + date_time + "].txt"
        """
        fileh = logging.FileHandler('./tmp/'+filename, 'a')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        """

        logging.basicConfig(filename=fileh, filemode="w",
                            format='%(module)s -- %(levelname)s -- %(message)s',
                            level=logging.WARNING)
        rootlogger = logging.getLogger()
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter('%(module)s -- %(levelname)s -- %(message)s'))
        rootlogger.addHandler(console)
        return rootlogger

