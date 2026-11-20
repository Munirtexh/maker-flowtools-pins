"""Musique « vrais instruments » (20 nov. 2026, demande de Yaacoub : « change la musique, mets quelque chose de vraiment bien »).
Compose un morceau original (MIDI) par style, joué par la banque de sons FluidR3_GM (licence MIT, libre pour la vidéo)
via fluidsynth. Chaque style a ses instruments, son tempo, sa grille d'accords et son motif accrocheur (répété, varié).
Utilisation : from music2 import track ; track('pizz', 15, seed) -> numpy mono 44,1 kHz.
Styles : pizz (cordes pizzicato + glockenspiel, comédie « film d'animation »), uke (ukulélé/sifflet/claps), chip (8/16-bit),
synthwave (années 90), keys (lofi piano électrique), marimba (marimba + claquements de doigts), swing (cartoon jazz, trompette bouchée)."""
import os, subprocess, tempfile, wave
import numpy as np
import pretty_midi as pm

SF2 = '/usr/share/sounds/sf2/FluidR3_GM.sf2'
SR = 44100
# accords (notes MIDI) ; 1 accord par mesure
PROGS = {
    'pizz': [[53, 57, 60], [50, 53, 57], [46, 50, 53], [48, 52, 55]],          # F Dm Bb C
    'uke': [[48, 52, 55], [55, 59, 62], [57, 60, 64], [53, 57, 60]],           # C G Am F
    'chip': [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]],          # Am F C G
    'synthwave': [[50, 53, 57], [46, 50, 53], [48, 52, 55], [45, 48, 52]],     # Dm Bb C Am
    'keys': [[50, 53, 57, 60], [55, 59, 62, 65], [48, 52, 55, 59], [45, 48, 52, 55]],  # Dm9 G7 Cmaj7 Am7
    'marimba': [[52, 55, 59], [48, 52, 55], [55, 59, 62], [50, 54, 57]],       # Em C G D
    'swing': [[50, 53, 57, 60], [55, 59, 62, 65], [48, 52, 55, 59], [57, 61, 64, 67]],  # ii V I VI
}
BPM = {'pizz': 116, 'uke': 104, 'chip': 140, 'synthwave': 112, 'keys': 84, 'marimba': 120, 'swing': 132}
# motif (en croches : None = silence, entier = degré dans l'accord, +7 = octave)
HOOK = {
    'pizz': [0, None, 2, 1, 0, None, 7, None, 2, 1, 2, None, 4, None, None, None],
    'uke': [2, None, 2, 1, 0, None, 1, 2, None, 4, None, 2, 1, None, None, None],
    'chip': [0, 2, 7, 2, 4, 2, 7, 9, 0, 2, 7, 2, 9, 7, 4, 2],
    'synthwave': [7, None, None, 4, None, 2, None, None, 7, None, 9, None, 4, None, None, None],
    'keys': [4, None, 2, None, None, 1, None, None, 2, None, 0, None, None, None, None, None],
    'marimba': [0, 2, 4, None, 2, 4, 7, None, 4, 2, 0, None, 1, None, 2, None],
    'swing': [0, None, 2, 3, 4, None, 2, None, 7, None, 4, 2, 3, None, None, None],
}
INST = {  # mélodie, double, accords, basse (programmes GM)
    'pizz': (45, 9, 48, 45), 'uke': (78, 24, 24, 32), 'chip': (80, 80, 81, 38), 'synthwave': (81, 88, 89, 38),
    'keys': (4, None, 4, 33), 'marimba': (12, 11, 46, 33), 'swing': (59, None, 0, 32),
}


def deg(ch, d):
    o, k = divmod(d, 7) if d >= 7 else (0, d)
    tones = ch + [c + 12 for c in ch]
    return tones[min(k, len(tones) - 1)] + 12 + 12 * o


def compose(style, dur, seed):
    rng = np.random.default_rng(seed)
    bpm = BPM[style]; beat = 60 / bpm; bar = 4 * beat; e8 = beat / 2
    prog = PROGS[style]; hook = HOOK[style]; mi, di, ci, bi = INST[style]
    sw = 1.16 if style in ('swing', 'keys') else 1.0
    mid = pm.PrettyMIDI(initial_tempo=bpm)
    mel = pm.Instrument(mi); dbl = pm.Instrument(di) if di is not None else None
    chd = pm.Instrument(ci); bas = pm.Instrument(bi); drm = pm.Instrument(0, is_drum=True)
    nb = int(dur / bar) + 2
    for b in range(nb):
        t0 = b * bar; ch = prog[b % len(prog)]; half = (b // 2) % 2
        # mélodie : motif de 2 mesures, la 2e moitié varie légèrement (question / réponse)
        seg = hook[(b % 2) * 8:(b % 2) * 8 + 8]
        for j, d in enumerate(seg):
            if d is None: continue
            if half and j == 6 and rng.random() < .7: d = d + 1
            tt = t0 + j * e8 + (e8 * (sw - 1) if j % 2 else 0)
            n = deg(ch, d); ln_ = e8 * (0.55 if style in ('pizz', 'marimba', 'chip') else 1.6)
            vel = 92 if j % 2 == 0 else 78
            mel.notes.append(pm.Note(vel, n, tt, tt + ln_))
            if dbl is not None and (j % 2 == 0 or style == 'chip'): dbl.notes.append(pm.Note(70, n + (12 if style in ('pizz', 'marimba') else 0), tt, tt + ln_))
        # accords
        if style in ('uke',):
            for k in range(8):
                tt = t0 + k * e8; v = 74 if k % 2 == 0 else 58
                if k in (0, 2, 3, 5, 6, 7):
                    for i, c in enumerate(ch): chd.notes.append(pm.Note(v, c + 12, tt + i * .012, tt + e8 * .9))
        elif style in ('chip',):
            for k in range(16):
                tt = t0 + k * e8 / 2; c = ch[k % 3] + 12
                chd.notes.append(pm.Note(55, c, tt, tt + e8 / 2 * .8))
        elif style in ('pizz', 'marimba'):
            for k in range(4):
                tt = t0 + k * beat + (e8 if k % 2 else 0) * 0
                for c in ch: chd.notes.append(pm.Note(46 if style == 'pizz' else 58, c, tt, tt + beat * (1.9 if style == 'pizz' else .4)))
        else:  # nappes / accords tenus
            for c in ch: chd.notes.append(pm.Note(58 if style != 'keys' else 64, c, t0 + (e8 * 0.15 if style == 'keys' else 0), t0 + bar * .98))
        # basse
        root = ch[0] - 12
        if style == 'swing':
            walk = [root, root + 4, root + 7, root + 9]
            for k, n in enumerate(walk): bas.notes.append(pm.Note(84, n, t0 + k * beat, t0 + k * beat + beat * .9))
        elif style in ('synthwave', 'chip'):
            for k in range(8): bas.notes.append(pm.Note(80, root + (12 if k % 2 else 0), t0 + k * e8, t0 + k * e8 + e8 * .8))
        else:
            pat = [(0, root), (beat * 1.5, root + 7), (beat * 2, root), (beat * 3, root + (5 if style == 'uke' else 7))]
            for a, n in pat: bas.notes.append(pm.Note(80, n, t0 + a, t0 + a + beat * .8))
        # batterie (douce : pas de « boum boum »)
        for k in range(4):
            tb = t0 + k * beat
            if style == 'pizz':
                if k in (0, 2): drm.notes.append(pm.Note(52, 36, tb, tb + .1))
                drm.notes.append(pm.Note(38, 54, tb + e8, tb + e8 + .05))
                if k in (1, 3): drm.notes.append(pm.Note(44, 75, tb, tb + .05))  # claves
            elif style == 'uke':
                if k in (1, 3): drm.notes.append(pm.Note(62, 39, tb, tb + .1))  # claps
                drm.notes.append(pm.Note(34, 70, tb, tb + .05)); drm.notes.append(pm.Note(28, 70, tb + e8, tb + e8 + .05))  # maracas
                if k == 0: drm.notes.append(pm.Note(54, 36, tb, tb + .1))
            elif style == 'chip':
                drm.notes.append(pm.Note(60 if k in (0, 2) else 0, 36, tb, tb + .1))
                if k in (1, 3): drm.notes.append(pm.Note(58, 38, tb, tb + .1))
                for j in range(2): drm.notes.append(pm.Note(32, 42, tb + j * e8, tb + j * e8 + .05))
            elif style == 'synthwave':
                if k in (0, 2): drm.notes.append(pm.Note(64, 36, tb, tb + .1))
                if k in (1, 3): drm.notes.append(pm.Note(60, 40, tb, tb + .1))
                for j in range(2): drm.notes.append(pm.Note(30, 42, tb + j * e8, tb + j * e8 + .05))
            elif style == 'keys':
                if k in (0,) or (k == 2 and b % 2): drm.notes.append(pm.Note(50, 36, tb, tb + .1))
                if k in (1, 3): drm.notes.append(pm.Note(40, 38, tb, tb + .1))
                drm.notes.append(pm.Note(26, 42, tb, tb + .05)); drm.notes.append(pm.Note(20, 42, tb + e8 * sw, tb + e8 * sw + .05))
            elif style == 'marimba':
                if k in (1, 3): drm.notes.append(pm.Note(58, 39, tb, tb + .1))  # claquements
                drm.notes.append(pm.Note(30, 82, tb, tb + .05)); drm.notes.append(pm.Note(22, 82, tb + e8, tb + e8 + .05))
                if k == 0: drm.notes.append(pm.Note(46, 36, tb, tb + .1))
            elif style == 'swing':
                drm.notes.append(pm.Note(36, 51, tb, tb + .1)); drm.notes.append(pm.Note(26, 51, tb + e8 * sw, tb + e8 * sw + .05))
                if k in (1, 3): drm.notes.append(pm.Note(44, 44, tb, tb + .05))
    if style in ('pizz', 'marimba'):  # petites étincelles de célesta en fin de mesure paire
        cel = pm.Instrument(8)
        for b in range(0, nb, 2):
            ch = prog[b % len(prog)]
            for k, c in enumerate(ch): cel.notes.append(pm.Note(50, c + 36, b * bar + 3.5 * beat + k * .07, b * bar + 3.5 * beat + k * .07 + .4))
        mid.instruments.append(cel)
    for ins in (mel, dbl, chd, bas, drm):
        if ins is not None: mid.instruments.append(ins)
    return mid


def track(style, dur, seed=1):
    style = style if style in PROGS else 'pizz'
    mid = compose(style, dur, seed)
    with tempfile.TemporaryDirectory() as d:
        mp, wp = os.path.join(d, 'm.mid'), os.path.join(d, 'm.wav')
        mid.write(mp)
        subprocess.run(['fluidsynth', '-ni', '-g', '0.7', '-r', str(SR), '-F', wp, SF2, mp], check=True, capture_output=True)
        w = wave.open(wp); ch = w.getnchannels(); x = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2').astype(np.float32) / 32768
    if ch == 2: x = x.reshape(-1, 2).mean(1)
    n = int(dur * SR); x = x[:n] if len(x) >= n else np.pad(x, (0, n - len(x)))
    if style == 'keys':  # léger souffle de vinyle
        rng = np.random.default_rng(seed); x = x + rng.normal(0, .004, len(x)).astype(np.float32)
    return x / max(1e-6, np.max(np.abs(x))) * .9


if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/m'
    for s in PROGS:
        y = track(s, 15, 3); pcm = (np.stack([y, y], 1) * 32767).astype('<i2')
        with wave.open(f'{out}_{s}.wav', 'wb') as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
        print(s)
