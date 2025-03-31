import matplotlib.pyplot as plt
import numpy as np
from DHO924S import DHO924S
#from DS1054Z import DS1054Z
scope = DHO924S('192.168.0.127')
#scope = DS1054Z('169.254.14.240')
print("Connected to: ", scope.idn)
scope.run()
scope.display_channel(1, enable=True)
scope.display_channel(2, enable=True)
scope.display_channel(3, enable=True)
scope.display_channel(4, enable=True)

scope.memory_depth = 10e3
scope.set_probe_ratio(1,1000)
scope.set_probe_ratio(2,100)
scope.set_probe_ratio(3,100)
scope.set_probe_ratio(4,100)

scope.write(":TRIGger:EDGE:SOURce CHAN1")
scope.write(":TRIGger:EDGE:SLOPe POS")   
scope.write(":TRIGger:NREJect 0")
scope.write(":TRIGger:COUPling DC")
scope.write(":TRIGger:MODE EDGE")
scope.write(":TRIGger:EDGE:LEVel 1000")
scope.write(":CHANnel1:BWLimit 20M")

scope.set_channel_scale(1,2000, use_closest_match=False)
scope.set_channel_offset(1, -2500)
scope.set_channel_scale(2,200, use_closest_match=False)

scope.set_channel_scale(3,200, use_closest_match=False)
scope.set_channel_offset(3, -200)
scope.set_channel_scale(4,200, use_closest_match=False)
scope.set_channel_offset(4, -200)

scope.timebase_offset = 300e-6
scope.timebase_scale = 100e-6
print(scope.sample_rate)    

scope.tforce()

print("trigger forced")
print(scope.memory_depth)

ch1 = Oscope.read_chanel_converted(1)
ch2 = Oscope.read_chanel_converted(2)

plt.plot(scope.waveform_time_values,ch1)
plt.plot(scope.waveform_time_values,ch2)

plt.show()

scope.SourceOutputON()
scope.SourceWaveSquare()
scope.SourceAmplitude = 2
scope.SourceSquareDuty = 0.1
scope.SourceFrequency = 3e3
scope.SourceOffset = 1

scope.single()
#time.sleep(0.5)
while(scope.running == True):
    print("Waiting")

print("Memdepth",scope.memory_depth)
sCH1 = scope.get_waveform_samples(1, mode='NORMal')
TCH1 = scope.waveform_time_values

sCH1B = scope.get_waveform_samples(1, mode='RAW')
TCH1B = scope.waveform_time_values

sCH2 = scope.get_waveform_samples(2, mode='NORMal')
TCH2 = scope.waveform_time_values

sCH2B = scope.get_waveform_samples(2, mode='RAW')
TCH2B = scope.waveform_time_values

plt.plot(TCH1B,sCH1B)
plt.plot(TCH1,sCH1)


plt.plot(TCH2B,sCH2B)
plt.plot(TCH2,sCH2)
plt.show()
