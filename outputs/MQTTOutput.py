import os
import PluginLoader
import paho.mqtt.client as mqtt
import json
import datetime

# Define Variables
MQTT_HOST = "192.168.3.10"
MQTT_PORT = 1883
MQTT_USER = "User"
MQTT_PASS = "Password"
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "tele/inverter/SENSOR"

#######################################################################
class ConsoleOutput(PluginLoader.Plugin):
    """Outputs the data from the Omnik inverter to stdout"""
    def process_message(self, msg):
        """Output the information from the inverter to stdout.
        Args:
            msg (InverterMsg.InverterMsg): Message to process
        """
        actual_time = datetime.datetime.now().replace(microsecond=0).isoformat()

        json_body={"Time":actual_time,"ENERGY":{"Temp":(msg.temperature),"H_Total":(msg.h_total),"E_Today":(msg.e_today),"E_Total":(msg.e_total),"VPV1":(msg.v_pv(1)),"$
        mqttc = mqtt.Client("inverter")
        mqttc.username_pw_set(username=MQTT_USER, password=MQTT_PASS)
        mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
        mqtt_msg=json.dumps(json_body)
        mqttc.publish(MQTT_TOPIC, mqtt_msg)
        mqttc.disconnect()
