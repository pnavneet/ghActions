# Script to get system details
from Validation.systemUtils import SystemUtils

class TestSystem(object):

    def __init__(self):
        self.systemObj = SystemUtils()

    def run_system_test(self):
        self.systemObj.get_system_details()
        self.systemObj.display_system_info()

if __name__ == '__main__':
    obj = TestSystem()
    obj.run_system_test()
