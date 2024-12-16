# Heterogeneous Contrastive Graph (HCG) for Scientific Documments in English and Vietnamese Summarization

## Repository Structure

```tree
📦 Hetergenous-Contrastive-Graph
 ┣ 📂 CL_SciSumm_preprocessed     # English scientific papers dataset
 ┃ ┣ 📜 test_docs_v5.json        # Test documents
 ┃ ┣ 📜 test_label.json          # Test labels
 ┃ ┣ 📜 train_docs_v2.json       # Training documents
 ┃ ┗ 📜 train_label.json         # Training labels
 ┃
 ┣ 📂 VLSP Dataset               # Vietnamese news dataset
 ┃ ┣ 📜 LDA_models.pkl           # Pre-trained LDA models
 ┃ ┣ 📜 public.csv               # Public test data
 ┃ ┣ 📜 validation_data_new.jsonl # Validation data
 ┃ ┗ 📜 vietnamese-stopwords-dash.txt # Vietnamese stopwords
 ┃
 ┣ 📂 input_result_compare       # Results comparison
 ┃ ┣ 📜 result_compare_VN.json   # Vietnamese results
 ┃ ┣ 📜 result_compare.json      # English results  
 ┃ ┗ 📜 test_input_abstract_conclusion_v0.json
 ┃
 ┣ 📂 model                      # Model implementations
 ┃ ┣ 📜 evaluateFinal_evaluation_2_layer.ipynb  # Graph evaluation
 ┃ ┣ 📜 HCG-KHTK-Final.ipynb    # CL-SciSumm implementation
 ┃ ┗ 📜 vietnamese.ipynb         # Vietnamese implementation
 ┃
 ┣ 📜 dataset.py                 # Dataset utilities
 ┣ 📜 inits.py                   # Model initialization
 ┣ 📜 layers.py                  # Model layer definitions
 ┣ 📜 models.py                  # Model architecture
 ┣ 📜 run.py                     # Training script
 ┣ 📜 test.py                    # Testing script
 ┣ 📜 train_e2e.py              # End-to-end training
 ┣ 📜 test_adj.py               # Adjacency matrix testing
 ┗ 📜 utils.py                   # Helper functions
```
## Dataset
The repository contains two datasets:
1. **CL-SciSumm preprocessed Dataset** (in `CL_SciSumm_preprocessed/`)
2. **VLSP Dataset** (in `VLSP Dataset/`)

### Data Preprocessing for CL-SciSumm Dataset
Scientific papers are collected in PDF format from various sources. Using Grobid in a Docker environment, PDFs are converted to XML to extract titles, abstracts, body text, and citations. The extracted text is cleaned and formatted for deep learning models.


## Model Performance
### CL-SciSumm Dataset Results
| Model | ROUGE-2 F1 | ROUGE-SU4 F1 |
|-------|------------|--------------|
| LaSTUS/TALN+INCO | 0.241 | 0.171 |
| Graph Convolutional Network | 0.315 | 0.243 |
| BERT-based Classifier | 0.265 | 0.180 |  
| HCG (Our Model) | **0.368** | **0.379** |

#### Ablation Study Results
| Model Variant | ROUGE-1 ||| ROUGE-2 ||| ROUGE-SU4 |||
|--------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| | R | P | F1 | R | P | F1 | R | P | F1 |
| Full model | **0.584** | **0.547** | **0.561** | **0.384** | **0.358** | **0.368** | **0.395** | **0.368** | **0.378** |
| Without Contrastive Loss | 0.562 | 0.542 | 0.548 | 0.357 | 0.343 | 0.348 | 0.370 | 0.356 | 0.360 |
| Without Summarization Module | 0.572 | 0.530 | 0.546 | 0.372 | 0.341 | 0.354 | 0.385 | 0.353 | 0.366 |

### VLSP Dataset Results
| Model | ROUGE-2 ||| ROUGE-1 ||| ROUGE-L |||
|-------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| | P | R | F1 | P | R | F1 | P | R | F1 |
| The Coach | 0.2284 | 0.4463 | 0.2937 | 0.4072 | 0.6676 | 0.4962 | 0.3857 | 0.6326 | 0.4701 |
| CIST AI | 0.2629 | 0.3192 | 0.2805 | 0.4635 | 0.5352 | 0.4876 | 0.4314 | 0.4988 | 0.4541 |
| TheFinalYear | 0.2272 | 0.4040 | 0.2785 | 0.4221 | 0.6409 | 0.4956 | 0.3929 | 0.5964 | 0.4612 |
| NLP HUST | 0.2773 | 0.2829 | 0.2689 | 0.4903 | 0.4836 | 0.4732 | 0.4537 | 0.4465 | 0.4373 |
| Extractive Baseline | 0.2464 | 0.3174 | 0.2625 | 0.4582 | 0.5391 | 0.4772 | 0.4164 | 0.4905 | 0.4339 |
| Rule Baseline | 0.2634 | 0.2947 | 0.2611 | 0.4601 | 0.5053 | 0.4627 | 0.4257 | 0.4659 | 0.4273 |
| Anchor Baseline | 0.2306 | 0.1734 | 0.1886 | 0.5210 | 0.3900 | 0.4321 | 0.4659 | 0.3498 | 0.3869 |
| Abstractive Baseline | 0.3061 | 0.1025 | 0.1497 | 0.5801 | 0.2299 | 0.3226 | 0.5205 | 0.2065 | 0.2895 |
| **HCG (Our Model)** | **0.2765** | **0.3407** | **0.2966** | **0.4761** | **0.5429** | **0.4980** | **0.4459** | **0.5082** | **0.4663** |

#### Ablation Study Results
| Model Variant | ROUGE-1 F1 | ROUGE-2 F1 | ROUGE-L F1 |
|--------------|------------|------------|------------|
| Full model | **0.498** | **0.296** | **0.466** |
| No Contrastive Module | 0.471 | 0.263 | 0.443 |
| No Sentence-level Graph | 0.465 | 0.258 | 0.439 |
| No Summarization Module | 0.459 | 0.247 | 0.431 |


## Implementation & Training
The model implementations are available in three Jupyter notebooks under the `model/` directory:
1. `evaluateFinal_evaluation_2_layer.ipynb` - Graph evaluation with 3 models
2. `HCG-KHTK-Final.ipynb` - Original implementation for CL-SciSumm dataset
3. `vietnamese.ipynb` - Improved model implementation for Vietnamese dataset



