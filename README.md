# DHO924S
Quick hack to communicate with the new Rigol DHO924S. Get 12bit samples and use the signal generator. 
This is a dirty modification of https://github.com/pklaus/ds1054z.
Some things are changed in the Waveform preamble and dont behave the same way as in the ds1054z.
Also we had to change the data donwload to WORD, so we get the full 12bit samples.

This code is as is, take more like an example not a stable solution.
Sometimes the scope needs restarted if does not behave as expected.
