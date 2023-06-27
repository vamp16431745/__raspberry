import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep
import requests





if __name__ == "__main__":
    mcp3008_ch7 = zero.MCP3008(channel=7) # 偵測第7個頻
    mcp3008_ch6=zero.MCP3008(channel=6) # 偵測第6個頻
    try:
        while True:
             value = round(mcp3008_ch7.value*100)

             print("光敏電阻值: ",value)
             if value > 20:
                 print("光線亮")
             else:
                 print("光線暗")

                 print("LM35: ",mcp3008_ch6.value*100*3.3)

                 requests.get(f'https://vamp16431745-laughing-winner-6pw4jvx5vvg359r7-8000.preview.app.github.dev/raspberry?light={value}&temperature={mcp3008_ch6.value*100*3.3}')
                     
             sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程式退函數")    