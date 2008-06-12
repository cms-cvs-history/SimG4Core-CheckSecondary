import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'SimG4Core/CheckSecondary/test/data/TiTarget.xml'),
    rootNodeName = cms.string('TiTarget:OCMS')
)


