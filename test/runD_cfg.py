import FWCore.ParameterSet.Config as cms

process = cms.Process("CaloTest")
process.load("SimGeneral.HepPDTESSource.pdt_cfi")

process.load("IOMC.EventVertexGenerators.VtxSmearedGauss_cfi")

process.load("SimG4Core.CheckSecondary.test.DTarget_cfi")

process.load("SimG4Core.Application.g4SimHits_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        CheckSecondary = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        SimG4CoreGeometry = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        G4cerr = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        G4cout = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        )
    ),
    categories = cms.untracked.vstring('SimG4CoreGeometry', 
        'CheckSecondary', 
        'G4cout', 
        'G4cerr'),
    destinations = cms.untracked.vstring('cout')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)
process.source = cms.Source("FlatRandomEGunSource",
    PGunParameters = cms.untracked.PSet(
        PartID = cms.untracked.vint32(-211),
        MaxEta = cms.untracked.double(0.0),
        MaxPhi = cms.untracked.double(1.57079632679),
        MinEta = cms.untracked.double(0.0),
        MinE = cms.untracked.double(2.0049),
        MinPhi = cms.untracked.double(1.57079632679),
        MaxE = cms.untracked.double(2.0049)
    ),
    Verbosity = cms.untracked.int32(0)
)

process.Timing = cms.Service("Timing")

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    moduleSeeds = cms.PSet(
        g4SimHits = cms.untracked.uint32(9876),
        VtxSmeared = cms.untracked.uint32(123456789)
    ),
    sourceSeed = cms.untracked.uint32(135799753)
)

process.p1 = cms.Path(process.VtxSmeared*process.g4SimHits)
process.VtxSmeared.SigmaX = 0.00001
process.VtxSmeared.SigmaY = 0.00001
process.VtxSmeared.SigmaZ = 0.00001
process.g4SimHits.UseMagneticField = False
process.g4SimHits.Physics = cms.PSet(
    GFlashEmin = cms.double(1.0),
    G4BremsstrahlungThreshold = cms.double(0.5),
    DefaultCutValue = cms.double(1000.0),
    CutsPerRegion = cms.bool(True),
    Verbosity = cms.untracked.int32(0),
    EMPhysics = cms.untracked.bool(False),
    GFlashEToKill = cms.double(0.1),
    HadPhysics = cms.untracked.bool(True),
    GFlashEmax = cms.double(1000000.0),
    type = cms.string('SimG4Core/Physics/QGSP'),
    DummyEMPhysics = cms.bool(False)
)
process.g4SimHits.Watchers = cms.VPSet(cms.PSet(
    CheckSecondary = cms.PSet(
        SaveInFile = cms.untracked.string('DQGSP2.0GeV.root'),
        Verbosity = cms.untracked.int32(0),
        MinimumDeltaE = cms.untracked.double(0.0),
        KillAfter = cms.untracked.int32(1)
    ),
    type = cms.string('CheckSecondary')
), 
    cms.PSet(
        type = cms.string('KillSecondariesRunAction')
    ))

