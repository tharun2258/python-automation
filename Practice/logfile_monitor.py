import re
import time

def monitor_log_file(log_file , output_file, pattern):
    with open(log_file,'r') as log , open(output_file, 'a') as output:
        log.seek(0,2)
        while True:
           line = log.readline()
           if not line:
               time.sleep(0.5)
               continue
           
           if re.search(pattern , line):
               if not line.endswith('\n'):
                   line += '\n'
               output.write(line)
               output.flush()
               print(f"Error found: {line.strip()}")


if __name__ == "__main__":
    monitor_log_file("C:/Users/Yamini K/SRE_LEARNINGS/Python/Practice/application.log", "error.log",r'ERROR|Exception')