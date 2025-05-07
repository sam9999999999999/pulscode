import math
#A = amplitude
#T = time
#w = frequency
#𝜎 = phase
# 14553



def analog_signal_generator(A, omega, sigma, duration, t):
    signalgen = round(A*math.sin(omega*t + sigma),2)
    #print(signalgen)
    return signalgen


def sampler(samples, interval, A, omega, sigma, duration):
    t=0
    while t <= duration:
        samples.append(analog_signal_generator(A, omega, sigma, duration, t))
        t += 1
    print(samples)

def quantizer(samples, pcmpulses, levels):
    A_max = max(samples)
    A_min = min(samples)
    for i in samples:
        Q_level = round(((i - (A_min)) / (A_max - A_min) * levels), 0)

        if round(A_max) < Q_level:
            Q_level = round(A_max)
            pcmpulses.append(Q_level)
        else:
            Q_level = int(Q_level)
            pcmpulses.append(Q_level)
    print(pcmpulses)


def encoder(pcmpulses, encoderbits):
    dsignal = []
    for x in pcmpulses:
        x=int(x)
        bits = format(x, 'b')
        bits = bits.zfill(encoderbits)
        dsignal.append(bits)
    print(''.join(dsignal))






A = float(input("Amplitude (A): "))
omega = float(input("Angular Frequency (omega): "))
sigma = float(input("Phase (sigma): "))
duration = float(input("Duration (in seconds): "))
interval = float(input("Sampling Interval (seconds): "))
encoderbits = int(input("Encoder Bits: "))
levels = 2**encoderbits

samples = []
pcmpulses = []

sampler(samples, interval, A, omega, sigma, duration)
quantizer(samples, pcmpulses, levels)
encoder(pcmpulses, encoderbits)


# while t <= duration:
#     analog_signal_generator(A, omega, sigma, duration, t)
#     t += 1
