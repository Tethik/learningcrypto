#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import shift
from .. import alphabet

plaintext = """
Perseus, named after the Greek mythological hero Perseus, is a constellation in the northern sky. It was one of 48 listed by the 2nd-century astronomer Ptolemy and among the 88 modern constellations defined by the International Astronomical Union (IAU). It is located in the northern celestial hemisphere near several other constellations named after legends surrounding Perseus, including Andromeda to the west and Cassiopeia to the north. Perseus is also bordered by Aries and Taurus to the south, Auriga to the east, Camelopardalis to the north, and Triangulum to the west. The galactic plane of the Milky Way passes through Perseus but is mostly obscured by molecular clouds. The constellation's brightest star is the yellow-white supergiant Alpha Persei (also called Mirfak), which shines at magnitude 1.79. It and many of the surrounding stars are members of an open cluster known as the Alpha Persei Cluster. The best-known star, however, is Algol (Beta Persei), linked with ominous legends because of its variability, which is noticeable to the naked eye. Rather than being an intrinsically variable star, it is an eclipsing binary. Other notable star systems in Perseus include X Persei, a binary system containing a neutron star, and GK Persei, a nova that peaked at magnitude 0.2 in 1901. The Double Cluster, comprising two open clusters quite near each other in the sky, was known to the ancient Chinese. The constellation gives its name to the Perseus Cluster (Abell 426), a massive galaxy cluster located 250 million light-years from Earth. It hosts the radiant of the annual Perseids meteor shower—one of the most prominent meteor showers in the sky.
"""
plaintext = plaintext.replace('\n', '')
alphabetstr = "ABCDEFGHIJKLMNOPQRSTUVXYZ "
plaintext = "".join([p.upper() for p in plaintext if p.upper() in alphabetstr])
alphabet = alphabet.Alphabet(alphabetstr)

k = shift.keygen(alphabet)
ciphertext = shift.encrypt(k, plaintext, alphabet)
print ciphertext
#~ ciphertext = ciphertext.replace('\n', '')
