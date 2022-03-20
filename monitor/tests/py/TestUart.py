import serial
import io
import time

# test program for seeedstudio LoRa-E5
# see https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/


def send(sio, ser, cmd):
    sio.write(cmd)
    sio.flush()
    ser.flush()
    time.sleep(0.2)

    buff = ""

    while ser.inWaiting() > 0:
        buff += ser.read(1).decode()

    print(buff)


# seems to only work on 9600 baud
ser = serial.Serial("/dev/serial0", 9600, timeout=60, write_timeout=60)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# print(ser.name)
# print(ser.get_settings())
# print(ser.BAUDRATES)
# see https://files.seeedstudio.com/products/317990687/res/LoRa-E5%20module%20datasheet_V1.0.pdf
send(sio, ser, "AT+ID\n")
# send(sio, ser, "AT+LW=LEN\n")
send(sio, ser, "AT+POWER\n")
send(sio, ser, "AT+PORT=?\n")
send(sio, ser, "AT+ADR=?\n")
send(sio, ser, "AT+CH=NUM\n")
# set class, doesn't seem to take
send(sio, ser, "AT+CLASS=B,SAVE\n")
send(sio, ser, "AT+CLASS\n")
#
# set network app session keys
# send(sio, ser, 'AT+KEY=NWKSKEY, "b9 e5 57 0c 98 8e 4e fb f0 32 1d 99 ae 63 c2 06"\n')
# time.sleep(0.5)
# send(sio, ser, 'AT+KEY=APPSKEY, "4a fe 8f 63 77 30 52 69 10 3f 18 1a e7 63 09 28"\n')
# time.sleep(0.5)
# send(sio, ser, 'AT+KEY=APPKEY, "c2 11 ae 38 53 3a dc 50 e7 82 c4 2e 14 c4 d4 88"\n')
# time.sleep(0.5)

# baud rate
send(sio, ser, "AT+UART=BR\n")
# connect to gateway
# for x in range(10):
#    send(sio, ser, "AT+JOIN=FORCE\n")

ser.close()
