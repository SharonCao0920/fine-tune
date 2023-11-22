# Fine Tune in Practice
## 1.	Export your OpenAI API key:
```
$ export OPENAI_API_KEY="<OPENAI_API_KEY>"
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/d2d19007-6fce-4379-b578-ca97dcdf6a31)

 
## 2.	Create JSONL File
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/83c3bece-0c13-4f39-8fb1-29b7408ebb3a)

 
## 3.	Analyze and Prepare Data
```
$ openai tools fine_tunes.prepare_data -f data.json
```
***Note: May need to install missing packages***
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/eec51a8a-a158-41a0-a9a7-6615ab362778)

* Jsonl file generated
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/38e81670-fd2c-4135-9dc9-53fa3727012f)

	 
## 4.	Fine-Tune the Model
```
$ openai api fine_tunes.create -t "data_prepared.jsonl" -m curie
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/ccbbd6fd-bc85-4ff5-85b0-fec66b265f00)


## 5.	List Fine-Tuned Models
```
$ openai api fine_tunes.list
```
 
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/037526b3-24a5-4042-a5cc-49abc0c923ae)

## 6.	Resume Fine-Tuning (if needed)
```
$ openai api fine_tunes.follow -i ft-eIt0cXubeWlMeLtlJ4Sh7Lml
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/38b70696-40bc-4a05-b9c6-ca2f2f59f5a8)

* Try out model:
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/96a67828-4251-4fd0-877e-30b58f7eabf4)

***Note:
May happen into client disconnected issue. Give it sometime and retry. Job maybe already in queue.***

![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/9148bc19-7096-4ac6-b9c5-eede5a46cab1)

 
[Reference 1](https://community.openai.com/t/stream-interrupted-client-disconnected-while-fine-tuning-a-gpt-3-davinci-model/277694)
[Reference 1](https://community.openai.com/t/stream-interrupted-client-disconnected-during-fine-tunes-follow/70334/23)

## 7.	Use the Fine-Tuned Model
```
$ export FINE_TUNED_MODEL="<FINE_TUNED_MODEL>"
$ openai api completions.create -m $FINE_TUNED_MODEL -p <YOUR_PROMPT>
```
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/a5fa070b-08e0-442c-b099-1b0162a44864)

![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/ddc8cf5e-4a71-48cc-b7b4-5e151bdc973e)

## 8.	Use python
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/fac7cf67-f14e-4285-9d14-0c85cb0e6c6d)

**Result:**
 ![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/9ae89dc5-e44d-4e38-a9d2-cb499c8ef360)

## 9.	Analyze Fine-Tuned Model
![image](https://github.com/SharonCao0920/fine-tune/assets/54694766/06a94045-7bae-4369-938d-edd60b7c80ce)


