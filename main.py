import tkinter as tk
import math
import socket
import struct
import time
import threading


def fetch_ntp_time(ntp_server="pool.ntp.org", ntp_port=123):
    TIME1970 = 2208988800
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ntp_data = b'\x1b' + 47 * b'\0'
    client.sendto(ntp_data, (ntp_server, ntp_port))
    ntp_response, _ = client.recvfrom(1024)
    unpack_str = '!12I'
    ntp_response = struct.unpack(unpack_str, ntp_response)
    timestamp = ntp_response[10] - TIME1970
    return timestamp


lock = threading.Lock()
real_timestamp = [fetch_ntp_time() - 1]


def calculate_game_time(real_timestamp):
    SECONDS_IN_HOUR = 3600

    # Calculate the number of seconds elapsed since the top of the real-world hour
    seconds_since_hour = real_timestamp % SECONDS_IN_HOUR

    # Calculate the 'game hour' and 'game minute'
    game_hour = (seconds_since_hour // 150) % 24
    game_minute = (seconds_since_hour % 150) // 2.5

    # game_time_str = f"{int(game_hour):02d}:{int(game_minute):02d}"
    return (game_hour, game_minute)


def update_timestamp(real_timestamp, lock):
    next_sync_time = real_timestamp[0] + 3600
    target_sleep_time = 1
    AVG_SLEEP_DELAY = 0.000356

    while True:
        start_time = time.time()
        with lock:
            real_timestamp[0] += 1
            if real_timestamp[0] >= next_sync_time:
                real_timestamp[0] = fetch_ntp_time()
                next_sync_time = real_timestamp[0] + 3600
        elapsed_time = time.time() - start_time
        sleep_duration = target_sleep_time - (elapsed_time + AVG_SLEEP_DELAY)

        if sleep_duration > 0:
            time.sleep(sleep_duration)


def draw_hand(canvas, x, y, length, angle, color, width, tag):
    end_x = x + length * math.cos(angle)
    end_y = y + length * math.sin(angle)
    canvas.create_line(x, y, end_x, end_y, fill=color,
                       width=width, tags=(tag, "hands"))
    # Draw translucent lines around the main line for faux anti-aliasing
    for i in range(1, 4):
        canvas.create_line(x, y, end_x, end_y, fill=color, width=width,
                           stipple='gray' + str(25 * i), tags=(tag, "hands"))


def update_time(lock, root, canvas, hour_hand, minute_hand):
    with lock:
        current_time = real_timestamp[0]

    hours, minutes = calculate_game_time(current_time)

    # Remove previous hands
    canvas.delete("hands")

    # Draw the hands with faux anti-aliasing
    draw_hand(canvas, 150, 150, 50, math.radians(30 * (hours %
              12) + minutes / 2 - 90), 'black', 6, "hour_hand")
    draw_hand(canvas, 150, 150, 70, math.radians(
        6 * minutes - 90), 'black', 4, "minute_hand")

    # Update every 100 ms (0.1 second)
    root.after(100, update_time, lock, root, canvas, hour_hand, minute_hand)


def main():
    root = tk.Tk()
    root.title("Palia Clock")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    # Draw clock circle
    canvas.create_oval(50, 50, 250, 250)

    # Draw numbers
    for i in range(1, 13):
        angle = math.radians(360 * (i / 12))
        x = 150 + 85 * math.cos(angle - math.pi / 2)
        y = 150 + 85 * math.sin(angle - math.pi / 2)
        canvas.create_text(x, y, text=str(i), font=("Arial", 18, "bold"))

    timestamp_thread = threading.Thread(
        target=update_timestamp, args=(real_timestamp, lock))
    timestamp_thread.daemon = True
    timestamp_thread.start()

    # Create clock hands; initial positions don't matter since update_time() will move them
    hour_hand = canvas.create_line(
        150, 150, 150, 100, width=6, fill='black', tags="hands")
    minute_hand = canvas.create_line(
        150, 150, 150, 50, width=4, fill='blue', tags="hands")

    # Draw central circle
    canvas.create_oval(145, 145, 155, 155, fill="black", tags="center")

    # Start the clock
    update_time(lock, root, canvas, hour_hand, minute_hand)

    root.mainloop()


if __name__ == '__main__':
    main()
