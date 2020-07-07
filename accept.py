#!/usr/bin/env python

import hddm_s
import ROOT
import random

h0 = ROOT.TH1D("h0","",100,2,12)
h1 = ROOT.TH1D("h1","",100,2,12)
h2 = ROOT.TH1D("h2","",100,2,12)

for fin in open("samples"):
#for fin in open("AndrewBHgen.hddm"):
   for rec in hddm_s.istream(fin.rstrip()):
      for rea in rec.getReactions():
         E = rec.getMomenta()[0].E
         h0.Fill(E)
         h1.Fill(E, rea.weight)
         iE = h2.FindBin(E)
         if rea.weight > h2.GetBinContent(iE):
            h2.SetBinContent(iE, rea.weight)

fout = hddm_s.ostream("BHgen_filtered.hddm")
for fin in open("samples"):
   for rec in hddm_s.istream(fin.rstrip()):
      for rea in rec.getReactions():
         E = rec.getMomenta()[0].E
         iE = h2.FindBin(E)
         wmax = h2.GetBinContent(iE)
         if rea.weight > random.random() * wmax:
            rea.weight = h1.GetBinContent(iE) / h0.GetBinContent(iE)
            fout.write(rec)
