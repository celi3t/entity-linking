# entity-linking
Evaluating entity hashing / bloom filters methods for private record linkages

### Repo Structure:

#### datasets:
Util to simulate entities. Uses Faker to simulate names and other personal information.
Noise in names is added in the following ways:
* sample from a lookup of names with related nicknames / similar names
* typos in date of birth / invalid date of birth or ssn
* middle names that become first names
* 2 reported last names in one dataset, only one last name in the other
* todo: duplicate entries with mismatching information


#### evaluation:
Metrics to evaluate models
* confusion matrix
* precision, recall
* ROC curve


#### models:
Contains the actual name cleaning, dedup, and hashing algorithms to test
