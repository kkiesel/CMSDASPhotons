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


class TreeWriter : public edm::EDAnalyzer {
 public:
   explicit TreeWriter(const edm::ParameterSet&);
   ~TreeWriter(){};

   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

 private:
   virtual void beginJob() override {};
   virtual void endJob() override {};
   virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

   edm::EDGetTokenT<edm::View<pat::Photon> >   photonCollectionToken_;
   edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;

   // photon id
   edm::EDGetTokenT<edm::ValueMap<bool> > photonLooseIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool> > photonMediumIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<bool> > photonTightIdMapToken_;
   edm::EDGetTokenT<edm::ValueMap<float>> photonMvaValuesMapToken_;
   edm::EDGetTokenT<edm::ValueMap<vid::CutFlowResult>> phoLooseIdFullInfoMapToken_;

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
   : photonCollectionToken_  (consumes<edm::View<pat::Photon> >(iConfig.getParameter<edm::InputTag>("photons")))
   , prunedGenToken_         (consumes<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("prunedGenParticles")))
   , photonLooseIdMapToken_  (consumes<edm::ValueMap<bool> >(iConfig.getParameter<edm::InputTag>("photonLooseIdMap"  )))
   , photonMediumIdMapToken_ (consumes<edm::ValueMap<bool> >(iConfig.getParameter<edm::InputTag>("photonMediumIdMap" )))
   , photonTightIdMapToken_  (consumes<edm::ValueMap<bool> >(iConfig.getParameter<edm::InputTag>("photonTightIdMap"  )))
   , photonMvaValuesMapToken_(consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("photonMvaValuesMap")))
   , phoLooseIdFullInfoMapToken_(consumes<edm::ValueMap<vid::CutFlowResult> >(iConfig.getParameter<edm::InputTag>("photonLooseIdMap" )))
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
   eventTree_->Branch("isTrue", &isTrue, "isTrue/O");
   eventTree_->Branch("isLoose", &isLoose);
   eventTree_->Branch("isMedium", &isMedium);
   eventTree_->Branch("isTight", &isTight);
   eventTree_->Branch("hasPixelSeed", &hasPixelSeed);
   eventTree_->Branch("passElectronVeto", &passElectronVeto);
}

void
TreeWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   // get gen particles before photons for the truth match
   edm::Handle<edm::View<reco::GenParticle> > prunedGenParticles;
   iEvent.getByToken(prunedGenToken_,prunedGenParticles);

   edm::Handle<edm::ValueMap<bool> > loose_id_dec;
   edm::Handle<edm::ValueMap<bool> > medium_id_dec;
   edm::Handle<edm::ValueMap<bool> > tight_id_dec;
   edm::Handle<edm::ValueMap<float>> mva_value;
   edm::Handle<edm::ValueMap<vid::CutFlowResult> > loose_id_cutflow;
   iEvent.getByToken(photonLooseIdMapToken_  ,loose_id_dec);
   iEvent.getByToken(photonMediumIdMapToken_ ,medium_id_dec);
   iEvent.getByToken(photonTightIdMapToken_  ,tight_id_dec);
   iEvent.getByToken(photonMvaValuesMapToken_,mva_value);
   iEvent.getByToken(phoLooseIdFullInfoMapToken_,loose_id_cutflow);

   // photon collection
   edm::Handle<edm::View<pat::Photon> > photonColl;
   iEvent.getByToken(photonCollectionToken_, photonColl);

   bool foundCandidate = false;
   for(edm::View<pat::Photon>::const_iterator pho = photonColl->begin(); pho != photonColl->end(); pho++){
      // some basic selections
      if( pho->pt() < 15 || pho->hadTowOverEm() > 0.15 )
         continue;
      const edm::Ptr<pat::Photon> phoPtr( photonColl, pho - photonColl->begin() );

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

      mvaValue=(*mva_value)[phoPtr];
      isLoose = (*loose_id_dec) [phoPtr];
      isMedium= (*medium_id_dec)[phoPtr];
      isTight = (*tight_id_dec) [phoPtr];

      // mc matching
      isTrue = false;
      for (auto& genP: *prunedGenParticles) {
         if (fabs(genP.pdgId()) == 22
             && genP.statusFlags().fromHardProcess()
             && genP.status() == 1
             && ROOT::Math::VectorUtil::DeltaR(pho->p4(), genP.p4())<0.1) {
            isTrue = true;
         }
      }

      if (isTrue) break;
      foundCandidate = true;
   }
   if (foundCandidate) eventTree_->Fill();
}

void
TreeWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(TreeWriter);
