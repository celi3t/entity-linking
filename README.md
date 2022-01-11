# entity-linking
Evaluating entity hashing / bloom filters methods for private record linkages among multiple parties.
The code in this repo is a proof of concept for an end-to-end Master Data Management (MDM) solution, that includes:
* Entity normalization / canonicalization
* Entity deduplication
* ID creation methods
* Privacy-Protected entity resolution and linking


### Repo Structure:

```
entity-linking
│   README.md 
│
└───datasets
│       simulate_entities.py
│   
└───evaluation
│       metrics.py
│   
└───models
        bloom.ipynb
        preprocessing.py
        main_pyspark.ipynb
```

#### datasets:
Util to simulate entities. Uses `Faker` to simulate names and other personal information.
Noise in names is added in the following ways:
* sample from a lookup of names with related nicknames / similar names
* typos in date of birth / invalid date of birth or ssn
* middle names that become first names
* 2 reported last names in one dataset, only one last name in the other
* todo: duplicate entries with mismatching information

#### evaluation:
Metrics used to evaluate models
* confusion matrix
* precision, recall
* ROC curve
* Hash collisions rates (which in ER are equivalent to false positives rates)

#### models:
Contains the actual name cleaning, dedup-ing, and hashing algorithms.
Algorithms are inspired by the following papers (will likely add more):
* [Multi-Party Privacy-Preserving Record Linkage using Bloom Filters](https://arxiv.org/pdf/1612.08835.pdf)
* [Optimizing Bloom Filter: Challenges, Solutions, and Comparisons](https://arxiv.org/pdf/1804.04777.pdf)
* [Scalable Multi-Database Privacy-Preserving Record Linkage using Counting Bloom Filters](https://arxiv.org/pdf/1701.01232.pdf)



## Background: Problem
Privacy-protecting entity linking is
insert graph

## Background: phases of entity resolution and linkages:
### Canonicalization / Normalization
#### Problems of concern:
* pre process / clean and normalize data in a way that maximizes the chances of reconciling data entries to the correct entities
* definition of an entity view with both IDs and QIDs (quasi-identifiers such as phone and address)

### Deduplication
Basically, you are doind a "private" lookup on your data in order to assess whether the entity data entry should be associated to an existing entity (and eventually update the record), or create a new entity in the database.
...Upcoming....
#### Problems of concern:
* Schemas for entities
* Efficient updating

### ID creation (either token or hash, with or without encryption)
This phase is about creating a "Linkage Unit", that can take the form of a single ID (for unique identifiers, such as SSNs), multiple IDs (useful for quasi-identifiers, such as phone numbers), or composite identifiers (such as counting bloom filters, as discussed in [this paper](https://arxiv.org/pdf/1701.01232.pdf))
#### Problems of concern:
* For tokenization, trusted party must hold keys table
* For hashing, collisions causing false positives

### ID linking
...Upcoming...

All parties can share anonimyzed data and use IDs to lookup or join entities.
#### Problems of concern:
* Complexity of comparisons creates performance concerns of lookups or joins. Two steps techniques (1. blocking 2. retrieving) will be considered (e.g. Bloom Filters)




