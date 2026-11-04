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


def music(dur, theme, loop=False):
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
    out *= env(n, 0.02, 0.06) if loop else env(n, 0.4, 1.2)  # boucle : pas de fondu, la fin rejoint le début
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
    if kind == 'ping':  # notification (message reçu)
        d = .35; tt = np.arange(int(d * SR)) / SR
        f = 1046.5 if rng.random() < .5 else 1174.7
        return (np.sin(2 * np.pi * f * tt) + .4 * np.sin(4 * np.pi * f * tt)) * np.exp(-tt * 14) * 0.10
    if kind == 'riser':  # montée de 2,5 s qui finit pile sur la révélation
        d = 2.5; m = int(d * SR); tt = np.arange(m) / SR; nz = rng.standard_normal(m)
        nz = np.convolve(nz, np.ones(8) / 8, 'same')
        f = 220 * 2 ** (tt / d * 2)
        tone_ = np.sin(2 * np.pi * np.cumsum(f) / SR) * .35
        return (nz * .5 + tone_) * (tt / d) ** 2 * 0.16
    if kind == 'impact':  # impact doux (pas de « boum boum »)
        d = .6; tt = np.arange(int(d * SR)) / SR
        body = np.sin(2 * np.pi * (70 + 60 * np.exp(-tt * 20)) * tt) * np.exp(-tt * 9) * .22
        nz = rng.standard_normal(len(tt)); nz = np.convolve(nz, np.ones(6) / 6, 'same') * np.exp(-tt * 25) * .10
        bell = np.sin(2 * np.pi * 1568 * tt) * np.exp(-tt * 6) * .05
        return body + nz + bell
    return np.zeros(1)


def main():
    events = json.load(open(sys.argv[1])); out = sys.argv[2]; dur = float(sys.argv[3]); theme = sys.argv[4]
    rng = np.random.default_rng(3)
    extra = sys.argv[5:]; loop = 'loop' in extra
    style = next((x.split('=', 1)[1] for x in extra if x.startswith('music=')), None)
    if style:  # musique accrocheuse (reels tendance) : music.py
        import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from music import track
        mix = track(style, dur, seed=int(dur * 10)) * 0.62
        if not loop: mix *= env(len(mix), 0.005, 0.35)
    else:
        mix = music(dur, theme, loop)
    # silences de musique : paires mute / unmute (le moment calme juste avant le plus fort)
    ms = [e['t'] for e in events if e['type'] == 'mute']; us = [e['t'] for e in events if e['type'] == 'unmute']
    for a in ms:
        b = min([u for u in us if u > a] or [dur]); i, j = int(a * SR), int(b * SR); k = int(.04 * SR)
        g = np.ones(len(mix)); g[i:j] = 0.06; g[i:i + k] = np.linspace(1, .06, len(g[i:i + k])); g[j:j + k] = np.linspace(.06, 1, len(g[j:j + k]))
        mix = mix * g
    last = {}
    for e in events:
        if e['type'] in ('mute', 'unmute'): continue
        k = e['type']; t0 = e['t']
        if k == 'word' and t0 - last.get(k, -9) < .12: continue
        if k in ('tick', 'ping') and t0 - last.get(k, -9) < .1: continue
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
