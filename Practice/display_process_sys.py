import psutil


def display_process():
    process = psutil.process_iter(['pid','name','status', 'ppid'])


    for proc in process:
        try:
           
            print(f"PID's : {proc.info['pid']} , name : {proc.info['name']} , status: {proc.info['status']} , ppid: {proc.info['ppid']}")
    
        except (psutil.NoSuchProcess):
            print("no process found")


if __name__ == "__main__":
    display_process()
