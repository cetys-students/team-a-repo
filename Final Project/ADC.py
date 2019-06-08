import spidev
import time
import RPi.GPIO as GPIO

class MCP3204:
        def __init__(self, spi_channel=0):
                self.spi_channel = spi_channel
                self.conn = spidev.SpiDev(0, spi_channel)
                self.conn.max_speed_hz = 1000000 # 1MHz

        def __del__( self ):
                self.close

        def close(self):
                if self.conn != None:
                        self.conn.close
                        self.conn = None

        def bitstring(self, n):
                s = bin(n)[2:]
                return '0'*(8-len(s)) + s

        def read(self, adc_channel=0):
                # build command
                cmd  = 128 # start bit
                cmd +=  64 # single end / diff
                if adc_channel % 2 == 1:
                        cmd += 8
                if (adc_channel/2) % 2 == 1:
                        cmd += 16
                if (adc_channel/4) % 2 == 1:
                        cmd += 32

                # send & receive data
                reply_bytes = self.conn.xfer2([cmd, 0, 0, 0])

                #
                reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes)


                # see also... http://akizukidenshi.com/download/MCP3204.pdf (page.20)
                reply = reply_bitstring[5:19]
                return int(reply, 2)

        def readAverage(self, adc_channel=0, nAverage=128, bDebug=0):
                        raw = 0
                        for i in range(nAverage):
                                raw += self.read(adc_channel)
                        fMean = raw / nAverage

                        if bDebug:
                                print('nAverage={:d}: mean value={:7.2f}ticks'.format(nAverage, fMean))
                        return fMean

