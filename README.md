# pulscode
pulse code modulation 
this is version 0.1.in this version I thought to make the  command line 
interface. 
 This is complete to do according to the belove lab file... 


Data Communication Department of Computer Science #####
Lab Assignment 1 – Pulse Code Modulation
We learned about Pulse Code Modulation (PCM), a technique that is used to convert an analog signal to a digital signal. In this lab you will implement a Pulse Code Modulator as a Python program.
The following figure shows the main components involved in PCM.
In this lab, you will implement the Pulse Code Modulator in a modular way where each module will be responsible for a specific PCM function. Moreover, to test and showcase the operation of your PCM program, you will need to implement a simple analog signal generator. Thus, the following modules need to be implemented.
1. Analog Signal Generator
2. Sampler
3. Quantizer
4. Encoder
Rest of this document provides instructions regarding implementing these four components.
Lab 2.1 Analog Signal Generator
def analog_signal_generator(A, omega, sigma, duration, t):
For simplicity, we assume only a sinusoidal analog will be used for this lab. As you should already know, any sinusoidal signal can be represented with 𝑥(𝑡)=𝐴sin(𝜔𝑡+ 𝜎)
Where t is time, A is the peak amplitude, 𝜔 is the angular frequency in radians, and 𝜎 is the phase in radians. duration is the number of time units that the signal exists.
The analog signal generator function will take as input A, omega, sigma, and t, and output the signal value x(t) at time t given the input values.
Lab 2.2 Sampler
def sampler(samples, interval, A, omega, sigma, duration)
The sampler function takes as input a list where samples will be stored, the sampling interval and the analog signal and updates the samples array with the relevant sample values.
Lab 2.3 Quantizer
def quantizer(samples, pcmpulses, levels)
The quantizer function takes as input the samples list, the pcmpulses list where the output of quantizer will be stored, and the number of quantization levels, and produces PCM pulses accordingly.
For simplicity, in this lab assignment, please take the “floor” value as the quantized value. Quantization logic can be expressed with the following formula: 𝑄𝑙𝑒𝑣𝑒𝑙(𝑡)=⌊((𝑥(𝑡)−𝐴𝑚𝑖𝑛𝐴𝑚𝑎𝑥−𝐴𝑚𝑖𝑛) ×𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑄𝑢𝑎𝑛𝑡𝑖𝑧𝑎𝑡𝑖𝑜𝑛 𝐿𝑒𝑣𝑒𝑙𝑠)⌋
When 𝑥(𝑡)= 𝐴𝑚𝑎𝑥 the quantization level should be set to maximum quantization level.
Lab 2.4 Encoder
def encoder(pcmpulses, encoderbits)
The encoder takes as input pcmpulses list and the number of bits used for a single PCM code. It returns a list dsignal where output will be stored. It produces the PCM codes for each pulse recorded and stores in dsignal as a binary number stream.
The void run() function
In addition to the main components, you need to have a run() function that does the following:
1. Reads the following input parameters from the stdin. These will be given as space-separated values.
A omega sigma duration interval encoderbits
2. Prints the final output as a bit stream (consisting of 1s and 0s).
3. Perform any other auxiliary tasks, if necessary.
Example
Suppose the analog signal is x(t) = 3 sin(2t + 0).
Also assume that the signal duration = 5
Given these facts a possible input string is: 3 2 0 5 1 2
In this input string
A = 3 omega = 2 sigma = 0 duration = 5 interval = 1 encoderbits = 2
Thus, you should generate the sine wave using the give values, take samples every 1 time unit, assign samples into one of 4 quantization levels (since we are using 2 encoderbits as per the input string), and produce the encoder output bitstream. Please note that the quantization levels should span from the minimum peak to the maximum peak. In other words, quantization levels should cover both -3 as well as +3. In this example, quantization level 0 should start at -3 and, quantization level 3 should correspond to +3.
The samples from t=0 to t=5 will be as follows.
When t = 0; x(0) = 0 When t = 1; x(1) = 2.73 When t = 2; x(2) = -2.27 When t = 3; x(3) = -0.84 When t = 4; x(4) = 2.97 When t = 5; x(5) = -1.63
Calculating quantization levels:
𝑄𝑙𝑒𝑣𝑒𝑙(𝑡)=⌊((𝑥(𝑡)−𝐴𝑚𝑖𝑛𝐴𝑚𝑎𝑥−𝐴𝑚𝑖𝑛) ×𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑄𝑢𝑎𝑛𝑡𝑖𝑧𝑎𝑡𝑖𝑜𝑛 𝐿𝑒𝑣𝑒𝑙𝑠)⌋
When t = 0; x(0) = 0
𝑄𝑙𝑒𝑣𝑒𝑙(0)=⌊(0−(−3)3−(−3)) ×4 ⌋=2
When t = 1; x(1) = 2.73
𝑄𝑙𝑒𝑣𝑒𝑙(1)=⌊(2.73−(−3)3−(−3)) ×4 ⌋=3
When t = 2; x(2) = -2.27
𝑄𝑙𝑒𝑣𝑒𝑙(2)=⌊(−2.27−(−3)3−(−3)) ×4 ⌋=0
When t = 3; x(3) = -0.84
𝑄𝑙𝑒𝑣𝑒𝑙(3)=⌊(−0.84−(−3)3−(−3)) ×4 ⌋=1
When t = 4; x(4) = 2.97
𝑄𝑙𝑒𝑣𝑒𝑙(4)=⌊(2.97−(−3)3−(−3)) ×4 ⌋=3
When t = 5; x(5) = -1.63
𝑄𝑙𝑒𝑣𝑒𝑙(5)=⌊(−1.63−(−3)3−(−3)) ×4 ⌋=0
Thus, the PCM encoded output binary stream for the given analog signal is:
101100011100
Please try out different analog signals by changing the input parameters test the correctness of your program before submitting.
Submission Instructions
You need to write a Python file for the above task and exactly produce the output in the same format as the bit stream shown above as this assignment will be automatically graded (for multiple test cases).
Submit a single Python file named with the degree and numeric part of your registration number (eg. MIS010111.py) to the LMS submission link by the deadline.
Please note that this is an individual assignment, and those who are caught plagiarizing will be penalized and will be reported for disciplinary action.