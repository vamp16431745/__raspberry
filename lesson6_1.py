import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import requests



if __name__ == "__main__":
    mcp3008_ch7 = zero.MCP3008(channel=7)
    mcp3008_ch6 = zero.MCP3008(channel=6)
    try:
        while True:
            value = round(mcp3008_ch7.value*100)
            print("lightValue: ", value)
            if value > 20:
                print("Light_on")
            else:
                print("Light_out") 

            datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            response = requests.get(f'https://fastapi-26zh.onrender.com/raspberry?time={datetimeStr}light={value}&temperature={mcp3008_ch6.value*1000}')

            # response = requests.get(f'https://vamp16431745-animated-space-orbit-rxwpj756r9935jjx-8000.preview.app.github.dev/raspberry?time={datetimeStr}light={value}&temperature={mcp3008_ch6.value*1000}')

            

            
            if response.ok:
                print("file_upload")
                print(response.text)
            else:
                print(response.status_code)

            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("exit")