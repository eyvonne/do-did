import time
from ringBuffer import RingBuffer
import math
import subprocess
import sys

def send_icmp_pings(target_ip="google.com", buffer_size=50, tolerance=1):
    # Create a ring buffer
    ring_buffer = RingBuffer(buffer_size) 

    # Send continuous ICMP pings
    while True:
        # Send a ping and measure the travel time
        command = build_command(target_ip)
        ping_response = catch_ping_response(command)

        # this is for testing to make sure everything is working
        # TODO: remove this
        send_notification(ping_response)

        travel_time = parse_ping_time(ping_response)
        
        if travel_time == -1:
            send_notification('ping failed')
            time.sleep(1)
            continue

        devs = std_devs(ring_buffer, travel_time)
        
        if devs > tolerance:
            send_notification('ping time spiked')
        if devs < tolerance * -1: 
            send_notification('ping time dropped')

        # Add the travel time to the ring buffer
        ring_buffer.append(travel_time)

        # Add a delay of 1 second between pings
        time.sleep(1)

def catch_ping_response(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8')

def std_devs(buffer, ping): 
    if buffer.count == 0:
        return 0
    avg = buffer.get_average()
    variance = buffer.get_std_dev()
    return math.ceil((ping - avg) / variance)

def parse_ping_time(ping):
    # Parse the output of the ping command at the end of the script
    # and return the ping time in milliseconds
    # a ping looks like this:
    # 64 bytes from 142.251.33.78: icmp_seq=0 ttl=113 time=52.007 ms
    ping_time = ping.split('time=')[1].split(' ')[0]
    try:
        return float(ping_time)
    except: 
        return -1

def build_command(target_ip):
    # Build the command to send an ICMP ping
    return ['ping', '-c', '1', target_ip]


def send_notification(notification):
    subprocess.call(['osascript', '-e', 'display notification "{}" with title "Ping Problem"'.format(notification)])

if __name__ == '__main__':
    print('Starting ping monitor...')
    send_icmp_pings()
