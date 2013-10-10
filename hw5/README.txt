Problem 1:
The codes are in 'p1_client.py' and 'p1_server.py'. You can run them by typing: python p1_client.py or python p1_server.py.
The imgs on client side are saved in 'client_original.png' and 'client_manipulated.png'
The data of the imgs on server side are saved in 'server_original.p' and 'server_manipulated.p'
The port being used is 5054. Hopefully, it is free.

Problem 2:
1) It took me forever to process an .aig file. I don't have time to run through them. I record a .wav file of myself's voice. You can see the voice waveform and spectrum by running it in terminal as follow:
python p2.py myvoice.wav
 
You can see a peak at about 150 Hz, which is in the range of human voice's fundamental frequency 85 - 180 Hz according to Wikipedia.

You won't be able to run it for .aig file for now. I am using  'wave.open' instead of 'aifc.open' because I know I am gonna run a .wav file. If you wanna try for a .aig file, you can go to 21st line in p2.py and change 'wave' to 'aifc'.