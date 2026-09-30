# FAIR Data Publishing Pipeline

The FAIR Data Publishing Pipeline supports the transformation and publication of large-scale geospatial climate-adaptation datasets as analysis-ready, interoperable FAIR Digital Objects.

## Role in the FAIRification Framework

Large scientific datasets can be findable and accessible while still being difficult to reuse. Very large files, unsuitable chunking, non-cloud-optimised layouts and incompatible spatial grids can prevent efficient analysis by third parties.

The pipeline addresses these practical barriers to **Interoperability** and **Reusability** while preserving the relationships between data, software, processing steps and provenance.

## Response to user requirements

The requirements from **CS2 RiOMar** strongly shape the pipeline.

### Large model outputs must be usable, not only downloadable

RiOMar produces high-volume NetCDF coastal-ocean model outputs. Instead of treating deposition and persistent identification as the end of FAIRification, the pipeline creates a virtual analysis-ready representation using reference catalogues so that the source data do not need to be unnecessarily copied or fragmented.

### Users need efficient spatial access

The workflow supports the derivation of a Region of Interest and regridding to a common **DGGS/HEALPix** representation. The output is organised as time-chunked, cloud-optimised Zarr, improving downstream access and processing.

### Data, software and provenance must remain connected

The FAIR Solution distinguishes input big data, processing software and output data while preserving their relationships. Scientific software and models can be packaged as RO-Crates, FAIR assessed and published through ROHub.

### Pipelines should transfer across case studies

The requirements analysis identifies cross-case synergies. The RiOMar approach to subsetting and processing information can inform the Arctic case study, demonstrating that the pipeline is intended as a reusable FAIRification pattern rather than a one-off transformation.

## Evaluation in the CCA case studies

The pipeline is evaluated through **FAIR Solution #1: Data Processing Pipeline for Coastal Water Quality (CS2 RiOMar)**. Its purpose is to overcome limited accessibility and practical usability of model data through regridding, FAIRification and catalogue-oriented publication.

Current outputs include HEALPix-indexed, time-chunked, cloud-optimised Zarr stores. The software and models are represented as RO-Crates for FAIR validation and publication.

The evaluation also identifies work that is still in progress:

* HEALPix regridding for the NorESM Arctic sample requires adaptation because its tripolar ocean grid differs from RiOMar's curvilinear coastal grid;
* STAC cataloguing of multidimensional HEALPix/Zarr outputs is planned as the relevant community patterns mature;
* reference-catalogue management at full dataset volume continues to be validated;
* automated RO-Crate generation and integration with FAIR scoring are objectives for the next iteration.

These points are retained as requirements for the continued development of the FAIR Data Publishing Pipeline.

!!! info "CCA evaluation"
    See **Evaluation in the CCA case studies** for the online summary of how the Data Pipeline and the other FAIR supporting services respond to the case-study requirements.
