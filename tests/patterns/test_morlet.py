import numpy as np
from matplotlib import pyplot as plt
from waveform_factory.patterns.morlet import generate_morlet_wave

class MorletWaveTest:
    def run_tests(self):
        self.test_generate_morlet_wave()

    def test_generate_morlet_wave(self):
        # Define the "baseline" parameters
        baseline_frequency = 4
        baseline_amplitude = 10.0
        baseline_offset = 0.0
        baseline_phase_shift = 0.0
        baseline_sample_rate = 900

        # Define the variations for each parameter
        frequency_variations = [2, 20]
        amplitude_variations = [0.5, 0.7]
        offset_variations = [-0.5, 0.5]
        phase_shift_variations = [np.pi / 2, np.pi]
        sample_rate_variations = [22050, 88200]
        invert_variations = [True, False]

        # Define colors for the plot
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        # Start the plot
        plt.figure(figsize=(18, 12))

        # Generate and plot the "baseline" Morlet wavelet
        baseline_wave = generate_morlet_wave(baseline_frequency, baseline_amplitude, 2.0, baseline_sample_rate,
                                             baseline_phase_shift, baseline_offset)
        plt.plot(np.real(baseline_wave)[:10000], color=colors[0], label='Real (baseline)')
        plt.plot(np.imag(baseline_wave)[:10000], color=colors[1], label='Imaginary (baseline)')

        # Generate and plot Morlet wavelets for each variation of the parameters
        color_index = 2
        for frequency in frequency_variations:
            wave = generate_morlet_wave(frequency, baseline_amplitude, 2.0, baseline_sample_rate,
                                        baseline_phase_shift, baseline_offset)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'freq={frequency}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'freq={frequency}, imag')
            color_index += 2

        for amplitude in amplitude_variations:
            wave = generate_morlet_wave(baseline_frequency, amplitude, 2.0, baseline_sample_rate,
                                        baseline_phase_shift, baseline_offset)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'amp={amplitude}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'amp={amplitude}, imag')
            color_index += 2

        for offset in offset_variations:
            wave = generate_morlet_wave(baseline_frequency, baseline_amplitude, 2.0, baseline_sample_rate,
                                        baseline_phase_shift, offset)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'offset={offset}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'offset={offset}, imag')
            color_index += 2

        for phase_shift in phase_shift_variations:
            wave = generate_morlet_wave(baseline_frequency, baseline_amplitude, 2.0, baseline_sample_rate,
                                        phase_shift, baseline_offset)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'phase={phase_shift}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'phase={phase_shift}, imag')
            color_index += 2

        for sample_rate in sample_rate_variations:
            wave = generate_morlet_wave(baseline_frequency, baseline_amplitude, 2.0, sample_rate,
                                        baseline_phase_shift, baseline_offset)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'sr={sample_rate}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'sr={sample_rate}, imag')
            color_index += 2

        for invert in invert_variations:
            wave = generate_morlet_wave(baseline_frequency, baseline_amplitude, 2.0, baseline_sample_rate,
                                        baseline_phase_shift, baseline_offset, invert=invert)
            plt.plot(np.real(wave)[:10000], color=colors[color_index % len(colors)], label=f'invert={invert}, real')
            plt.plot(np.imag(wave)[:10000], color=colors[(color_index + 1) % len(colors)], label=f'invert={invert}, imag')
            color_index += 2

        # Show the plot with a legend
        plt.title('Morlet Wavelet')
        plt.legend(loc='upper right')
        plt.show()

# Create an instance of the test class and run the tests
morlet_wave_test = MorletWaveTest()
morlet_wave_test.run_tests()
