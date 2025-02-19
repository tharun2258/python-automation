def log_file_check(logfile):
    keywords= ["ERROR", "WARNING"]

    with open(logfile, 'r') as file:
        for line in file:
           if any(keyword in line for keyword in keywords):
            print(line.strip())

logfile = "application.log"

if __name__ == "__main__":
    log_file_check(logfile)