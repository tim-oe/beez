import serial
import io

# test program for seeedstudio LoRa-E5
# see https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/

def send(sio, ser, cmd):
    sio.write(cmd)
    sio.flush()
    ser.flush()

ser = serial.Serial("/dev/serial0")  # Open named port
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

print(ser.name)
# see https://files.seeedstudio.com/products/317990687/res/LoRa-E5%20module%20datasheet_V1.0.pdf
send(sio, ser, "AT+VER\n")
send(sio, ser, "AT+ID\n")
send(sio, ser, "AT+PORT=?\n")
send(sio, ser, "AT+ADR=?\n")
# set to us freg
# send(sio, ser, "AT+DR=US915\n")
send(sio, ser, "AT+DR\n")
send(sio, ser, "AT+CH=NUM\n")
# range based on command above
# for x in range(71):
#    send(sio, ser, "AT+CH=%d\n" % x)
# set app key
# ser.write(str.encode('AT+KEY=APPKEY,"e7565893d479a2a2be7599603de2eed3"'))

# TODO connect to gateway, send data packet

ser.close()
