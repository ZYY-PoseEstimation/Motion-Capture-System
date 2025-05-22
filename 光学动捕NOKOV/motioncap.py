#UDP远程触发惯性动捕
import socket
import json
import time

class XsensTrigger:
    def __init__(self, host='127.0.0.1', port=9763):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP协议
    
    def send_trigger(self, command):
        """发送开始/停止录制的JSON指令"""
        message = json.dumps({
            "command": "start_recording",  # "start_recording" 或 "stop_recording"
            "timestamp": time.strftime("%H:%M:%S", time.gmtime())
        }).encode()
        self.sock.sendto(message, (self.host, self.port))
        print(f"Sent {command} to Xsens at {self.host}:{self.port}")


if __name__ == '__main__':
    trigger = XsensTrigger()
    trigger.send_trigger("start_recording")  # 开始采集
