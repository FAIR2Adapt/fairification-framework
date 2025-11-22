## DeSci Publish

### Role in the FAIRification Framework
DeSci Publish is a pre-print and publication platform built using Content Identifiers (CIDs) through the Inter-Planetary File System (IPFS). This system gives all Research Objects truely persistent identifiers version control, an Automatically Generated RO Crate, and AI knowledge enhancement + search for Research Objects. 

This service can currently make it easier for researchers to ensure their public research object metadata is in line with FAIR principles. It has the capability to provide RO Crates and limited metadata for private data, or to act as a public or private gateway to data hosted on local servers. 

### Input / Outputs
Input: any research artifact or file type 

Output: a research object with a dPID, RO Crate, and AI analysis. 

### API specification
A complete specification of the API can be found [here](https://nodes-api.desci.com/documentation/).

### Principles
For the FAIR Principles, DeSci Publish can allow the following - 

For Findability. 
1. F1 - [(Meta) data are assigned globally unique and persistent identifiers] (https://www.go-fair.org/fair-principles/f1-meta-data-assigned-globally-unique-persistent-identifiers/). It assigns persistent identifiers using the dPID protocol which allows for fine-grained identifiers for each research artifact down to a data point. It also assigns DOI's for the Research Object as a whole. 
2. F3 - [Metadata clearly and explicitly include the identifier of the data they describe](https://www.go-fair.org/fair-principles/f3-metadata-clearly-explicitly-include-identifier-data-describe/)
3. F4 - [(Meta)data are registered or indexed in a searchable resource](https://www.go-fair.org/fair-principles/f4-metadata-registered-indexed-searchable-resource/). We are indexed both on Google Scholar and on the InterPlanetary Network Indexer. 

For Accesibility - 
You can retrieve the metadata using either https or IPFS
1. A 1.1 - [The protocol is open, free and universally implementable](https://www.go-fair.org/fair-principles/a1-1-protocol-open-free-universally-implementable/). Both HTTPS and IPFS are open protocols. 

For Interoperability - 
1. I1 - [(Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation](https://www.go-fair.org/fair-principles/i1-metadata-use-formal-accessible-shared-broadly-applicable-language-knowledge-representation/). We create RO Crates in line with RDF and JSON-LD Standards. 
2. I2 - [Meta)data use vocabularies that follow the FAIR principles](https://www.go-fair.org/fair-principles/i2-metadata-use-vocabularies-follow-fair-principles/). We use the schema.org vocabularies through RO Crate. 

For Reusability - 
1. R1.1 - [(Meta)data are released with a clear and accessible data usage license](https://www.go-fair.org/fair-principles/r1-1-metadata-released-clear-accessible-data-usage-license/). We ask for license attribution from the authors upon upload and associate this with the (meta)data.
2. R1.2 - [(Meta)data are associated with detailed provenance](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/). All (meta)data are associated with upload information + version control. We do not track what happens before the data reaches the platform. 


### Metadata
We extract Title, Authors, Keywords, and Abstract directly from the text. From there we use the Open Alex API to assign OrcIDs to authors, and match the keywords to topics.   

We additionally discover related papers and qualified reviewers. 
