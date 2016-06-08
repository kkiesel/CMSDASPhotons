import FWCore.ParameterSet.Config as cms


process = cms.Process("TreeWriter")
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
    "root://xrootd-cms.infn.it//store/mc/RunIISpring16MiniAODv1/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02ED80EA-5012-E611-BC71-842B2B76670F.root"
))
process.TFileService = cms.Service("TFileService",fileName = cms.string("gjet.root"))

if False:
    process.source.fileNames = [ "root://xrootd-cms.infn.it//store/mc/RunIISpring16MiniAODv1/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/MINIAODSIM/PUSpring16_magnetOn_80X_mcRun2_asymptotic_2016_v3-v1/60000/968DC4DC-4F0D-E611-8E0F-0025905C2C86.root" ]
    process.TFileService.fileName = "qcd.root"

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "80X_mcRun2_asymptotic_2016_v3", '')

######################
# PHOTONS, ELECTRONS #
######################
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
from RecoEgamma.PhotonIdentification.PhotonIDValueMapProducer_cfi import *
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

# turn on VID producer, indicate data format to be DataFormat.MiniAOD
dataFormat = DataFormat.MiniAOD
switchOnVIDElectronIdProducer(process, dataFormat)
switchOnVIDPhotonIdProducer(process, dataFormat)

# define which IDs we want to produce
el_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff']
ph_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring15_25ns_V1_cff',
                 'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Spring15_25ns_nonTrig_V2_cff']

#add them to the VID producer
for idmod in el_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
for idmod in ph_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)

process.TreeWriter = cms.EDAnalyzer('TreeWriter',
    photons = cms.InputTag("slimmedPhotons"),
    prunedGenParticles = cms.InputTag("prunedGenParticles"),
    electronVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    electronLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    photonLooseIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
    photonMediumIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-medium"),
    photonTightIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-tight"),
    photonMvaValuesMap = cms.InputTag("photonMVAValueMapProducer:PhotonMVAEstimatorRun2Spring15NonTrig25nsV2Values"),
)

process.p = cms.Path(
    process.photonIDValueMapProducer
    *process.egmGsfElectronIDSequence
    *process.egmPhotonIDSequence
    *process.TreeWriter
)


