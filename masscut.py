#!/usr/bin/env python

import hddm_s
import ROOT
import random

h0 = ROOT.TH1D("h0", "", 200, 0, 12)
h1 = ROOT.TH1D("h1", "", 200, 0, 12)
h1.GetXaxis().SetTitle("beam photon energy (GeV)")
h1.GetYaxis().SetTitle("Bethe Heitler cross section (ub)")
h1.Sumw2();

wsum0 = 0
wsum1 = 0
wsum2 = 0
duds = 0
for fin in open("samples"):
   for rec in hddm_s.istream(fin.rstrip()):
      for rea in rec.getReactions():
         moms = rec.getMomenta()
         wsum0 += 1
         h0.Fill(moms[0].E)
         if len(moms) == 5:
            invmass2 = ( (moms[2].E + moms[3].E)**2
                       - (moms[2].px + moms[3].px)**2
                       - (moms[2].py + moms[3].py)**2
                       - (moms[2].pz + moms[3].pz)**2 )
            if invmass2 >= 1:
               wsum1 += rea.weight
               wsum2 += rea.weight**2
               h1.Fill(moms[0].E, rea.weight)
               if rea.weight == 0:
                  duds += 1

h1.Divide(h0)
#print wsum1/wsum0, "+/-", (wsum2/wsum0 - (wsum1/wsum0)**2)**0.5 / wsum0**0.5
print duds, "duds"
