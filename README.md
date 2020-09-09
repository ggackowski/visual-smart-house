# visual-smart-house
Python app that visualizes state of a smart home. 

# Usage

To run the app, just type:

    python3 main.py

App uses a config file named .vsm_config, that must be in this format:

  <json config file> 
  <mqtt host> 
  <mqtt port>
  <mqtt topic>

If no config file provided, app will run with default configuration:

  data/default.json
  localhost
  1883
  ok

Application also uses a JSON configuration file, that is described below. 

# JSON config file

    {
      "plan": {
       <room-name (string)>: {
        "width": <width (number)>,
        "height": <height (number)>,
        "elements": [
          {
            "type": <element type (string)>,
            "position": {
              "x": <x (number)>,
              "y": <y (number)>
            },
            "id": <id (string)>
          }
        ]
      }
      }
    }
    
possible types of elements (devices): 
- Windows ("window")
- Lamps ("lamp")
- Motion sensors ("motion_sensor")

# Connection with a MQTT broker

App connects with a MQTT broker and can understand a message in this format:

    "<room-name>/<device id>/<action>"  
  
Possible actions differ among different devices and are shown below.

Example message (using Mosquitto):

  mosquitto_pub -t "ok" -m "toilet/1/open"
  
# Window

Windows can be open ("/open") or closed ("/close").

# Lamp

Lamps can be turned on ("/on") or off ("/off").

# Motion sensor

Motions sensor can detect motion ("/movement"). It indicates it for fixed amount of time.

# Preview

![Screenshot](/sample_screenshot.png)
