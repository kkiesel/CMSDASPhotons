// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Common/interface/ValueMap.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"

#include "TTree.h"
#include "Math/VectorUtil.h"
#include "TMath.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class TreeWriter : public edm::EDAnalyzer {
 public:
   explicit TreeWriter(const edm::ParameterSet&);
   ~TreeWriter(){};

   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

 private:
   virtual void beginJob() override {};
   virtual void endJob() override {};
   virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

   edm::EDGetTokenT<edm::View<pat::Photon>> photonCollectionToken_;
   edm::EDGetTokenT<edm::View<pat::Electron> > electronCollectionToken_;
   edm::EDGetTokenT<edm::View<reco::GenParticle>> prunedGenToken_;

   // photon id
   edm::EDGetTokenT<edm::ValueMap<bool>> photonLooseIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool>> photonMediumIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool>> photonTightIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<float>> photonMvaValuesMapToken_;
   edm::EDGetTokenT<edm::ValueMap<vid::CutFlowResult>> phoLooseIdFullInfoMapToken_;

   // electron id
   edm::EDGetTokenT<edm::ValueMap<bool>> electronVetoIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool>> electronLooseIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool>> electronMediumIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool>> electronTightIdMapToken_;


   TTree *eventTree_;
   float pt;
   float eta;
   float sigmaIetaIeta;
   float hOverE;
   float r9;
   float cIso;
   float nIso;
   float pIso;
   float mvaValue;
   bool hasPixelSeed;
   bool passElectronVeto;
   bool isTrue;
   bool isLoose;
   bool isMedium;
   bool isTight;
   edm::Service<TFileService> fs_;
};


TreeWriter::TreeWriter(const edm::ParameterSet& iConfig)
   : photonCollectionToken_     (consumes<edm::View<pat::Photon>>(iConfig.getParameter<edm::InputTag>("photons")))
   , electronCollectionToken_(consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("electrons")))
   , prunedGenToken_            (consumes<edm::View<reco::GenParticle>>(iConfig.getParameter<edm::InputTag>("prunedGenParticles")))
   , photonLooseIdMapToken_     (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("photonLooseIdMap")))
   , photonMediumIdMapToken_    (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("photonMediumIdMap")))
   , photonTightIdMapToken_     (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("photonTightIdMap")))
   , photonMvaValuesMapToken_   (consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("photonMvaValuesMap")))
   , phoLooseIdFullInfoMapToken_(consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("photonLooseIdMap" )))
   , electronVetoIdMapToken_    (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("electronVetoIdMap")))
   , electronLooseIdMapToken_   (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("electronLooseIdMap")))
   , electronMediumIdMapToken_  (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("electronMediumIdMap")))
   , electronTightIdMapToken_   (consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("electronTightIdMap")))
{
   eventTree_ = fs_->make<TTree> ("eventTree", "event data");
   eventTree_->Branch("pt", &pt);
   eventTree_->Branch("eta", &eta);
   eventTree_->Branch("sigmaIetaIeta", &sigmaIetaIeta);
   eventTree_->Branch("hOverE", &hOverE);
   eventTree_->Branch("r9", &r9);
   eventTree_->Branch("cIso", &cIso);
   eventTree_->Branch("nIso", &nIso);
   eventTree_->Branch("pIso", &pIso);
   eventTree_->Branch("mvaValue", &mvaValue);
   eventTree_->Branch("isLoose", &isLoose);
   eventTree_->Branch("isMedium", &isMedium);
   eventTree_->Branch("isTight", &isTight);
   eventTree_->Branch("hasPixelSeed", &hasPixelSeed);
   eventTree_->Branch("passElectronVeto", &passElectronVeto);
   eventTree_->Branch("isTrue", &isTrue, "isTrue/O");
}

void
TreeWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   // get gen particles before photons for the truth match
   edm::Handle<edm::View<reco::GenParticle>> prunedGenParticles;
   iEvent.getByToken(prunedGenToken_,prunedGenParticles);

   edm::Handle<edm::ValueMap<bool>> loose_id_dec;
   edm::Handle<edm::ValueMap<bool>> medium_id_dec;
   edm::Handle<edm::ValueMap<bool>> tight_id_dec;
   edm::Handle<edm::ValueMap<float>> mva_value;
   edm::Handle<edm::ValueMap<vid::CutFlowResult>> loose_id_cutflow;
   iEvent.getByToken(photonLooseIdMapToken_, loose_id_dec);
   iEvent.getByToken(photonMediumIdMapToken_, medium_id_dec);
   iEvent.getByToken(photonTightIdMapToken_, tight_id_dec);
   iEvent.getByToken(photonMvaValuesMapToken_, mva_value);
   iEvent.getByToken(phoLooseIdFullInfoMapToken_, loose_id_cutflow);

   // photon collection
   edm::Handle<edm::View<pat::Photon>> photonColl;
   iEvent.getByToken(photonCollectionToken_, photonColl);

   for (edm::View<pat::Photon>::const_iterator pho = photonColl->begin(); pho != photonColl->end(); pho++) {
      // some basic selections
      if (pho->pt() < 15 || pho->hadTowOverEm() > 0.15) continue;
      const edm::Ptr<pat::Photon> phoPtr(photonColl, pho - photonColl->begin());

      pt = pho->pt();
      eta = pho->eta();
      sigmaIetaIeta=pho->full5x5_sigmaIetaIeta();
      hOverE=pho->hadTowOverEm() ;
      hasPixelSeed=pho->hasPixelSeed() ;
      passElectronVeto= pho->passElectronVeto() ;
      r9  = pho->r9();

      vid::CutFlowResult cutFlow = (*loose_id_cutflow)[phoPtr];
      cIso = cutFlow.getValueCutUpon(4);
      nIso = cutFlow.getValueCutUpon(5);
      pIso = cutFlow.getValueCutUpon(6);

      mvaValue = (*mva_value)    [phoPtr];
      isLoose  = (*loose_id_dec) [phoPtr];
      isMedium = (*medium_id_dec)[phoPtr];
      isTight  = (*tight_id_dec) [phoPtr];

      // mc matching
      bool foundPhoton = false;
      bool vetoPhoton = false;
      for (auto& genP: *prunedGenParticles) {
         if (fabs(genP.pdgId()) == 22
            && genP.statusFlags().fromHardProcess()
            && genP.status() == 1
            && ROOT::Math::VectorUtil::DeltaR(pho->p4(), genP.p4())<0.1) {
            foundPhoton = true;
         } else if (fabs(genP.pdgId()) == 22
            && ROOT::Math::VectorUtil::DeltaR(pho->p4(), genP.p4())<0.4) {
            vetoPhoton = true;
         }
      }
      if (foundPhoton) {
         isTrue = true;
         eventTree_->Fill();
      }
      if (!vetoPhoton) {
         isTrue = false;
         eventTree_->Fill();
      }

   }

   // Get the electron ID data from the event stream
   edm::Handle<edm::ValueMap<bool>> veto_id_decisions;
   edm::Handle<edm::ValueMap<bool>> loose_id_decisions;
   edm::Handle<edm::ValueMap<bool>> medium_id_decisions;
   edm::Handle<edm::ValueMap<bool>> tight_id_decisions;
   iEvent.getByToken(electronVetoIdMapToken_, veto_id_decisions);
   iEvent.getByToken(electronLooseIdMapToken_, loose_id_decisions);
   iEvent.getByToken(electronMediumIdMapToken_, medium_id_decisions);
   iEvent.getByToken(electronTightIdMapToken_, tight_id_decisions);

   edm::Handle<edm::View<pat::Electron>> electronColl;
   iEvent.getByToken(electronCollectionToken_, electronColl);

   for (edm::View<pat::Electron>::const_iterator el = electronColl->begin();el != electronColl->end(); el++) {
      const edm::Ptr<pat::Electron> elPtr (electronColl, el - electronColl->begin() );
      bool isLoose = (*loose_id_decisions) [elPtr];
      if (isLoose && false ) std::cout << el->pt() << std::endl;
   }
}

void
TreeWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(TreeWriter);
