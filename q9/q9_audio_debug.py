import wave
import numpy as np

wf = wave.open('forensics-audio.wav', 'rb')
n_frames = wf.getnframes()
framerate = wf.getframerate()
audio_data = wf.readframes(n_frames)
wf.close()

samples = np.frombuffer(audio_data, dtype=np.int16)

freq_map = {
    400: '0', 560: '1', 720: '2', 880: '3',
    1040: '4', 1200: '5', 1360: '6', 1520: '7',
    1680: '8', 1840: '9', 2000: 'a', 2160: 'b',
    2320: 'c', 2480: 'd', 2640: 'e', 2800: 'f'
}

tone_length = int(0.25 * framerate)
stride = int(0.29 * framerate)

for i in range(8):
    start = i * stride
    end = start + tone_length
    segment = samples[start:end]
    
    fft_out = np.fft.fft(segment)
    freqs = np.fft.fftfreq(len(segment), 1.0/framerate)
    pos_mask = freqs > 0
    peak_idx = np.argmax(np.abs(fft_out[pos_mask]))
    peak_freq = freqs[pos_mask][peak_idx]
    
    closest_freq = min(freq_map.keys(), key=lambda f: abs(f - peak_freq))
    print(f"Tone {i}: detected={peak_freq:.1f} closest={closest_freq} char={freq_map[closest_freq]}")
