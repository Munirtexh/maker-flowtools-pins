"""Funk brésilien / phonk 100 % ORIGINAL (28 nov. 2026, Yaacoub veut une ambiance « funk tendance » pour la course). Aucun extrait ni mélodie d'un morceau existant.
130 BPM, rythme tamborzão (kick syncopé + caisse claire), cloche (cowbell) phonk, basse 808 qui glisse, drop à `drop` s (le 3e relèvement).
track(dur, drop=14.0, seed=1) -> mono -1..1."""
import numpy as np
from music import SR, Mix, kick, clap, hat, snare, hz, lp, adsr

def cowbell(m, d=.22):
    n = int(d * SR); t = np.arange(n) / SR; f = hz(m)
    s = np.sign(np.sin(2 * np.pi * f * t)) + np.sign(np.sin(2 * np.pi * f * 1.504 * t)); s = lp(s, 3)
    return s * np.exp(-t * 16) * .20

def b808(m, d, glide=0):
    n = int(d * SR); t = np.arange(n) / SR; f = hz(m) * (2 ** (glide * np.exp(-t * 9) / 12))
    return np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * 1.6) * adsr(n, .004, .12, .8, .06) * .55

def rim(rng):
    n = int(.06 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1700 * t) + .5 * rng.standard_normal(n) * 0.3) * np.exp(-t * 70) * .22

def riser(d):
    n = int(d * SR); t = np.arange(n) / SR; rng = np.random.default_rng(9)
    nz = rng.standard_normal(n); nz = nz - lp(nz, 3)
    return nz * (t / d) ** 2 * .22 + np.sin(2 * np.pi * np.cumsum(260 * 2 ** (t / d * 2.4)) / SR) * (t / d) ** 2 * .12

def track(dur, drop=14.0, seed=1):
    rng = np.random.default_rng(seed); bpm = 130; beat = 60 / bpm; s16 = beat / 4; bar = beat * 4
    roots = [41, 44, 48, 46]  # F2 Ab2 C3 Bb2 (fa mineur)
    HOOK = [(0, 77), (3, 80), (4, 77), (6, 75), (8, 72), (10, 75), (12, 77), (14, 80)]  # motif original de cloche
    mx, dr = Mix(dur + 2), Mix(dur + 2)
    for b in range(int(dur / bar) + 2):
        t0 = b * bar; root = roots[b % 4]; full = t0 >= drop - .01
        for st in range(16):
            tt = t0 + st * s16
            if full:
                if st in (0, 3, 6, 8, 11, 14): dr.add(tt, kick(1.0), 1.0)
                if st in (4, 12): dr.add(tt, clap(rng), 1.0)
                if st in (7, 15): dr.add(tt, rim(rng), 1.0)
            else:
                if st in (0, 8): dr.add(tt, kick(.7), .8)
                if st in (6, 14): dr.add(tt, rim(rng), .7)
            if st % 2 == 0: dr.add(tt, hat(rng), .6 if st % 4 else .9)
        for j, (st, m) in enumerate(HOOK):
            if full or b % 2 == 1: mx.add(t0 + st * s16, cowbell(m), 1.0 if full else .7)
        mx.add(t0, b808(root, bar * .42, 0), 1.0); mx.add(t0 + 6 * s16, b808(root + (12 if full else 0), s16 * 2.4, -5), .9)
        mx.add(t0 + 10 * s16, b808(root + 7, s16 * 3, 0), .85 if full else .6)
    mx.add(drop - 2.5, riser(2.5), 1.0); dr.add(drop, kick(1.2), 1.2)
    out = mx.buf + dr.buf; out = np.tanh(out * 1.3) / np.tanh(1.3); out = out[:int(dur * SR)]
    fade = np.ones(len(out)); k = int(.6 * SR); fade[-k:] = np.linspace(1, 0, k)
    return out * fade / max(1e-6, np.max(np.abs(out)))
