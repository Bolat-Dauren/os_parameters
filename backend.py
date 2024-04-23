# backend.py

import platform
import psutil
import socket
import time

class ParameterRetrievalError(Exception):
    pass

class OSParametersBackend:
    def get_parameters(self, category):
        try:
            if category == "Operating System":
                return self.get_os_parameters()
            elif category == "CPU":
                return self.get_cpu_parameters()
            elif category == "Memory":
                return self.get_memory_parameters()
            elif category == "Disk":
                return self.get_disk_parameters()
            elif category == "Additional":
                return self.get_additional_parameters()
            else:
                return {}
        except Exception as e:
            # Raise an error if parameter retrieval fails
            raise ParameterRetrievalError(f"Failed to retrieve parameters: {e}")

    def get_os_parameters(self):
        # Retrieve operating system parameters
        os_info = {
            "OS Name": platform.system(),
            "OS Release": platform.release(),
            "OS Version": platform.version(),
            "Architecture": platform.machine(),
            "Hostname": socket.gethostname(),
        }
        return os_info

    def get_cpu_parameters(self):
        # Retrieve CPU parameters
        cpu_info = {
            "CPU Model": platform.processor(),
            "CPU Cores": psutil.cpu_count(logical=True),
            "CPU Usage": psutil.cpu_percent(interval=1),
        }
        return cpu_info

    def get_memory_parameters(self):
        # Retrieve memory parameters
        mem_info = {
            "Total Memory (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
            "Available Memory (GB)": round(psutil.virtual_memory().available / (1024**3), 2),
        }
        return mem_info

    def get_disk_parameters(self):
        # Retrieve disk parameters
        disk_info = {
            "Disk Usage (GB)": round(psutil.disk_usage('/').total / (1024**3), 2),
            "Disk Free (GB)": round(psutil.disk_usage('/').free / (1024**3), 2),
        }
        return disk_info

    def get_additional_parameters(self):
        # Retrieve additional parameters
        additional_info = {
            "IP Address": self.get_ip_address(),
            "System Uptime (seconds)": self.get_system_uptime(),
            "Running Processes": self.get_running_processes(),
            "System Architecture": platform.architecture()[0],
        }
        return additional_info

    def get_ip_address(self):
        # Retrieve the IP address of the system
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address

    def get_system_uptime(self):
        # Retrieve the system uptime
        uptime_seconds = time.time() - psutil.boot_time()
        return int(uptime_seconds)

    def get_running_processes(self):
        # Retrieve information about running processes
        running_processes = []
        for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_percent']):
            running_processes.append({
                "PID": proc.info['pid'],
                "Name": proc.info['name'],
                "Memory Usage (%)": proc.info['memory_percent'],
            })
        return running_processes
