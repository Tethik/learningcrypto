classical-crypto
================

Implementation of Classical crypto ciphers described in the book Cryptography: Theory and Practice by Douglas R. Stinson

Ciphers implemented:
* Shift cipher
  * Each letter in the message is shifted by K
* Substitution cipher
  * Each letter is substituted by another specific letter
* Affine cipher
  * The key K is composed of two values A and B. 
  * Encryption: e(m) = A*m + B
  * Decryption: d(m) = Ainv*(m-B)
* Vigenère cipher
  * The key is a word. E.g. "Secret"
  * Each letter is shifted by k where k is the current letter in the keyword.
* Hill cipher
  * The key K is an invertible m*m matrix where m is the block size.
  * Encryption: e(m) = m*K
  * Decryption: e(m) = m*Kinv
* Permutation cipher
  * Letters are scrambled based on their position in the message.
* Autokey cipher
  * Each letter in the message is shifted by Z where Z is the previous letter or the key.
  * Basically Shift Cipher with recursion
