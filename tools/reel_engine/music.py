"""Musiques accrocheuses générées (libres de droits, 100 % originales) pour les reels tendance.
Demande de Yaacoub (4 nov. 2026) : musiques variées et accrocheuses « comme les influenceurs et les pubs »,
mais pas agressives. Styles : pop, lofi, tropical, funk, future (house douce), chacun avec son groove.
track(style, dur, seed) -> np.array mono 44,1 kHz, entre -1 et 1.
"""
import numpy as np

SR = 44100
STYLES = ['pop', 'lofi', 'tropical', 'funk', 'future']


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def adsr(n, a=.005, d=.1, s=.6, r=.1):
    e = np.full(n, s, float)
    ai, di, ri = int(a * SR), int(d * SR), int(r * SR)
    ai = min(ai, n); e[:ai] = np.linspace(0, 1, ai)
    dj = min(n, ai + di); e[ai:dj] = np.linspace(1, s, dj - ai)
    if ri and n > ri: e[-ri:] *= np.linspace(1, 0, ri)
    return e


def lp(x, k):  # filtre passe-bas simple (moyenne glissante)
    if k <= 1: return x
    return np.convolve(x, np.ones(k) / k, 'same')


class Mix:
    def __init__(self, dur):
        self.n = int(dur * SR); self.buf = np.zeros(self.n)

    def add(self, t, sig, g=1.0):
        i = int(t * SR)
        if i >= self.n or i < 0: return
        j = min(self.n, i + len(sig)); self.buf[i:j] += sig[:j - i] * g


def kick(soft=1.0):
    d = .32; t = np.arange(int(d * SR)) / SR
    f = 48 + 90 * np.exp(-t * 32)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 11) * .9 * soft


def snare(rng, tone=190):
    d = .2; t = np.arange(int(d * SR)) / SR
    nz = rng.standard_normal(len(t)); nz = nz - lp(nz, 6)
    return (nz * np.exp(-t * 22) * .45 + np.sin(2 * np.pi * tone * t) * np.exp(-t * 30) * .35)


def clap(rng):
    d = .22; t = np.arange(int(d * SR)) / SR
    nz = rng.standard_normal(len(t)); nz = nz - lp(nz, 4)
    e = np.exp(-t * 26)
    for o in (.0, .011, .022):  # triple attaque
        k = int(o * SR); e[k:k + 60] += .8
    return nz * e * .32


def hat(rng, open_=False):
    d = .18 if open_ else .045; t = np.arange(int(d * SR)) / SR
    nz = rng.standard_normal(len(t)); nz = nz - lp(nz, 2)
    return nz * np.exp(-t * (16 if open_ else 95)) * .16


def shaker(rng):
    d = .07; t = np.arange(int(d * SR)) / SR
    nz = rng.standard_normal(len(t)); nz = nz - lp(nz, 3)
    return nz * np.sin(np.linspace(0, np.pi, len(t))) * .09


def tone(m, d, kind='pluck', bright=1.0):
    n = int(d * SR); t = np.arange(n) / SR; f = hz(m)
    if kind == 'pluck':
        s = np.sin(2 * np.pi * f * t) + .45 * np.sin(4 * np.pi * f * t) * bright + .2 * np.sin(6 * np.pi * f * t) * bright
        return s * np.exp(-t * 7) * .32
    if kind == 'marimba':
        s = np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 30)
        return s * np.exp(-t * 9) * .4
    if kind == 'bass':
        s = np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t)
        return s * adsr(n, .006, .12, .7, .05) * .55
    if kind == 'slap':
        s = np.sin(2 * np.pi * f * t) + .6 * np.sin(4 * np.pi * f * t) * np.exp(-t * 20) + .25 * np.sin(6 * np.pi * f * t) * np.exp(-t * 30)
        return s * adsr(n, .003, .08, .5, .04) * .55
    if kind == 'keys':  # rhodes doux
        s = np.sin(2 * np.pi * f * t) * (1 + .25 * np.sin(2 * np.pi * 5 * t)) + .15 * np.sin(2 * np.pi * f * 2.001 * t)
        return s * adsr(n, .01, .4, .45, .25) * .16
    if kind == 'pad':  # « supersaw » adouci
        s = sum(lp(((f * (1 + dt) * t) % 1) * 2 - 1, 18) for dt in (-.006, 0, .006))
        return s * adsr(n, .06, .2, .7, .3) * .07
    if kind == 'lead':
        s = np.sin(2 * np.pi * f * t + .8 * np.sin(2 * np.pi * f * 2 * t) * np.exp(-t * 4))
        vib = 1  # pas de vibrato pour rester propre
        return s * adsr(n, .01, .15, .55, .08) * .2 * vib
    if kind == 'stab':
        s = lp(((f * t) % 1) * 2 - 1, 10) + lp(((f * 1.004 * t) % 1) * 2 - 1, 10)
        return s * adsr(n, .004, .09, .25, .05) * .09
    return np.zeros(n)


# progressions (accords en MIDI) et motifs de mélodie (degrés dans l'accord, -1 = silence)
PROG = {
    'pop': [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 67]],
    'lofi': [[57, 60, 64, 67], [50, 53, 57, 60], [55, 59, 62, 65], [52, 55, 59, 62]],
    'tropical': [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]],
    'funk': [[52, 55, 59, 62], [57, 61, 64, 67], [52, 55, 59, 62], [57, 61, 64, 67]],
    'future': [[53, 57, 60, 64], [55, 59, 62, 65], [57, 60, 64, 67], [52, 55, 59, 64]],
}
BPM = {'pop': 118, 'lofi': 84, 'tropical': 104, 'funk': 110, 'future': 124}
HOOK = {  # mélodie accrocheuse sur 8 croches (index dans l'accord + octave), répétée
    'pop': [3, -1, 2, 3, -1, 1, 2, -1], 'lofi': [2, -1, -1, 1, -1, 3, -1, -1], 'tropical': [0, 2, 1, 2, 0, 2, 1, 2],
    'funk': [0, -1, 0, 2, -1, 3, -1, 2], 'future': [3, -1, 3, 2, -1, 2, 1, -1],
}


def track(style, dur, seed=1):
    rng = np.random.default_rng(seed)
    st = style if style in PROG else 'pop'
    bpm = BPM[st]; beat = 60 / bpm; bar = beat * 4; e8 = beat / 2; e16 = beat / 4
    prog = PROG[st]; mx = Mix(dur + 1); drums = Mix(dur + 1)
    nb = int(dur / bar) + 1
    for b in range(nb):
        t0 = b * bar; ch = prog[b % len(prog)]
        intro = b == 0  # 1re mesure : déjà du groove (hook immédiat), batterie un peu plus légère
        # --- batterie ---
        for k in range(4):
            tb = t0 + k * beat
            if st in ('pop', 'future'):
                drums.add(tb, kick(.75 if intro else .85))
                if k in (1, 3): drums.add(tb, clap(rng), .9)
                drums.add(tb + e8, hat(rng, open_=(st == 'future')), 1.0)
                drums.add(tb, hat(rng), .5)
            elif st == 'lofi':
                sw = e8 * 1.18  # swing
                if k in (0, 2) or (k == 3 and b % 2): drums.add(tb + (e8 if k == 3 else 0), kick(.75))
                if k in (1, 3): drums.add(tb, snare(rng, 170), .65)
                drums.add(tb, hat(rng), .55); drums.add(tb + sw, hat(rng), .4)
            elif st == 'tropical':
                if k in (0, 2): drums.add(tb, kick(.7))
                drums.add(tb + e16 * 3, snare(rng, 230) * .5, .55)  # rythme « dembow » léger
                if k in (1, 3): drums.add(tb, clap(rng), .55)
                for j in range(4): drums.add(tb + j * e16, shaker(rng), 1.0 if j % 2 else .6)
            elif st == 'funk':
                if k == 0 or k == 2 or (k == 1 and b % 2): drums.add(tb + (e8 if k == 1 else 0), kick(.8))
                if k in (1, 3): drums.add(tb, snare(rng, 200), .7)
                for j in range(4): drums.add(tb + j * e16, hat(rng), .65 if j % 2 else .4)
        # --- basse ---
        root = ch[0] - 24
        if st == 'funk':
            pat = [0, -1, 0, 12, -1, 7, 10, 12, 0, -1, 0, -1, 12, -1, 7, -1]
            for j, p in enumerate(pat):
                if p >= 0: mx.add(t0 + j * e16, tone(root + p, e16 * .9, 'slap'))
        elif st == 'lofi':
            for k, p in enumerate([0, -1, 7, 5]):
                if p >= 0: mx.add(t0 + k * beat, tone(root + p, beat * .95, 'bass'), .9)
        else:
            for j in range(8):
                p = [0, 0, 12, 0, 7, 0, 12, 10][j] if st in ('pop', 'future') else [0, -1, 0, 7, -1, 7, 5, -1][j]
                if p >= 0: mx.add(t0 + j * e8, tone(root + p, e8 * .85, 'bass'), .85)
        # --- accords ---
        if st == 'lofi':
            for m in ch: mx.add(t0, tone(m, bar * 1.05, 'keys'))
        elif st == 'future':
            for m in ch: mx.add(t0, tone(m, bar, 'pad'))
            for j in (1, 3, 5, 7):
                for m in ch: mx.add(t0 + j * e8, tone(m + 12, e8 * .7, 'stab'), .8)
        elif st == 'funk':
            for j in (1, 3, 6):
                for m in ch: mx.add(t0 + j * e8, tone(m + 12, e16 * 1.2, 'stab'), 1.2)
        elif st == 'tropical':
            for m in ch: mx.add(t0, tone(m, bar, 'pad'), .7)
        else:  # pop
            for m in ch: mx.add(t0, tone(m, bar, 'pad'), .9)
            for j in range(0, 8, 2):
                for m in ch: mx.add(t0 + j * e8 + e8, tone(m, e8 * .6, 'stab'), .7)
        # --- mélodie accroche ---
        kind = {'tropical': 'marimba', 'lofi': 'pluck', 'pop': 'pluck', 'funk': 'lead', 'future': 'pluck'}[st]
        for j, d in enumerate(HOOK[st]):
            if d < 0: continue
            m = ch[d % len(ch)] + 12 + (12 if st == 'tropical' else 0)
            if b % 4 == 3 and j >= 6: m += 2  # petite variation de fin de phrase
            mx.add(t0 + j * e8, tone(m, e8 * 1.6, kind, bright=.7 if st == 'lofi' else 1.0), .9)
    # pompage doux (effet « sidechain ») sur la musique, pas sur la batterie
    if st in ('pop', 'future', 'tropical'):
        t = np.arange(mx.n) / SR; ph = (t % beat) / beat
        mx.buf *= .55 + .45 * np.clip(ph * 3.5, 0, 1)
    if st == 'lofi':  # craquement vinyle léger
        cr = (rng.random(mx.n) < .0007) * rng.standard_normal(mx.n) * .08
        mx.buf += lp(cr, 3) + lp(rng.standard_normal(mx.n), 40) * .004
        mx.buf = lp(mx.buf, 3)  # plus « feutré »
    out = mx.buf + drums.buf * (.8 if st == 'lofi' else 1.0)
    out = np.tanh(out * 1.3) / np.tanh(1.3)  # léger compresseur
    out = out[:int(dur * SR)]
    return out / max(1e-6, np.max(np.abs(out)))
