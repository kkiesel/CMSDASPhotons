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

def reweightPtEta(tree):
    num = ROOT.TH2F("num", "", 200, 0, 2000, 30, 0, 3)
    den = num.Clone("den")
    tree.Draw("abs(eta):pt>>num", " isTrue", "goff")
    tree.Draw("abs(eta):pt>>den", "!isTrue", "goff")
    num.Divide(den)

    weightTree = ROOT.TTree("weightTree", "")
    import numpy
    weight = numpy.zeros(1, dtype=float)
    weightTree.Branch("weight", weight, "weight/D")
    for event in tree:
        if event.isTrue:
            weight[0] = 1
        else:
            b = num.FindBin(event.pt, abs(event.eta))
            weight[0] = num.GetBinContent(b)
        weightTree.Fill()
    tree.AddFriend(weightTree)

def drawROC(tree, commonCut="1", cuts=[]):
    """Draw the reciver operating characteristics for the mva identification and draws marker for own selections"""
    c = ROOT.TCanvas()
    # Create ROC curve for MVA
    nBins = 100000
    h1 = createHistoFromTree(tree, "mvaValue", "weight*( isTrue && {})".format(commonCut), nBins, -1, 1).GetCumulative(False)
    h2 = createHistoFromTree(tree, "mvaValue", "weight*(!isTrue && {})".format(commonCut), nBins, -1, 1).GetCumulative(False)
    gr = ROOT.TGraph(nBins)
    gr.SetTitle(";Signal efficiency;Background rejection")
    for bin in range(1, nBins+1):
        s = h1.GetBinContent(bin)/h1.GetBinContent(1)
        b = h2.GetBinContent(bin)/h2.GetBinContent(1)
        gr.SetPoint(bin-1, s, 1-b)
    gr.GetXaxis().SetRangeUser(0,1)
    gr.GetYaxis().SetRangeUser(0,1)
    gr.Draw()
    # For each marker, add a point
    markers = [] # save markers so pyroot won't overwrite them
    for icut, cut in enumerate(cuts):
        h1 = createHistoFromTree(tree, cut, "weight*( isTrue && {})".format(commonCut), 2, 0, 2)
        h2 = createHistoFromTree(tree, cut, "weight*(!isTrue && {})".format(commonCut), 2, 0, 2)
        s = h1.GetBinContent(2)/h1.Integral()
        b = h2.GetBinContent(2)/h2.Integral()
        m = ROOT.TMarker(s, 1-b, 20+icut)
        m.Draw()
        markers.append(m)
    ROOT.gPad.SaveAs("roc.pdf")

tree = readTree("../gjets.root")
reweightPtEta(tree)

cut = "hOverE<0.05"


histograms = [
    ("r9", 100, 0, 1),
    ("hOverE", 20, 0, 0.15),
    ("pt", 2000, 0, 2000),
]


for var, nBins, xmin, xmax in histograms:
    h1 = createHistoFromTree(tree, var, "weight*( isTrue && {})".format(cut), nBins, xmin, xmax)
    h2 = createHistoFromTree(tree, var, "weight*(!isTrue && {})".format(cut), nBins, xmin, xmax)

    h1.SetLineColor(1)
    h2.SetLineColor(2)

    for h in h1, h2:
        h.Scale(1./h.Integral())

    h1.Draw("hist")
    h2.Draw("hist same")
    ROOT.gPad.SaveAs("{}.pdf".format(var))

drawROC(tree, "pt<70 && abs(eta)<1.5", ["isLoose", "isMedium", "isTight"])
