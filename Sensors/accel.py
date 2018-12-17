import smbus, time
import RPi.GPIO as GPIO

rev = GPIO.RPI_REVISION
bus = smbus.SMBus(1) if rev == 2 or rev == 3 else smbus.SMBus(0)

DEV_ADDR = 0x6A

CTRL1_XL_ADDR = 0x10
TAP_CFG_ADDR  = 0x58
TAP_THS_ADDR  = 0x59
INT_DUR2_ADDR = 0x5A
WAKE_THS_ADDR = 0x5B
MD1_CFG_ADDR  = 0x5E

CTRL1_XL_CMD = 0x60
TAP_CFG_CMD  = 0x0E
TAP_THS_CMD  = 0x01
INT_DUR2_CMD = 0x06
WAKE_THS_CMD = 0x00
MD1_CFG_CMD  = 0x40

INTERRUPT_VAL_TAP = 0x1C

def init():
	bus.write_byte_data(DEV_ADDR, CTRL1_XL_ADDR, CTRL1_XL_CMD)
	time.sleep(0.2)
	bus.write_byte_data(DEV_ADDR, TAP_CFG_ADDR,  TAP_CFG_CMD)
	time.sleep(0.2)
	bus.write_byte_data(DEV_ADDR, TAP_THS_ADDR,  TAP_THS_CMD)
	time.sleep(0.2)
	bus.write_byte_data(DEV_ADDR, INT_DUR2_ADDR, INT_DUR2_CMD)
	time.sleep(0.2)
	bus.write_byte_data(DEV_ADDR, WAKE_THS_ADDR, WAKE_THS_CMD)
	time.sleep(0.2)
	bus.write_byte_data(DEV_ADDR, MD1_CFG_ADDR,  MD1_CFG_CMD)
	time.sleep(0.2)
		
def isTapped():
	return True if bus.read_byte_data(DEV_ADDR, INTERRUPT_VAL_TAP) > 0 else False
