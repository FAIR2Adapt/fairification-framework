# Evaluation in the CCA case studies

## Online summary of the evaluation of the FAIR supporting services

This page provides an **online summary of the evaluation of the FAIR supporting services as part of the FAIRification framework based on the CCA case studies**.

The FAIR2Adapt requirements elicitation process starts from case-study user stories and FAIR Implementation Profiles (FIPs). The resulting requirements are used to identify FAIR gaps, define FAIRification plans and select the FAIR Supporting Resources (FSRs) needed to execute them. The services described below therefore respond to concrete needs identified in the Climate Change Adaptation (CCA) case studies rather than being isolated technical components.

The evaluation is organised around four service groups: **FAIR Assessment**, **I-ADOPT Variable Service**, **Knowledge Extraction, Metadata Enrichment and Claims**, and the **FAIR Data Publishing Pipeline**. The FAIR Solutions provide the main validation scenarios in which these services are combined into end-to-end FAIRification workflows.

## From user requirements to FAIR supporting services

| User requirement / identified need | FAIR supporting service | Response in the FAIRification Framework | CCA validation context |
| --- | --- | --- | --- |
| Identify FAIR gaps in heterogeneous digital objects and compare the current state with community FAIR expectations | FAIR Assessment | Executes FAIR tests and represents results using interoperable FAIR Test Results (FTR); supports assessment of datasets, software, semantic artefacts and aggregated Research Objects | Used as the assessment and validation layer of the FAIRification workflows |
| Move from qualitative FIP-based gap analysis to repeatable quantitative assessment | FAIR Assessment | Uses the As-Is FIP, Reference FIP, metadata requirements and FAIR metrics as inputs for assessment and FAIRification planning | Cross-cutting requirement across the six case studies |
| Describe scientific variables in a machine-actionable and interoperable way without requiring users to be semantic-web experts | I-ADOPT Variable Service | Converts natural-language variable descriptions into I-ADOPT components, enriches them with semantic concepts and keeps a human in the loop | RiOMar/oceanographic variables and other case-study variables |
| Make unstructured scientific and adaptation knowledge machine actionable | Metadata Enrichment | Extracts topics, key elements, entities and other semantic metadata from textual research resources | Scientific-publication and literature-review workflows |
| Extract reusable scientific assertions instead of leaving knowledge locked inside publications | Claim Extraction and Verification | Extracts self-contained scientific claims and supports verification against a curated climate-adaptation literature collection | Hamburg knowledge-production scenario and Portugal/weADAPT literature workflow |
| Preserve claims, evidence and provenance in machine-readable form | Claim / Knowledge Production services | Represents validated assertions as nanopublications and incorporates them into enriched FAIR Digital Objects | Knowledge-production and adaptation-hub FAIR Solutions |
| Make very large model datasets usable by third parties, not merely findable and downloadable | FAIR Data Publishing Pipeline | Creates virtual analysis-ready views, supports subsetting/regridding and cloud-optimised publication while preserving provenance | RiOMar coastal-water-quality FAIR Solution |
| Support reuse of FAIRification approaches across case studies and transfer cases | FAIR Data Publishing Pipeline and FAIRification workflows | Uses modular services, RO-Crate packaging and interoperable publication mechanisms so workflows can be transferred and adapted | RiOMar → Arctic synergies; Hamburg GIS workflow → Bremen/transfer cases |

## FAIR Assessment

The requirements analysis showed that FAIRification must begin with an understanding of the current FAIR status of the digital objects and the target practices expressed by the communities. The case studies therefore use **FAIR Implementation Profiles as a qualitative gap-analysis mechanism**, while the FAIR Assessment service provides the quantitative and repeatable assessment layer.

The service is affected by the requirements in three important ways:

* **Community-specific assessment.** The relevant FAIR criteria depend on the type of digital object, the CCA scenario and the FIP adopted by the community. The assessment architecture therefore distinguishes FAIR metrics, tests, benchmarks and scoring algorithms instead of assuming that one fixed score is sufficient for every case.
* **Heterogeneous resources.** Case-study workflows contain datasets, software, publications, semantic artefacts and compound FAIR Digital Objects. Assessment consequently needs to combine specialised validators while providing a common representation of their results.
* **Transparent FAIRification planning.** Assessment results must be usable as inputs to FAIRification plans. FAIR Test Results (FTR) provide an interoperable and provenance-oriented representation that makes the evidence behind an assessment explicit.

The current evaluation also exposes limitations that are relevant to the requirements: FAIR validators can implement different interpretations of FAIR, resource categories may have different numbers of tests, and aggregation strategies can influence the resulting score. These limitations motivate further work on community-specific benchmarks, aggregation algorithms and more detailed FAIRification recommendations.

## I-ADOPT Variable Service

Variable descriptions occur throughout the CCA case studies, but variables are frequently expressed as free-text labels. This limits comparison and automated reuse across datasets, disciplines and infrastructures. The requirements work explicitly identifies the extraction and later semantic enrichment of variables with the **I-ADOPT Framework** as part of the FAIRification process.

The I-ADOPT service responds to these requirements by:

* accepting a **plain-language scientific variable definition**;
* using an LLM to propose an I-ADOPT-aligned decomposition;
* linking components to external semantic resources where possible;
* providing an editable visualisation so that the researcher remains **in the loop**;
* producing machine-actionable RDF/Turtle;
* supporting publication of the variable as a persistent, citable semantic object.

This is particularly relevant to the **RiOMar FAIR Solution**, where oceanographic variables associated with large model datasets need machine-actionable descriptions. The approach is also intended to support variables extracted from the other CCA case studies. The service reduces the need for case-study users to have detailed semantic-modelling expertise while retaining expert validation of the result.

## Knowledge Extraction, Metadata Enrichment and Claims

Several CCA user requirements concern information that is present in scientific publications, grey literature and other textual resources but is difficult to discover and reuse automatically. The FAIRification Framework therefore includes services that transform unstructured content into structured metadata and machine-readable knowledge.

### Metadata enrichment

The Metadata Extraction service supports the requirement to enrich research resources with semantic descriptions. It can identify topics, key elements and entities, including links to external semantic resources. These outputs can be combined with provenance and other metadata when creating an enriched FAIR Digital Object.

This is especially relevant where adaptation knowledge must be aggregated from distributed publications and knowledge resources rather than from already structured datasets.

### Scientific claims

The Claim Extraction service responds to the requirement to make the scientific findings contained in publications independently reusable. Extracted claims are expected to be self-contained, clear, concise, objective and generalisable scientific assertions rather than narrative or self-referential statements.

The Claim Verification service complements extraction by comparing a claim with related literature from a curated climate-adaptation collection and producing a verification report and rationale. Human validation remains important in the FAIRification workflow.

The relationship with the CCA requirements is visible in two FAIR Solutions:

* **Knowledge Production from Scientific Publications (Hamburg):** metadata extraction, claim extraction/verification and semantic descriptions support reusable and verifiable scientific knowledge.
* **Literature Review and Extraction Pipeline (Portugal + weADAPT):** publications are processed through metadata extraction, scientific-claim extraction and validation, nanopublication generation, semantic enrichment and FAIR Digital Object publication.

Once validated, scientific assertions can be represented as **nanopublications**, preserving the assertion together with provenance and supporting evidence. This turns knowledge that was previously embedded in a document into a machine-actionable component that can be discovered, cited, linked and reused.

The evaluation identifies further requirements for this service family, including stakeholder-driven refinement of custom tags, stronger human validation of claim extraction and verification, multilingual support, and support for additional resource types such as policy documents.

## FAIR Data Publishing Pipeline

The data-publishing requirements are particularly visible in **CS2 RiOMar**. Large coastal-ocean model outputs may already be findable and accessible but remain difficult to reuse because their storage layout is not designed for efficient subsetting, they are not cloud optimised and their spatial grid is not necessarily suitable for downstream applications.

The pipeline therefore interprets FAIR reuse as more than depositing a large file and assigning a persistent identifier. It responds to the case-study requirements by:

1. exposing the original large NetCDF model outputs through virtual reference catalogues rather than unnecessarily copying or fragmenting them;
2. supporting spatial subsetting and regridding to a common DGGS/HEALPix representation;
3. producing time-chunked, cloud-optimised Zarr data;
4. preserving the relationship between input data, processing software, output data and provenance;
5. packaging scientific software and models as RO-Crates for FAIR validation and publication;
6. preparing the resulting resources for catalogue-based discovery and interoperable reuse.

The requirements also drive the pipeline beyond RiOMar. The user-requirements analysis identifies cross-case-study reuse: the RiOMar approach to subsetting information can inform the Arctic case study, while other FAIRification pipelines can similarly be transferred between case studies.

The evaluation is still iterative. In particular, STAC cataloguing of the HEALPix/Zarr outputs, HEALPix regridding for the NorESM Arctic data, validation of reference-catalogue management at full volume, and automated RO-Crate packaging combined with FAIR scoring remain areas of ongoing work.


## FAIR Solutions used for validation

The FAIRification services are validated through four reusable FAIR Solutions. Each solution combines a demo Digital Object, a FAIRification Plan, a FAIRification Workflow and a demo FAIR Digital Object.

* **[FAIR Solution #1](fair-solutions/solution-1-riomar.md) — Data processing pipeline for coastal water quality modelling:** validates large-scale FAIR data transformation and publication using the RiOMar scenario.
* **[FAIR Solution #2](fair-solutions/solution-2-hamburg.md) — FAIR GIS workflow for urban climate risk assessment:** validates FAIRification of datasets, software, workflows, controlled-access resources and derived outputs in Hamburg, with transferability toward Bremen.
* **[FAIR Solution #3](fair-solutions/solution-3-knowledge.md) — Knowledge production from scientific publications:** validates machine-readable scientific statements and their explicit links to evidence and provenance through the Knowledge Loom.
* **[FAIR Solution #4](fair-solutions/solution-4-literature.md) — Literature review and extraction pipeline:** validates metadata enrichment, scientific-claim processing, nanopublication generation and FAIR Digital Object publication for the Portuguese adaptation context.

Together, these scenarios provide the practical basis for the **online summary of the evaluation of the FAIR supporting services as part of the FAIRification framework based on the CCA case studies**.

## What the CCA evaluation shows

The CCA case studies show that the four service groups address complementary parts of the same FAIRification process:

**requirements → FAIR assessment → FAIRification plan → semantic/data transformation → validation → publication**

The evaluation therefore does not treat a service as successful only because it can run independently. Its value is assessed through its contribution to an integrated FAIR Solution: identifying a case-study FAIR gap, applying the appropriate supporting service, producing a more machine-actionable digital object, and enabling that object or its knowledge to be discovered, interpreted and reused.

The FAIR Solutions demonstrate the feasibility of combining FAIR Assessment, variable semantic modelling, metadata and knowledge extraction, nanopublications, RO-Crates and FAIR publication mechanisms. At the same time, the identified limitations and planned extensions are retained as inputs for the next iteration of the FAIRification Framework.
