import psutil
import matplotlib.pyplot as plt

cpu_usage = []
ram_usage = []
timestamps = []

plt.ion()

for i in range(30):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    print(f"Czas: {i}, CPU: {cpu}%, RAM: {ram}%")

    cpu_usage.append(cpu)
    ram_usage.append(ram)
    timestamps.append(i)

    plt.clf()
    plt.plot(timestamps,cpu_usage, label='CPU Usage (%)', color="red") #ghjghkh
    plt.plot(timestamps,ram_usage, label='RAM Usage (%)', color="blue")
    plt.xlabel('Czas (s)')
    plt.ylim(0,110)
    plt.ylabel('Zużycie (%)')
    plt.title('Monitorowanie CPU i RAM')
    plt.legend()
    plt.pause(1)

plt.ioff()
plt.show()

