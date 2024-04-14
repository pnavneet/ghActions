"""
This file is created only for GH actions learning purpose.
Creating dummy functions, for PR creation and triggering the workflow
"""
import platform
import psutil

class SystemUtils(object):

    def __init__(self):
        self.system_name = None
        self.system_platform = None
        self.system_vendor = None
        self.system_os = None
        self.system_cpu = None
        self.system_memory = None


    def _run_cmd(self, cmd):
        """ Function which will run the command and will return ouput and error status"""
        pass

    def _get_system_name(self):
        self.system_name = platform.node()
        return self.system_name
    
    def _get_system_platform(self):
        self.system_platform = platform.platform()
        return self.system_platform
    
    def _get_system_vendor(self):
        self.system_vendor = "TBD"

    def _get_system_cpu(self):
        self.system_cpu = "TBD"

    def _get_system_os(self):
        self.system_os = "TBD"

    def _get_system_memory(self):
        self.system_memory = "TBD"


    def display_system_info(self):
        """ Function to display system info"""
        print("*"*30)
        print("{:>20}".format("Displaying System Info"))
        print("*"*30)
        print("- {:<20}: {}".format("System Name", self.system_name))
        print("- {:<20}: {}".format("System Vendor", self.system_vendor))
        print("- {:<20}: {}".format("System Platform", self.system_platform))
        print("- {:<20}: {}".format("System OS", self.system_os))
        print("- {:<20}: {}".format("System CPU", self.system_cpu))
        print("- {:<20}: {}".format("System RAM", self.system_memory))

    
    def get_system_details(self):
        self._get_system_name()
        self._get_system_vendor()
        self._get_system_platform()
        self._get_system_os()
        self._get_system_cpu()
        self._get_system_memory()

