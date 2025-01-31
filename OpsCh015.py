# We are going to use the psutil command to format a script to check these items.  cpu times, cpu percentatge, disk partion's, users and net connections.
# You may have to do some extra modification to make the ouput be more readable.


import psutil
import datetime

def get_cpu_info():
  print("=== CPU Information ===")
  print(f"CPU Times: {psutil.cpu_times()}")
  print(f"CPU Percentage: {psutil.cpu_percent(interval=1)}%\n")

def get_disk_info():
  print("=== Disk Partitions ===")
  for partition in psutil.disk_partitions():
    print(f"Device: {partition.device}")
    print(f" Mountpoint: {partition.mountpoint}")
    print(f" Filesystem: {partition.fstype}\n")

def get_users_info():
  print("=== Logged-in Users ===")
  users = psutil.users()
  for user in users:
    print(f"User: {user.name}, Terminal: {user.terminal}, Host: {user.host}, Login Time: {datetime.datetime.fromtimestamp(user.started)}")
  print()

def get_net_connections():
  print("=== Network Connections ===")
  for conn in psutil.net_connections(kind='inet'):
    print(f"Family: {conn.family.name}, Type: {conn.type.name}, Local Addr: {conn.laddr}, Remote Addr: {conn.raddr}, Status: {conn.status}")
    print()

def main():
  get_cpu_info()
  get_disk_info()
  get_users_info()
  get_net_connections()

if __name__ == "__main__":
  main()




