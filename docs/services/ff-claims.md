# Scientific claims extraction and verification

The Claim Extraction and Claim Verification services support the transformation of scientific findings embedded in textual documents into machine-readable, reusable knowledge.

## Role in the FAIRification Framework

Claim extraction uses LLM-based semantic analysis to identify meaningful scientific or factual assertions in textual content. Extracted claims are intended to be self-contained, clear, concise, objective and generalisable rather than narrative or self-referential statements.

Claim verification complements this process by comparing extracted claims with related scientific literature and returning evidence together with a verification rationale.

## Response to user requirements

Several CCA requirements concern knowledge that is difficult to reuse because it remains locked inside scientific publications and grey literature.

### Make scientific findings reusable

A publication may be findable and accessible while its individual findings remain unavailable to automated systems. Claim extraction addresses this gap by identifying scientific assertions that can be handled independently from the document.

### Connect assertions to evidence and provenance

The FAIRification workflow can represent validated assertions as **nanopublications**. This enables the assertion, provenance and supporting evidence to be preserved as machine-readable components of an enriched FAIR Digital Object.

### Retain human validation

The case-study evaluation confirms that human validation remains important for the quality, reliability and interpretability of automatically extracted and verified claims. Strengthening human validation is therefore a requirement for the next iteration of the services.

## Evaluation in the CCA case studies

The services are particularly relevant to two FAIR Solutions.

### Hamburg — Knowledge Production from Scientific Publications

The Hamburg scenario combines metadata extraction, scientific claims, semantic descriptions and FAIR publication to make research knowledge verifiable and reusable by researchers who want to build upon previous methods and results.

### Portugal and weADAPT — Literature Review and Extraction Pipeline

The workflow transforms selected publications into machine-actionable FAIR resources through:

1. publication selection;
2. metadata extraction;
3. scientific claim extraction and validation;
4. nanopublication creation;
5. semantic enrichment;
6. FAIR Digital Object creation and publication.

The resulting knowledge can be consumed by adaptation hubs, dashboards, knowledge graphs and decision-support systems.

The evaluation also identifies future requirements: stronger human validation, support for policy documents and knowledge platforms, multilingual processing, and replication for additional hazards and national adaptation contexts.

!!! info "CCA evaluation"
    See **Evaluation in the CCA case studies** for the online summary of how claims/enrichment and the other FAIR supporting services respond to the case-study requirements.
