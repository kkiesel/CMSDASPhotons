import FWCore.ParameterSet.Config as cms

# dataset=/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"
inFileName = [
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D46A0D21-FD3E-E611-805C-008CFA0016A4.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D4960790-F43E-E611-ACEB-F04DA275C03D.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D4D1ECB3-F63E-E611-ACBA-3417EBE64762.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D4DFB450-F73E-E611-BA90-008CFA0014EC.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D6092FB8-FD3E-E611-96A1-7845C4FC3C86.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D620168C-F93E-E611-A440-00266CF9C22C.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D6A96F6D-F93E-E611-AE4E-7845C4F91450.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D6E6A96F-F83E-E611-BCFE-848F69FD2853.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D82B9B28-F33E-E611-9549-848F69FD2940.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/D8E5621C-E73E-E611-BB1B-848F69FD4553.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/DAD48FFF-FE3E-E611-AEB2-848F69FD28AA.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/DC2B8886-D63E-E611-B7BE-008CFAF75356.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/DEF27A96-F13E-E611-AA83-848F69FD28FE.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E2530B27-F83E-E611-ACA2-008CFAFBEEE6.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E2FEB07B-F83E-E611-999A-7845C4FC3B18.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E438F973-F93E-E611-822C-F04DA275BFB9.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E64F7067-F83E-E611-9932-848F69FD28FE.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E6DF49AA-F63E-E611-A088-848F69FD2940.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E6F1EA8D-FB3E-E611-9546-7845C4FC3B1B.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/E82EDE89-F03E-E611-A19E-F04DA275C019.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EAADF853-F93E-E611-B3E3-848F69FD29B2.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EAFD337D-EF3E-E611-A8C0-008CFA008F50.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EC2ECB74-F13E-E611-B138-008CFA002434.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EC5378ED-E23E-E611-8A9A-008CFAFBE8CE.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EC77EFA9-F43E-E611-B1B9-008CFA00038C.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/ECAAF81D-FE3E-E611-99A3-7845C4FC3B18.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/ECB40E4C-FB3E-E611-8398-008CFAFBEA7E.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/ECDDAE2F-F43E-E611-89F9-008CFAFBE5E0.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/ECE9DD57-FA3E-E611-87EE-00266CF9B59C.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EE007330-EC3E-E611-9B79-848F69FD29B2.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/EE6D98E3-003F-E611-963A-F04DA275BFDD.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F066F11A-FD3E-E611-A1A8-848F69FD45A7.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F0B7A770-FA3E-E611-A868-008CFAFC03F8.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F2273309-003F-E611-A9BA-848F69FD483E.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F254DB37-ED3E-E611-BC17-848F69FD4EFB.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F28A4D55-FA3E-E611-BCB5-180373FF8456.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F2C4B750-F63E-E611-ADF3-001D09FDD7DA.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F2E1E7DA-003F-E611-A53B-008CFAFBE8F2.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F45AFF34-F63E-E611-B963-7845C4FBB644.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F4B34692-FD3E-E611-833B-008CFAFBEEE6.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F4B3D50B-FF3E-E611-AA60-180373FF8D42.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F4FB800E-FF3E-E611-8878-848F69FD28FE.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F6E8AD7F-FE3E-E611-8CF6-F04DA275C328.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F80D9D80-F13E-E611-BF1D-7845C4FC39AA.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F834094C-F73E-E611-92CF-F04DA275C328.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F84E1673-F93E-E611-AB74-3417EBE6475F.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F856D0EE-ED3E-E611-9F66-24B6FDFF2B44.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/F86DB9A8-F23E-E611-A759-7845C4FC3B1B.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FA3C0723-FA3E-E611-9D51-F04DA275C328.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FA5A8776-F93E-E611-AB9A-00266CF9C22C.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FA73F45A-F83E-E611-BF21-F04DA275C328.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FA7A6523-FE3E-E611-AFF2-3417EBE64762.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FC1C575A-FA3E-E611-96CA-7845C4FC3B1B.root",
  "/store/mc/RunIISpring16MiniAODv2/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/FC836344-F23E-E611-8E95-848F69FD2940.root",
]
outFileName = "gjets.root"

process = cms.Process("TreeWriter")
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(inFileName))
process.TFileService = cms.Service("TFileService",fileName = cms.string(outFileName))

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
    electrons = cms.InputTag("slimmedElectrons"),
    prunedGenParticles = cms.InputTag("prunedGenParticles"),
    photonLooseIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
    photonMediumIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-medium"),
    photonTightIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-tight"),
    photonMvaValuesMap = cms.InputTag("photonMVAValueMapProducer:PhotonMVAEstimatorRun2Spring15NonTrig25nsV2Values"),
    electronVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    electronLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
)


process.p = cms.Path(
    process.photonIDValueMapProducer
    *process.egmGsfElectronIDSequence
    *process.egmPhotonIDSequence
    *process.TreeWriter
)


