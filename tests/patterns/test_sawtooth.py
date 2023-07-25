import numpy as np
from matplotlib import pyplot as plt

from waveform_factory.patterns.sawtooth import generate_sawtooth_wave

class SawtoothWaveTest:
    def run_tests(self):
        self.test_generate_sawtooth_wave()

    def test_generate_sawtooth_wave(self):
        # Define the "baseline" parameters
        baseline_frequency = 440
        baseline_amplitude = 1.0
        baseline_length = 1.0
        baseline_sample_rate = 44100
        baseline_phase_shift = 0.0
        baseline_offset = 0.0
        baseline_invert = False

        # Define the variations for each parameter
        frequency_variations = [220, 880]
        amplitude_variations = [0.5, 2.0]
        length_variations = [0.5, 2.0]
        sample_rate_variations = [22050, 88200]
        phase_shift_variations = [np.pi/2, np.pi]
        offset_variations = [-0.5, 0.5]
        invert_variations = [True, False]

        # Define colors for the plot
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        # Start the plot
        plt.figure(figsize=(18, 12))

        # Generate and plot the "baseline" sawtooth wave
        baseline_wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, baseline_length,
                                               baseline_sample_rate, baseline_phase_shift, baseline_offset,
                                               baseline_invert)
        plt.plot(baseline_wave[:1000], color=colors[0], label='baseline')

        # Generate and plot sawtooth waves for each variation of the parameters
        color_index = 1
        for frequency in frequency_variations:
            wave = generate_sawtooth_wave(frequency, baseline_amplitude, baseline_length, baseline_sample_rate,
                                          baseline_phase_shift, baseline_offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'freq={frequency}')
            color_index += 1

        for amplitude in amplitude_variations:
            wave = generate_sawtooth_wave(baseline_frequency, amplitude, baseline_length, baseline_sample_rate,
                                          baseline_phase_shift, baseline_offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'amp={amplitude}')
            color_index += 1

        for length in length_variations:
            wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, length, baseline_sample_rate,
                                          baseline_phase_shift, baseline_offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'length={length}')
            color_index += 1

        for sample_rate in sample_rate_variations:
            wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, baseline_length, sample_rate,
                                          baseline_phase_shift, baseline_offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'sr={sample_rate}')
            color_index += 1

        for phase_shift in phase_shift_variations:
            wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, baseline_length, baseline_sample_rate,
                                          phase_shift, baseline_offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'phase={phase_shift}')
            color_index += 1

        for offset in offset_variations:
            wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, baseline_length, baseline_sample_rate,
                                          baseline_phase_shift, offset, baseline_invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'offset={offset}')
            color_index += 1

        for invert in invert_variations:
            wave = generate_sawtooth_wave(baseline_frequency, baseline_amplitude, baseline_length, baseline_sample_rate,
                                          baseline_phase_shift, baseline_offset, invert)
            plt.plot(wave[:1000], color=colors[color_index % len(colors)], label=f'invert={invert}')
            color_index += 1

        # Show the plot with a legend
        plt.title('Sawtooth Wave')
        plt.legend(loc='upper right')
        plt.show()

# Create an instance of the test class and run the tests
sawtooth_wave_test = SawtoothWaveTest()
sawtooth_wave_test.run_tests()
