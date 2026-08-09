import numpy as np
from PIL import Image
import wave

# Part 1: LSB in forensics-image.png
def solve_part1():
    img = Image.open('forensics-image.png').convert('RGB')
    pixels = np.array(img)
    # Extract blue channel (index 2)
    blue_channel = pixels[:, :, 2].flatten()
    # Extract LSB
    bits = blue_channel & 1
    
    # Pack into bytes (most significant bit first)
    chars = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break
        # Convert bit array to integer (MSB first)
        val = 0
        for b in byte_bits:
            val = (val << 1) | b
        if val == 0: # NUL byte
            break
        chars.append(chr(val))
    return "".join(chars)

# Part 2: Tone sequence in forensics-audio.wav
def solve_part2():
    wf = wave.open('forensics-audio.wav', 'rb')
    n_frames = wf.getnframes()
    framerate = wf.getframerate()
    audio_data = wf.readframes(n_frames)
    wf.close()
    
    # 16-bit mono
    samples = np.frombuffer(audio_data, dtype=np.int16)
    
    # Frequencies map
    freq_map = {
        400: '0', 560: '1', 720: '2', 880: '3',
        1040: '4', 1200: '5', 1360: '6', 1520: '7',
        1680: '8', 1840: '9', 2000: 'a', 2160: 'b',
        2320: 'c', 2480: 'd', 2640: 'e', 2800: 'f'
    }
    
    tone_length = int(0.25 * framerate)
    stride = int(0.29 * framerate)
    
    result = []
    for i in range(8):
        start = i * stride
        end = start + tone_length
        segment = samples[start:end]
        
        # apply FFT to find peak frequency
        fft_out = np.fft.fft(segment)
        freqs = np.fft.fftfreq(len(segment), 1.0/framerate)
        
        # only look at positive frequencies
        pos_mask = freqs > 0
        peak_idx = np.argmax(np.abs(fft_out[pos_mask]))
        peak_freq = freqs[pos_mask][peak_idx]
        
        # match to closest expected frequency
        closest_freq = min(freq_map.keys(), key=lambda f: abs(f - peak_freq))
        result.append(freq_map[closest_freq])
        
    return "".join(result)

# Part 3: Scene changes in forensics-frames.png
def solve_part3():
    img = Image.open('forensics-frames.png').convert('RGB')
    w, h = img.size
    # 6 across, 4 down
    frame_w = w // 6
    frame_h = h // 4
    
    frames = []
    for row in range(4):
        for col in range(6):
            left = col * frame_w
            upper = row * frame_h
            right = left + frame_w
            lower = upper + frame_h
            frame = img.crop((left, upper, right, lower))
            
            # calculate average color
            avg_color = np.array(frame).mean(axis=(0,1))
            frames.append(avg_color)
            
    changes = 0
    for i in range(len(frames)-1):
        # difference in average color
        diff = np.max(np.abs(frames[i] - frames[i+1]))
        if diff > 10: # Since noise is +/- 6, average won't shift more than 6, but base color will shift by much more
            changes += 1
            
    return changes

print(f"{solve_part1()}|{solve_part2()}|{solve_part3()}")
