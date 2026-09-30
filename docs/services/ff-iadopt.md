# Automated I-ADOPT service

The I-ADOPT Variable Service transforms natural-language descriptions of scientific variables into machine-interpretable representations aligned with the **I-ADOPT Framework Ontology**.

## Role in the FAIRification Framework

Scientific variables are frequently described only with free-text labels. This makes them difficult to compare, integrate and process automatically across datasets and infrastructures. I-ADOPT addresses this problem by decomposing a variable into semantic components such as the property, object of interest, matrix, contextual objects, statistical modifiers and constraints.

The service combines LLM-assisted decomposition with a **human-in-the-loop** workflow. A user supplies a plain-language variable definition, reviews the proposed decomposition and can correct it before producing an I-ADOPT-conformant representation.

## Response to user requirements

The FAIR2Adapt requirements process explicitly identifies variables from case-study digital objects so that they can later be enriched and aligned with I-ADOPT. This affects the service in several ways.

### Lower the semantic-modelling barrier

CCA researchers and data providers need machine-actionable variable metadata, but they cannot be expected to be experts in semantic-web modelling. The service therefore starts from a natural-language definition and proposes the decomposition automatically.

### Keep domain experts in control

Automatic decomposition cannot replace domain knowledge. The proposed representation is presented to the user for review and correction. This human-in-the-loop approach responds to the need for automation while preserving semantic quality and scientific oversight.

### Produce reusable machine-actionable variables

The result is not only a textual description. The service generates standards-compliant RDF/Turtle aligned with I-ADOPT, can link components to external semantic concepts and supports persistent publication of variable descriptions.

## Evaluation in the CCA case studies

The service is directly relevant to **CS2 RiOMar**, where oceanographic variables associated with the coastal-water-quality model outputs need interoperable descriptions. I-ADOPT variable descriptions form part of the RiOMar FAIR Solution together with the data-processing/publishing pipeline, RO-Crate profiles and FAIR publication mechanisms.

The requirements analysis also envisages I-ADOPT enrichment across the case studies. This makes the service a semantic interoperability layer that can be reused wherever variables extracted from datasets or publications need to be represented in a machine-actionable form.

The service is designed for researchers, data stewards and infrastructure developers who need FAIR-compliant variable metadata without requiring deep semantic-web expertise.

!!! info "CCA evaluation"
    See **Evaluation in the CCA case studies** for the online summary of how the I-ADOPT service and the other FAIR supporting services respond to the case-study requirements.
