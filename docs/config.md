# NGRAM for NLP

<!-- For full documentation visit [mkdocs.org](https://www.mkdocs.org). -->

## Configuration
Before starting the N-gram models training, you need to modify **config.json**.

This file includes all the parameters necessary to perform the training and use of the models.

### Default parameters
- **generate_name** : project name
- **source** : Path of the data file(s)

- **data_type** : type of data

| **Values** | **Description** |
|---------------|---------------|
| df      | Load dataframe      |
| files      | Load files in the folder      |

- **file_extension** (optional): extension that files must have (if select, depending on data_type)

- **source_params** (optional, if data_type=="df")
    - **df_column** : column to select data from
    - **df_parameters** : DataFrame opening parameters (used in pandas.read_csv())

- **parallelize** : True/False if we want the training to be parallelized

- **dask_distributed** : True/False if we want the training to be made on a Dask Cluster

### Training parameters

- **ngram_range_min**
- **ngram_range_max**

N-gram(s) will be generated in the range [ngram_range_min;ngram_range_max]

### Generator parameters
- **nb_sentences_to_generate** : number of sentence(s) to generate
- **delay** : delay of appearance of generated sentences
- **starts_with** : string by which generated sentences should start
- **min_words** : minimum number of word needed in the generated sentence
- **end_char** : list of characters by which a generated sentence should end
- **display_model_used**: True/False if we want to show the model used at each word generation
- **max_ngram_to_use**: sets the value that will limit the model to be used for generating sentences

### Dask Parameters
- **scheduler_address** : IP of the Scheduler.
- **local_scheduler_address** : local IP:PORT of the Scheduler.
