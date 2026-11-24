"""Musique de pub « Cyber / Black Friday » (24 nov. 2026, Yaacoub : « un vrai truc qui donne envie d'acheter »).
128 BPM, groove énergique : kick 4/4, claps, hats en croches, basse pompée, arpège brillant, montée + impact sur la révélation (12,6 s).
Générée à la main (numpy), 100 % originale. track(dur, variant) -> mono -1..1."""
import numpy as np
from music import SR, Mix, kick, clap, hat, hz, lp, adsr, snare

def saw(f, t, det=(0,)):
    return sum(((f * (1 + d) * t) % 1) * 2 - 1 for d in det) / len(det)

def arp(m, d, bright=1.0):
    n = int(d * SR); t = np.arange(n) / SR; f = hz(m)
    s = lp(saw(f, t, (-.004, .004)), 6 if bright < 1 else 3) + .3 * np.sin(2 * np.pi * f * 2 * t)
    return s * adsr(n, .002, .08, .35, .04) * .26

def sub(m, d):
    n = int(d * SR); t = np.arange(n) / SR; f = hz(m)
    return (np.sin(2 * np.pi * f * t) + .35 * np.sin(4 * np.pi * f * t)) * adsr(n, .004, .06, .8, .03) * .6

def chord(ms, d):
    n = int(d * SR); t = np.arange(n) / SR
    s = sum(lp(saw(hz(m), t, (-.006, .006)), 14) for m in ms) / len(ms)
    return s * adsr(n, .01, .1, .75, .08) * .28

def riser(d):
    n = int(d * SR); t = np.arange(n) / SR; rng = np.random.default_rng(5)
    nz = rng.standard_normal(n); nz = nz - lp(nz, 3)
    return (nz * (t / d) ** 2 * .22 + np.sin(2 * np.pi * np.cumsum(300 * 2 ** (t / d * 2.2)) / SR) * (t / d) ** 2 * .12)

def crash(rng, d=1.4):
    n = int(d * SR); t = np.arange(n) / SR
    nz = rng.standard_normal(n); nz = nz - lp(nz, 2)
    return nz * np.exp(-t * 3.2) * .28

def track(dur, variant=0, seed=1):
    rng = np.random.default_rng(seed)
    bpm = 128; beat = 60 / bpm; bar = beat * 4; e8 = beat / 2; e16 = beat / 4
    prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]] if variant == 0 else [[50, 53, 57], [58, 62, 65], [53, 57, 60], [48, 52, 55]]
    HOOK = [2, -1, 2, 1, -1, 2, 0, 1]
    mx = Mix(dur + 2); dr = Mix(dur + 2)
    drop = 12.6  # CTA : tout revient fort
    for b in range(int(dur / bar) + 2):
        t0 = b * bar; ch = prog[b % 4]; root = ch[0] - 24
        in_break = 11.0 <= t0 < drop  # petite coupure avant la révélation
        for k in range(4):
            tb = t0 + k * beat
            if not in_break or k == 0: dr.add(tb, kick(.95), 1.0)
            if k in (1, 3): dr.add(tb, clap(rng), 1.0)
            dr.add(tb + e8, hat(rng, True), .9)
            dr.add(tb, hat(rng), .55); dr.add(tb + e16, hat(rng), .3); dr.add(tb + e16 * 3, hat(rng), .3)
        # basse pompée (croches décalées)
        for j in range(8):
            if j % 2 == 1 or j in (0,): mx.add(t0 + j * e8, sub(root + ([0, 0, 12, 7][j % 4] if j else 0), e8 * .9), .9)
        # accords en « stab » syncopés
        for j in (0, 3, 6):
            mx.add(t0 + j * e8 + (e16 if j else 0), chord([m + 12 for m in ch], e8 * .8), 1.0)
        # arpège brillant (le « jingle » qui accroche)
        for j in range(16):
            m = ch[[0, 1, 2, 1, 2, 1, 0, 1][j % 8]] + 24 + (12 if j % 8 == 4 else 0)
            mx.add(t0 + j * e16, arp(m, e16 * 1.4), .7 if j % 2 else 1.0)
        # mélodie « hook »
        for j, d in enumerate(HOOK):
            if d >= 0: mx.add(t0 + j * e8, arp(ch[d] + 36, e8 * 1.5), .9)
    # montée vers la révélation + impact
    mx.add(drop - 2.4, riser(2.4), 1.0)
    dr.add(drop, crash(rng), 1.0); dr.add(drop, kick(1.2), 1.2)
    dr.add(0.0, crash(rng, .9), .8)
    # pompage doux
    t = np.arange(mx.n) / SR; ph = (t % beat) / beat
    mx.buf *= .5 + .5 * np.clip(ph * 3.0, 0, 1)
    # roulement de caisse claire avant le drop
    for j in range(16):
        tt = drop - 1.0 + j * (1.0 / 16)
        dr.add(tt, snare(rng, 200), .25 + .6 * j / 16)
    out = mx.buf + dr.buf
    out = np.tanh(out * 1.35) / np.tanh(1.35)
    out = out[:int(dur * SR)]
    fade = np.ones(len(out)); k = int(.5 * SR); fade[-k:] = np.linspace(1, 0, k)
    return out * fade / max(1e-6, np.max(np.abs(out)))
