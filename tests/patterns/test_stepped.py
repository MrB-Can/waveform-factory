import unittest
import numpy as np
from waveform_factory.patterns.stepped import generate_stepped_wave
from matplotlib import pyplot as plt
def test_generate_stepped_wave():
    total_periods = 16
    step_info = [{'height': 0.5, 'start_period': 1, 'stop_period': 2},
                 {'height': 0.8, 'start_period': 2, 'stop_period': 4},
                 {'height': 0.9, 'start_period': 4, 'stop_period': 9},
                 {'height': 0.5, 'start_period': 9, 'stop_period': 10},
                 {'height': 0.1, 'start_period': 10, 'stop_period': 12},
                 {'height': -1, 'start_period': 12, 'stop_period': 14}]
    sample_rate = 100000
    length = 1.0

    # Generate the waveform
    waveform = generate_stepped_wave(total_periods, step_info, sample_rate, length)

    # Plot the waveform
    plt.plot(waveform)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title('Generated Stepped Waveform')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    unittest.main()
