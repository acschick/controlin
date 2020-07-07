#!/usr/bin/env python

import hddm_s
import ROOT

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
         wsum0 += 1
         wsum1 += rea.weight
         wsum2 += rea.weight**2
         moms = rec.getMomenta()
         h0.Fill(moms[0].E)
         h1.Fill(moms[0].E, rea.weight)
         if rea.weight == 0:
            duds += 1

h1.Divide(h0)
print wsum1/wsum0, "+/-", (wsum2/wsum0 - (wsum1/wsum0)**2)**0.5 / wsum0**0.5
print duds, "duds"
