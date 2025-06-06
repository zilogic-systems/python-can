"""
Contains Python equivalents of the function and constant
definitions in CANLIB's canstat.h, with some supporting functionality
specific to Python.

Copyright (C) 2010 Dynamic Controls
"""

import ctypes


class c_canStatus(ctypes.c_int):
    pass


# TODO better formatting
canOK = 0
canERR_PARAM = -1
canERR_NOMSG = -2
canERR_NOTFOUND = -3
canERR_NOMEM = -4
canERR_NOCHANNELS = -5
canERR_RESERVED_3 = -6
canERR_TIMEOUT = -7
canERR_NOTINITIALIZED = -8
canERR_NOHANDLES = -9
canERR_INVHANDLE = -10
canERR_INIFILE = -11
canERR_DRIVER = -12
canERR_TXBUFOFL = -13
canERR_RESERVED_1 = -14
canERR_HARDWARE = -15
canERR_DYNALOAD = -16
canERR_DYNALIB = -17
canERR_DYNAINIT = -18
canERR_NOT_SUPPORTED = -19
canERR_RESERVED_5 = -20
canERR_RESERVED_6 = -21
canERR_RESERVED_2 = -22
canERR_DRIVERLOAD = -23
canERR_DRIVERFAILED = -24
canERR_NOCONFIGMGR = -25
canERR_NOCARD = -26
canERR_RESERVED_7 = -27
canERR_REGISTRY = -28
canERR_LICENSE = -29
canERR_INTERNAL = -30
canERR_NO_ACCESS = -31
canERR_NOT_IMPLEMENTED = -32
canERR__RESERVED = -33


def CANSTATUS_SUCCESS(status):
    return status >= canOK


canMSG_MASK = 0x00FF
canMSG_RTR = 0x0001
canMSG_STD = 0x0002
canMSG_EXT = 0x0004
canMSG_WAKEUP = 0x0008
canMSG_NERR = 0x0010
canMSG_ERROR_FRAME = 0x0020
canMSG_TXACK = 0x0040
canMSG_TXRQ = 0x0080
canMSG_LOCAL_TXACK = 0x1000_0000

canFDMSG_FDF = 0x010000
canFDMSG_BRS = 0x020000
canFDMSG_ESI = 0x040000

canMSGERR_MASK = 0xFF00
canMSGERR_HW_OVERRUN = 0x0200
canMSGERR_SW_OVERRUN = 0x0400
canMSGERR_STUFF = 0x0800
canMSGERR_FORM = 0x1000
canMSGERR_CRC = 0x2000
canMSGERR_BIT0 = 0x4000
canMSGERR_BIT1 = 0x8000

canMSGERR_OVERRUN = 0x0600
canMSGERR_BIT = 0xC000
canMSGERR_BUSERR = 0xF800

canTRANSCEIVER_LINEMODE_NA = 0
canTRANSCEIVER_LINEMODE_SWC_SLEEP = 4
canTRANSCEIVER_LINEMODE_SWC_NORMAL = 5
canTRANSCEIVER_LINEMODE_SWC_FAST = 6
canTRANSCEIVER_LINEMODE_SWC_WAKEUP = 7
canTRANSCEIVER_LINEMODE_SLEEP = 8
canTRANSCEIVER_LINEMODE_NORMAL = 9
canTRANSCEIVER_LINEMODE_STDBY = 10
canTRANSCEIVER_LINEMODE_TT_CAN_H = 11
canTRANSCEIVER_LINEMODE_TT_CAN_L = 12
canTRANSCEIVER_LINEMODE_OEM1 = 13
canTRANSCEIVER_LINEMODE_OEM2 = 14
canTRANSCEIVER_LINEMODE_OEM3 = 15
canTRANSCEIVER_LINEMODE_OEM4 = 16
canTRANSCEIVER_RESNET_NA = 0
canTRANSCEIVER_RESNET_MASTER = 1
canTRANSCEIVER_RESNET_MASTER_STBY = 2
canTRANSCEIVER_RESNET_SLAVE = 3

canTRANSCEIVER_TYPE_UNKNOWN = 0
canTRANSCEIVER_TYPE_251 = 1
canTRANSCEIVER_TYPE_252 = 2
canTRANSCEIVER_TYPE_DNOPTO = 3
canTRANSCEIVER_TYPE_W210 = 4
canTRANSCEIVER_TYPE_SWC_PROTO = 5
canTRANSCEIVER_TYPE_SWC = 6
canTRANSCEIVER_TYPE_EVA = 7
canTRANSCEIVER_TYPE_FIBER = 8
canTRANSCEIVER_TYPE_K251 = 9
canTRANSCEIVER_TYPE_K = 10
canTRANSCEIVER_TYPE_1054_OPTO = 11
canTRANSCEIVER_TYPE_SWC_OPTO = 12
canTRANSCEIVER_TYPE_TT = 13
canTRANSCEIVER_TYPE_1050 = 14
canTRANSCEIVER_TYPE_1050_OPTO = 15
canTRANSCEIVER_TYPE_1041 = 16
canTRANSCEIVER_TYPE_1041_OPTO = 17
canTRANSCEIVER_TYPE_RS485 = 18
canTRANSCEIVER_TYPE_LIN = 19
canTRANSCEIVER_TYPE_KONE = 20
canTRANSCEIVER_TYPE_LINX_LIN = 64
canTRANSCEIVER_TYPE_LINX_J1708 = 66
canTRANSCEIVER_TYPE_LINX_K = 68
canTRANSCEIVER_TYPE_LINX_SWC = 70
canTRANSCEIVER_TYPE_LINX_LS = 72

canTransceiverTypeStrings = {
    canTRANSCEIVER_TYPE_UNKNOWN: "unknown",
    canTRANSCEIVER_TYPE_251: "82C251",
    canTRANSCEIVER_TYPE_252: "82C252/TJA1053/TJA1054",
    canTRANSCEIVER_TYPE_DNOPTO: "Optoisolated 82C251",
    canTRANSCEIVER_TYPE_W210: "W210",
    canTRANSCEIVER_TYPE_SWC_PROTO: "AU5790 prototype",
    canTRANSCEIVER_TYPE_SWC: "AU5790",
    canTRANSCEIVER_TYPE_EVA: "EVA",
    canTRANSCEIVER_TYPE_FIBER: "82C251 with fibre extension",
    canTRANSCEIVER_TYPE_K251: "K251",
    canTRANSCEIVER_TYPE_K: "K",
    canTRANSCEIVER_TYPE_1054_OPTO: "TJA1054 optical isolation",
    canTRANSCEIVER_TYPE_SWC_OPTO: "AU5790 optical isolation",
    canTRANSCEIVER_TYPE_TT: "B10011S Truck-And-Trailer",
    canTRANSCEIVER_TYPE_1050: "TJA1050",
    canTRANSCEIVER_TYPE_1050_OPTO: "TJA1050 optical isolation",
    canTRANSCEIVER_TYPE_1041: "TJA1041",
    canTRANSCEIVER_TYPE_1041_OPTO: "TJA1041 optical isolation",
    canTRANSCEIVER_TYPE_RS485: "RS485",
    canTRANSCEIVER_TYPE_LIN: "LIN",
    canTRANSCEIVER_TYPE_KONE: "KONE",
    canTRANSCEIVER_TYPE_LINX_LIN: "LINX_LIN",
    canTRANSCEIVER_TYPE_LINX_J1708: "LINX_J1708",
    canTRANSCEIVER_TYPE_LINX_K: "LINX_K",
    canTRANSCEIVER_TYPE_LINX_SWC: "LINX_SWC",
    canTRANSCEIVER_TYPE_LINX_LS: "LINX_LS",
}

canDRIVER_NORMAL = 4
canDRIVER_SILENT = 1
canDRIVER_SELFRECEPTION = 8
canDRIVER_OFF = 0

canOPEN_EXCLUSIVE = 0x0008
canOPEN_REQUIRE_EXTENDED = 0x0010
canOPEN_ACCEPT_VIRTUAL = 0x0020
canOPEN_OVERRIDE_EXCLUSIVE = 0x0040
canOPEN_REQUIRE_INIT_ACCESS = 0x0080
canOPEN_NO_INIT_ACCESS = 0x0100
canOPEN_ACCEPT_LARGE_DLC = 0x0200
canOPEN_CAN_FD = 0x0400
canOPEN_CAN_FD_NONISO = 0x0800

canIOCTL_GET_RX_BUFFER_LEVEL = 8
canIOCTL_GET_TX_BUFFER_LEVEL = 9
canIOCTL_FLUSH_RX_BUFFER = 10
canIOCTL_FLUSH_TX_BUFFER = 11
canIOCTL_GET_TIMER_SCALE = 12
canIOCTL_SET_TXRQ = 13
canIOCTL_GET_EVENTHANDLE = 14
canIOCTL_SET_BYPASS_MODE = 15
canIOCTL_SET_WAKEUP = 16
canIOCTL_GET_DRIVERHANDLE = 17
canIOCTL_MAP_RXQUEUE = 18
canIOCTL_GET_WAKEUP = 19
canIOCTL_SET_REPORT_ACCESS_ERRORS = 20
canIOCTL_GET_REPORT_ACCESS_ERRORS = 21
canIOCTL_CONNECT_TO_VIRTUAL_BUS = 22
canIOCTL_DISCONNECT_FROM_VIRTUAL_BUS = 23
canIOCTL_SET_USER_IOPORT = 24
canIOCTL_GET_USER_IOPORT = 25
canIOCTL_SET_BUFFER_WRAPAROUND_MODE = 26
canIOCTL_SET_RX_QUEUE_SIZE = 27
canIOCTL_SET_USB_THROTTLE = 28
canIOCTL_GET_USB_THROTTLE = 29
canIOCTL_SET_BUSON_TIME_AUTO_RESET = 30
canIOCTL_SET_LOCAL_TXECHO = 32
canIOCTL_SET_LOCAL_TXACK = 46
canIOCTL_PREFER_EXT = 1
canIOCTL_PREFER_STD = 2
canIOCTL_CLEAR_ERROR_COUNTERS = 5
canIOCTL_SET_TIMER_SCALE = 6
canIOCTL_SET_TXACK = 7

canCHANNELDATA_CHANNEL_CAP = 1
canCHANNELDATA_TRANS_CAP = 2
canCHANNELDATA_CHANNEL_FLAGS = 3
canCHANNELDATA_CARD_TYPE = 4
canCHANNELDATA_CARD_NUMBER = 5
canCHANNELDATA_CHAN_NO_ON_CARD = 6
canCHANNELDATA_CARD_SERIAL_NO = 7
canCHANNELDATA_TRANS_SERIAL_NO = 8
canCHANNELDATA_CARD_FIRMWARE_REV = 9
canCHANNELDATA_CARD_HARDWARE_REV = 10
canCHANNELDATA_CARD_UPC_NO = 11
canCHANNELDATA_TRANS_UPC_NO = 12
canCHANNELDATA_CHANNEL_NAME = 13
canCHANNELDATA_DLL_FILE_VERSION = 14
canCHANNELDATA_DLL_PRODUCT_VERSION = 15
canCHANNELDATA_DLL_FILETYPE = 16
canCHANNELDATA_TRANS_TYPE = 17
canCHANNELDATA_DEVICE_PHYSICAL_POSITION = 18
canCHANNELDATA_UI_NUMBER = 19
canCHANNELDATA_TIMESYNC_ENABLED = 20
canCHANNELDATA_DRIVER_FILE_VERSION = 21
canCHANNELDATA_DRIVER_PRODUCT_VERSION = 22
canCHANNELDATA_MFGNAME_UNICODE = 23
canCHANNELDATA_MFGNAME_ASCII = 24
canCHANNELDATA_DEVDESCR_UNICODE = 25
canCHANNELDATA_DEVDESCR_ASCII = 26
canCHANNELDATA_DRIVER_NAME = 27

kvLED_ACTION_ALL_LEDS_ON = 0
kvLED_ACTION_ALL_LEDS_OFF = 1

canBITRATE_1M = -1
canBITRATE_500K = -2
canBITRATE_250K = -3
canBITRATE_125K = -4
canBITRATE_100K = -5
canBITRATE_62K = -6
canBITRATE_50K = -7
canBITRATE_83K = -8
canBITRATE_10K = -9

canFD_BITRATE_500K_80P = -1000
canFD_BITRATE_1M_80P = -1001
canFD_BITRATE_2M_80P = -1002
canFD_BITRATE_4M_80P = -1003
canFD_BITRATE_8M_60P = -1004
