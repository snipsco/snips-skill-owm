#!/usr/bin/env python3
# encoding: utf-8

import argparse
import json
import paho.mqtt.client as mqtt

from weather import Weather

class Server:

    def __init__(self, mqtt_hostname, mqtt_port, api_key, default_location):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.mqtt_hostname = mqtt_hostname
        self.mqtt_port = mqtt_port
        self.weather = Weather(self, api_key, default_location)

    def start(self):
        print("[MQTT] Connecting to {} on port {}".format(
            self.mqtt_hostname, str(self.mqtt_port)))
        self.client.connect(self.mqtt_hostname, self.mqtt_port, 60)
        self.client.subscribe("#", 0)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("[MQTT] Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        print("[MQTT] Disconnected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        if (msg.topic == "hermes/nlu/intentParsed") and msg.payload:
            self.weather.handle_intent(json.loads(msg.payload.decode('utf-8')))

    def publish(self, topic, payload):
        self.client.publish(topic, payload=payload, qos=0, retain=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Start Weather Skills")
    parser.add_argument("--mqtt_host", type=str, default="localhost")
    parser.add_argument("--mqtt_port", type=int, default=9898)
    parser.add_argument("--owm_api_key", type=str, default=None)
    parser.add_argument("--default_location", type=str, default="Paris,fr")
    args = parser.parse_args()
    server = Server(args.mqtt_host,
        args.mqtt_port,
        args.owm_api_key,
        args.default_location)
    server.start()
