# backend.py
import platform
import psutil
import socket

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
            else:
                return {}
        except Exception as e:
            # If an error occurs during parameter retrieval, raise an exception
            raise ParameterRetrievalError(f"Failed to retrieve parameters: {e}")

    def get_os_parameters(self):
        os_info = {
            "OS Name": platform.system(),
            "OS Release": platform.release(),
            "OS Version": platform.version(),
            "Architecture": platform.machine(),
            "Hostname": socket.gethostname(),
        }
        return os_info

    def get_cpu_parameters(self):
        cpu_info = {
            "CPU Model": platform.processor(),
            "CPU Cores": psutil.cpu_count(logical=True),
        }
        return cpu_info

    def get_memory_parameters(self):
        mem_info = {
            "Total Memory (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
            "Available Memory (GB)": round(psutil.virtual_memory().available / (1024**3), 2),
        }
        return mem_info

    def get_disk_parameters(self):
        disk_info = {
            "Disk Usage (GB)": round(psutil.disk_usage('/').total / (1024**3), 2),
            "Disk Free (GB)": round(psutil.disk_usage('/').free / (1024**3), 2),
        }
        return disk_info
