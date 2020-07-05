# visual-smart-house
Python app that visualizes the state of a smart home. 

# Usage

App uses a JSON configuration file described below. 
To run the app, just type:

    python3 main.py <json config file> <mqtt host> <mqtt port> <mqtt topic>

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

# Connection with MQTT broker

App connects with a MQTT broker and can understand a message in this format:

    "<room-name>/<device id>/<action>"  
  
Possible actions differ among different devices.
  
# Window

Window can be open ("/open") or closed ("/close").

# Lamp

Lamp can be turned on ("/on") or off ("/off").

# Motion sensor

Motion sensor can detect motion ("/movement"). It indicates it for fixed amount of time.

# Preview

As for now, very simple graphics.

![Screenshot](/sample_screenshot.png)
