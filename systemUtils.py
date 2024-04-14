"""
This file is created only for GH actions learning purpose.
Creating dummy functions, for PR creation and triggering the workflow
"""
import platform
import psutil

class SystemUtils(object):

    def __init__(self):
        self.host_name = None
        self.host_platform = None
        self.host_vendor = None
        self.host_os = None
        self.host_cpu = None
        self.host_memory = None


    def _run_cmd(self, cmd):
        """ Function which will run the command and will return ouput and error status"""
        pass

    def _get_system_name(self):
        self.host_name = platform.node()
        return self.host_name
    
    def _get_system_platform(self):
        self.host_platform = platform.platform()
        return self.host_platform
    
    def _get_system_vendor(self):
        pass


    def _display_system_info(self):
        """ Function to display system info"""
        print("")

    
