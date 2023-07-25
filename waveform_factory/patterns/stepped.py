import numpy as np
from matplotlib import pyplot as plt
def generate_stepped_wave(total_periods: int, step_info: list, sample_rate: int = 44100, length: float = 1.0,
                          offset: float = 0.0):
    """
    Generates a stepped wave (staircase) with added features.

    :param total_periods: The total number of periods in the waveform.
    :param step_info: A list of dictionaries containing step information.
                      Each dictionary should have 'height', 'start_period', and 'stop_period' keys.
    :param sample_rate: The sample rate for the wave. Default is 44100Hz (standard audio CD sample rate).
    :param length: The total length of the wave in seconds.
    :param offset: The DC offset of the wave. Default is 0.0.
    :return: A numpy array representing the generated wave.
    """
    total_samples = int(sample_rate * length)
    period_length = total_samples // total_periods

    waveform = np.zeros(total_samples)

    for step in step_info:
        height = step['height']
        start_period = step['start_period']
        stop_period = step['stop_period']

        start_sample = start_period * period_length
        stop_sample = stop_period * period_length

        # Generate the step waveform
        step_wave = np.ones(stop_sample - start_sample) * height

        # Add the step waveform to the main waveform
        waveform[start_sample:stop_sample] = step_wave

    waveform += offset  # Apply DC offset

    return waveform
