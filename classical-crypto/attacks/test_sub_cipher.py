#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import substitution, alphabet

plaintext = """
The 2014 Winter Olympics, officially the XXII Olympic Winter Games (French: Les XXIIes Jeux olympiques d'hiver [3][4]), or the 22nd Winter Olympics, is a major international multi-sport event being held in Sochi, Russia.
Scheduled for 7–23 February 2014, opening rounds in figure skating, skiing, and snowboard competitions were held on the eve of the Opening Ceremony, 6 February 2014. Both the Olympics and 2014 Winter Paralympics are being organized by the Sochi Organizing Committee (SOC). Sochi was selected as the host city in July 2007, during the 119th IOC Session held in Guatemala City. It is the first Olympics in Russia since the breakup of the USSR in 1991. The USSR was the host nation for the 1980 Summer Olympics in Moscow.
A total of 98 events in 15 winter sport disciplines are being held during the Games. A number of new competitions—a total of 12 accounting for gender—are being held during the Games, including biathlon mixed relay, women's ski jumping, mixed-team figure skating, mixed-team luge, half-pipe skiing, ski and snowboard slopestyle, and snowboard parallel slalom. The events are being held around two clusters of new venues; an Olympic Park constructed in Sochi's Imeretinsky Valley on the coast of the Black Sea, with Fisht Olympic Stadium and the Games' indoor venues located within walking distance, and snow events in the resort settlement of Krasnaya Polyana.
In preparation, organizers focused on modernizing the telecommunications, electric power, and transportation infrastructures of the region. While originally budgeted at US$12 billion, various factors caused the budget to expand to over US$51 billion, surpassing the estimated $44 billion cost of the 2008 Summer Olympics in Beijing as the most expensive Olympics in history.
The lead-up to the 2014 Games was marked by major controversies, including allegations of corruption leading to the aforementioned cost overruns, concerns for the safety and human rights of lesbian, gay, bisexual and transgender (LGBT) athletes and supporters during the Games due to the country's recent anti-LGBT policies, which led to ongoing Olympic-focussed protests of the laws and its effects, protests by ethnic Circassian activists over the site of Sochi (the site of what they consider to be a genocide) and various security concerns over threats by jihadist groups tied to the insurgency in the North Caucasus.
"""

plaintext = plaintext.replace('\n','').upper()
alphabet = alphabet.Alphabet("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ ")
plaintext = alphabet.filter(plaintext)
key = substitution.keygen(alphabet)
ciphertext = substitution.encrypt(key, plaintext, alphabet)
print ciphertext
