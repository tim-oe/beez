import serial
import io

# test program for seeedstudio LoRa-E5
# see https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/


def send(sio, ser, cmd):
    sio.write(cmd)
    sio.flush()
    ser.flush()


# seems to only work on 9600 baud
ser = serial.Serial("/dev/serial0", 9600, timeout=60, write_timeout=60)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# print(ser.name)
# print(ser.get_settings())
# print(ser.BAUDRATES)
# see https://files.seeedstudio.com/products/317990687/res/LoRa-E5%20module%20datasheet_V1.0.pdf
send(sio, ser, "AT+VER\n")
send(sio, ser, "AT+LW=VER\n")
send(sio, ser, "AT+TEMP\n")
# send(sio, ser, "AT+LW=LEN\n")
send(sio, ser, "AT+ID\n")
send(sio, ser, "AT+POWER\n")
send(sio, ser, "AT+PORT=?\n")
send(sio, ser, "AT+ADR=?\n")
# set to us freg
send(sio, ser, "AT+DR=US915\n")
send(sio, ser, "AT+DR=SCHEME\n")
# enable channels
send(sio, ser, "AT+CH=NUM, 8-15\n")
send(sio, ser, "AT+CH=NUM\n")
for x in range(8, 16):
    send(sio, ser, "AT+CH=%d\n" % x)
# set class
# send(sio, ser, "AT+CLASS=B,SAVE\n")
# send(sio, ser, "AT+CLASS\n")
#
# set app session keys
# only do one at a time
# send(sio, ser, 'AT+KEY=NWKSKEY, "b9 e5 57 0c 98 8e 4e fb f0 32 1d 99 ae 63 c2 06"\n')
# send(sio, ser, 'AT+KEY=APPSKEY, "4a fe 8f 63 77 30 52 69 10 3f 18 1a e7 63 09 28"\n')
# send(sio, ser, 'AT+KEY=APPKEY, "c2 11 ae 38 53 3a dc 50 e7 82 c4 2e 14 c4 d4 88"\n')
#
# set join mode
send(sio, ser, "AT+MODE=LWOTAA\n")
send(sio, ser, "AT+MODE\n")

# connect to gateway
#for x in range(10):
#    send(sio, ser, "AT+JOIN=FORCE\n")

ser.close()
