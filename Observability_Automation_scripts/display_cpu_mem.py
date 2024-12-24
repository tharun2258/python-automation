import psutil
import os
import time



def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def monitor_cpu_mem():

    try:
    
       while True:
          console_clear()
          cpu_usage = psutil.cpu_percent()
          mem_usage = psutil.virtual_memory()

          print(f"Cpu usage: {cpu_usage}")
          print(f"memory usage: {mem_usage.percent}")
          time.sleep(1)

    except KeyboardInterrupt:
      print("\nMonitoring stopped")
      
if __name__ == "__main__":
    monitor_cpu_mem()
