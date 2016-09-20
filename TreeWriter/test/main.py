#!/usr/bin/env python2

import ROOT
ROOT.gROOT.SetBatch()
ROOT.PyConfig.IgnoreCommandLineOptions = True

def randomName():
    """
    Generate a random string. This function is useful to give ROOT objects
    different names to avoid overwriting.
    """
    from random import randint
    from sys import maxint
    return "%x"%(randint(0, maxint))

def createHistoFromTree(tree, variable, weight="", nBins=20, firstBin=0, lastBin=20):
    """
    tree: tree to create histo from
    variable: variable to plot (must be a branch of the tree)
    weight: weights to apply (e.g. "var1*(var2 > 15)" will use weights from var1 and cut on var2 > 15
    nBins, firstBin, lastBin: number of bins, first bin and last bin (same as in TH1F constructor)
    nBins: if nBins is a list, and to a int, a user binned plot will be generated
    returns: histogram
    """
    name = randomName()
    result = ROOT.TH1F(name, variable, nBins, firstBin, lastBin)
    result.Sumw2()
    tree.Draw("%s>>%s"%(variable, name), weight, "goff")
    return result


def readTree(filename, treename="TreeWriter/eventTree"):
    """
    filename: name of file containing the tree
    treename: name of the tree
    returns: TChain Object
    """
    tree = ROOT.TChain(treename)
    tree.AddFile(filename)
    return tree

def reweightPtEta(tree, applyWeight=True):
    num = ROOT.TH2F("num", "", 100, 0, 200, 30, 0, 3)
    den = num.Clone("den")
    tree.Draw("abs(eta):pt>>num", " isTrue", "goff")
    tree.Draw("abs(eta):pt>>den", "!isTrue", "goff")

    weightTree = ROOT.TTree("weightTree", "")
    import numpy
    weight = numpy.zeros(1, dtype=float)
    weightTree.Branch("weight", weight, "weight/D")
    for event in tree:
        bin = num.FindBin(event.pt, abs(event.eta))
        if event.isTrue:
            weight[0] = 1./num.GetBinContent(bin)
        else:
            weight[0] = 1./den.GetBinContent(bin)
        if not applyWeight: wegiht[0] = 1.
        weightTree.Fill()
    tree.AddFriend(weightTree)

tree = readTree("../gjets.root")
reweightPtEta(tree, False)

cut = "hOverE<0.05"


histograms = [
    ("r9", 100, 0, 1),
    ("hOverE", 20, 0, 0.15),
    ("pt", 2000, 0, 2000),
]


for var, nBins, xmin, xmax in histograms:
    h1 = createHistoFromTree(tree, var, "weight*( isTrue && {})".format(cut), nBins, xmin, xmax)
    h2 = createHistoFromTree(tree, var, "weight*(!isTrue && {})".format(cut), nBins, xmin, xmax)

    h1.SetLineColor(ROOT.kBlack)
    h2.SetLineColor(ROOT.kRed)

    for h in h1, h2:
        h.Scale(1./h.Integral())

    h1.Draw("hist")
    h2.Draw("hist same")
    ROOT.gPad.SaveAs("{}.pdf".format(var))

