# Advanced Fine Tuning: Drug Classification
## Step 1: Preparing the Data and Launching the Fine Tuning
### 1. Preparing the Data and Launching the Fine Tuning

* Download the .XLSX file from [here](https://www.kaggle.com/datasets/saratchendra/medicine-recommendation/)
* Add python code to transfor data into desired format.
* Got .jsonl file ready to use
  
  ![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/aa5756b1-eb8c-48c1-b450-d80146ef2af1)

### 2. Command to Prepare Data
```
$ openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
```
      
The output will show data analysis details and prompts for splitting into training and validation sets.

**Result:**
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/6ab8850e-3e9b-4c1e-84d6-48c9fab4d292)

### 3. Command to Train the Model
```
# Export your OpenAI key
$ export OPENAI_API_KEY="xxxxxxxxxxxx"

$ openai api fine_tunes.create \
   -t "drug_malady_data_prepared_train.jsonl" \
   -v "drug_malady_data_prepared_valid.jsonl" \
   --compute_classification_metrics \
   --classification_n_classes 3 \
   -m ada \
   --suffix "drug_malady_data"
```
***Fine-Tune Failed***
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/7b0d3ab5-f7eb-4c68-b8c1-cd0a6a6278ae)

***Do not split data to training and validation***
```
$ openai api fine_tunes.create -t "drug_malady_data.jsonl" -m ada
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/5d03e297-c17f-48d4-8d57-0bacdb316b2e)

### 4. Checking Job Progress
```
# List jobs
$ openai api fine_tunes.list
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/08d2ed14-686c-40cc-a0d1-4dbbabc375c3)

```
# Check progress
$ openai api fine_tunes.follow -i ft-lJeaTL7arLyYc9968zaQu3QQ
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/e874d5d9-8ec5-4c8e-a44d-25047539dcf0)

### 5. Completion of Fine-Tuning
```
$ openai api completions.create -m ada:ft-personal-2023-11-22-07-16-27 -p <YOUR_PROMPT>
```

![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/4121da5f-36f1-4a37-8f7b-c77b8e184291)


## Step 2: Testing the Fine Tuned Model

Test the fine-tuned model using the provided Python code.

**Result**

![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/afbf0da1-76a1-4102-be15-1c992cd4baed)

![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/921a4c42-d066-4917-9210-3a9eb575c037)
