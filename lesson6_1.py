import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep
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

            response = requests.get(f'https://vamp16431745-ubiquitous-telegram-7xwpg7j5r44cp5p4-8000.preview.app.github.dev/raspberry?light={value}&temperature={mcp3008_ch6.value}')
            
            if response.ok:
                print("file_upload")
                print(response.text)
            else:
                print(response.status_code)

            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("exit")