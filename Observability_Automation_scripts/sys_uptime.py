import psutil
import datetime


def system_uptime():
    boot_time = psutil.boot_time()
    time = datetime.datetime.now()- datetime.datetime.fromtimestamp(boot_time)
    print(f"system uptime is : {time}")


if __name__ == "__main__":
    system_uptime()
