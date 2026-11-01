"""Soft music bed + light pop/whoosh sound effects for Maker FlowTools reels.
No kick drum, no "boum boum": warm pads, gentle plucks, soft pops.
Usage: python3 audio.py events.json out.wav duration theme
"""
import json, sys, wave
import numpy as np

SR = 44100
KEYS = {  # chord progressions (MIDI notes) per theme, all mellow
    'landlord': [[57, 60, 64, 67], [53, 57, 60, 64], [48, 52, 55, 59], [55, 59, 62, 66]],
    'treasurer': [[50, 53, 57, 60], [55, 58, 62, 65], [48, 52, 55, 58], [53, 57, 60, 64]],
    'seat': [[53, 57, 60, 64], [50, 53, 57, 60], [46, 50, 53, 57], [48, 52, 55, 60]],
    'habit': [[52, 55, 59, 62], [48, 52, 55, 59], [53, 57, 60, 64], [55, 59, 62, 65]],
    'artisan': [[55, 59, 62, 66], [52, 55, 59, 62], [48, 52, 55, 59], [50, 54, 57, 60]],
}


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def env(n, a, r):
    e = np.ones(n)
    ai = min(n, int(a * SR)); ri = min(n, int(r * SR))
    if ai: e[:ai] = np.linspace(0, 1, ai)
    if ri: e[-ri:] *= np.linspace(1, 0, ri)
    return e


def music(dur, theme):
    n = int(dur * SR); t = np.arange(n) / SR
    out = np.zeros(n)
    prog = KEYS.get(theme, KEYS['landlord'])
    bar = 2.4
    for k in range(int(dur / bar) + 1):
        ch = prog[k % len(prog)]
        s = int(k * bar * SR); e = min(n, int((k + 1) * bar * SR) + int(.6 * SR))
        if s >= n: break
        tt = t[s:e] - t[s]
        seg = np.zeros(e - s)
        for m in ch:  # pad: detuned soft sines
            for d in (-0.08, 0.08):
                seg += np.sin(2 * np.pi * hz(m + d) * tt) * 0.045
        seg *= env(e - s, .5, .7)
        seg += np.sin(2 * np.pi * hz(ch[0] - 12) * tt) * 0.07 * env(e - s, .15, .6)
        out[s:e] += seg
        # plucks (arpeggio) 8th notes
        step = bar / 8
        for j in range(8):
            m = ch[[0, 2, 1, 3, 2, 1, 3, 2][j]] + 12
            ps = s + int(j * step * SR); pe = min(n, ps + int(.7 * SR))
            if ps >= n: break
            pt = t[ps:pe] - t[ps]
            out[ps:pe] += (np.sin(2 * np.pi * hz(m) * pt) + .3 * np.sin(4 * np.pi * hz(m) * pt)) * np.exp(-pt * 6) * 0.05
        # soft shaker (very light noise ticks, off-beat)
        for j in range(4):
            ps = s + int((j + .5) * bar / 4 * SR); pe = min(n, ps + int(.05 * SR))
            if ps >= n: break
            nz = np.random.default_rng(k * 10 + j).standard_normal(pe - ps)
            nz = np.diff(np.concatenate([[0], nz]))  # highpass-ish
            out[ps:pe] += nz * np.exp(-np.arange(pe - ps) / SR * 90) * 0.012
    out *= env(n, 0.4, 1.2)
    return out


def sfx(kind, rng):
    if kind in ('pop', 'word'):
        d = .09; tt = np.arange(int(d * SR)) / SR
        f = (700 if kind == 'pop' else 520) * (1 + 1.2 * tt / d) * (1 + rng.uniform(-.06, .06))
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 45) * (0.22 if kind == 'pop' else 0.13)
    if kind == 'tick':
        d = .05; tt = np.arange(int(d * SR)) / SR
        return np.sin(2 * np.pi * 1500 * tt) * np.exp(-tt * 90) * 0.10
    if kind == 'swish':
        d = .22; m = int(d * SR); nz = rng.standard_normal(m)
        nz = np.convolve(nz, np.ones(12) / 12, 'same')
        return nz * np.sin(np.linspace(0, np.pi, m)) * 0.10
    if kind == 'whoosh':
        d = .55; m = int(d * SR); nz = rng.standard_normal(m)
        nz = np.convolve(nz, np.ones(30) / 30, 'same')
        return nz * np.sin(np.linspace(0, np.pi, m)) ** 2 * 0.35
    if kind in ('ding', 'alert'):
        d = 1.0; tt = np.arange(int(d * SR)) / SR
        notes = (1318.5, 1975.5) if kind == 'ding' else (880, 830.6)
        s = sum(np.sin(2 * np.pi * f * tt) * np.exp(-tt * (4 + i * 2)) for i, f in enumerate(notes))
        return s * 0.11
    if kind == 'stamp':
        d = .18; tt = np.arange(int(d * SR)) / SR
        nz = rng.standard_normal(len(tt)) * np.exp(-tt * 60) * 0.12
        return nz + np.sin(2 * np.pi * 180 * tt) * np.exp(-tt * 30) * 0.18
    return np.zeros(1)


def main():
    events = json.load(open(sys.argv[1])); out = sys.argv[2]; dur = float(sys.argv[3]); theme = sys.argv[4]
    rng = np.random.default_rng(3)
    mix = music(dur, theme)
    last = {}
    for e in events:
        k = e['type']; t0 = e['t']
        if k == 'word' and t0 - last.get(k, -9) < .12: continue
        if k == 'tick' and t0 - last.get(k, -9) < .1: continue
        last[k] = t0
        s = sfx(k, rng); i = int(t0 * SR)
        if i >= len(mix): continue
        j = min(len(mix), i + len(s)); mix[i:j] += s[:j - i]
    mix = mix / max(1e-6, np.max(np.abs(mix))) * 0.85
    st = np.stack([mix, mix], 1)
    pcm = (st * 32767).astype('<i2')
    with wave.open(out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


if __name__ == '__main__':
    main()
