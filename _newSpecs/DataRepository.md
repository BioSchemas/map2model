---
description: "This document covers the schema.org and bioschemas.org properties necessary\
  \ to describe data repositories, catalogues and databases in the life sciences,\
  \ organised by their requirement level (M for mandatory, R for recommended and O\
  \ for optional) and driven by a set of use cases. A simple example in JSON-LD is\
  \ also provided. The majority of these fields already exist in schema.org, others\
  \ are pending. \nNote that this draft will be improved progressively through the\
  \ bioschemas process.\n"
g_mapping_file: DataRepository Mapping
github_url: https://github.com/BioSchemas/DataRepositories
layout: new_spec_detail
name: DataRepository
new_props: []
properties:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Dataset
  marginality: Minimum
  name: dataset
  reused_from: DataCatalog
  sdo_desc: 'A dataset contained in this catalog. Inverse property: includedInDataCatalog.'
- bsc_dec: CreativeWork:Name,URL
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - CreativeWork
  - Text
  marginality: Recommended
  name: citation
  reused_from: DataCatalog
  sdo_desc: A citation or reference to another creative work, such as another publication,
    web page, scholarly article, etc.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Date
  - DateTime
  marginality: Recommended
  name: dateModified
  reused_from: DataCatalog
  sdo_desc: The date on which the CreativeWork was most recently modified or when
    the item's entry was modified within a DataFeed.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Date
  marginality: Optional
  name: datePublished
  reused_from: DataCatalog
  sdo_desc: Date of first broadcast/publication.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Text
  - URL
  marginality: Optional
  name: fileFormat
  reused_from: DataCatalog
  sdo_desc: Media type, typically MIME format (see IANA site) of the content e.g.
    application/zip of a SoftwareApplication binary. In cases where a CreativeWork
    has several media type representations, 'encoding' can be used to indicate each
    MediaObject alongside particular fileFormat information. Unregistered or niche
    file formats can be indicated instead via the most appropriate URL, e.g. defining
    Web page or a Wikipedia entry.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Minimum
  name: keywords
  reused_from: DataCatalog
  sdo_desc: Keywords or tags used to describe this content. Multiple entries in a
    keywords list are typically delimited by commas.
- bsc_dec: CreativeWork:Name,URL
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - CreativeWork
  - URL
  marginality: Recommended
  name: license
  reused_from: DataCatalog
  sdo_desc: A license document that applies to this content, typically indicated by
    URL.
- bsc_dec: person:email,name
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Organization
  - Person
  marginality: Minimum
  name: provider
  reused_from: DataCatalog
  sdo_desc: The service provider, service operator, or service performer; the goods
    producer. Another party (a seller) may offer those services or goods on behalf
    of the provider. A provider may also serve as the seller. Supersedes carrier.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - PublicationEvent
  marginality: Recommended
  name: publication
  reused_from: DataCatalog
  sdo_desc: A publication event associated with the item.
- bsc_dec: organization:name,location
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Organization
  marginality: Recommended
  name: sourceOrganization
  reused_from: DataCatalog
  sdo_desc: The Organization on whose behalf the creator was working.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Recommended
  name: alternateName
  reused_from: Thing
  sdo_desc: An alias for the item.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Minimum
  name: description
  reused_from: Thing
  sdo_desc: A description of the item.
- bsc_dec: identifier:accessURL,identifierPattern,exampleIdentifeir
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - PropertyValue
  - Text
  - URL
  marginality: Minimum
  name: identifier
  reused_from: Thing
  sdo_desc: The identifier property represents any kind of identifier for any kind
    of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated
    properties for representing many of these, either as textual strings or as URL
    (URI) links. See background notes for more details.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Minimum
  name: name
  reused_from: Thing
  sdo_desc: The name of the item.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - URL
  marginality: Minimum
  name: url
  reused_from: Thing
  sdo_desc: URL of the item.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain_case: reu_sdo
  expected_type:
  - ''
  marginality: Optional
  name: metrics
  reused_from: Thing
  sdo_desc: ''
reu_props: []
spec_mapping_url: https://docs.google.com/spreadsheets/d/1H12h5VpVNJFzNs2RQJWjXkauCEn3qEsVFzKRoiHHffY/edit?usp=drivesdk
status: revision
stereotype: None
subtitle: Bioschemas specification for describing data repositories and data catalogues
  in the life-sciences.
version: 0.0.1
---