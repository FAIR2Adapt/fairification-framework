# FAIR Assessment

The FAIR Assessment service evaluates the FAIRness of digital resources and supports the identification of gaps that must be addressed by a FAIRification plan. Within FAIR2Adapt, assessment connects the requirements elicitation phase with the execution and validation of FAIRification workflows.

## Role in the FAIRification Framework

The assessment uses the current FAIR practices expressed through the **As-Is FAIR Implementation Profile (FIP)**, the target practices represented by a **Reference FIP**, synthesised metadata requirements and FAIR Assessment metrics. The results provide evidence for selecting FAIR Supporting Resources and defining the actions required to transform a digital object into a FAIR Digital Object.

The service supports heterogeneous resources and can combine results produced by specialised assessment tools. FAIR assessment results are represented using the **FAIR Test Results (FTR)** vocabulary, enabling transparent and interoperable reporting of metrics, tests, benchmarks and scoring algorithms.

## Response to user requirements

The CCA user requirements directly affect the design of the assessment service.

### From qualitative gap analysis to quantitative assessment

The requirements elicitation process uses FIPs to understand current and intended FAIR practices. Case-study providers need this qualitative analysis to be translated into repeatable assessments that can show where a digital object differs from the target FAIR practices. FAIROs and the wider FAIR Assessment architecture provide this quantitative layer.

### Different communities require different assessment perspectives

The FAIR requirements are not identical for every case study or every resource. Datasets, software, publications and semantic artefacts have different characteristics, while communities can select different FAIR Supporting Resources. The assessment model therefore separates:

* **metrics**, which describe what is being evaluated;
* **tests**, which implement an evaluation;
* **benchmarks**, which group metrics according to a community or FAIRification objective;
* **scoring algorithms**, which aggregate assessment results.

This makes it possible to evolve from a single generic assessment towards assessments better aligned with the FIPs and requirements of CCA communities.

### Assessment results must support action

Case-study users do not only need a FAIR score. They need to understand the gaps that prevent reuse and which FAIRification actions should follow. For this reason, assessment results feed the FAIRification Plan and are represented with provenance-oriented FTR descriptions that make individual test results transparent.

## Evaluation in the CCA case studies

FAIR Assessment is a cross-cutting component of the FAIR Solutions. It is used before FAIRification to identify gaps and after execution to validate the resulting FAIR Digital Objects against the selected metrics, Reference FIP and RO-Crate profiles.

The evaluation has also highlighted issues that influence future development:

* different validators may implement different interpretations of FAIR;
* resource categories can have different numbers of applicable tests, creating scoring asymmetries;
* aggregation strategies influence quantitative FAIRness indicators;
* community-specific benchmarks and improved FAIRification recommendations are needed.

These findings are treated as requirements for subsequent iterations of the service rather than hidden behind a single FAIRness score.

!!! info "CCA evaluation"
    See **Evaluation in the CCA case studies** for the online summary of how FAIR Assessment and the other FAIR supporting services respond to the case-study requirements.
