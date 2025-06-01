## Inference  

After completing the parameter configuration (API, input/output paths, prompt type), execute `infer_api.sh`.  

Note: Each inference run generates only 1 CQ (Critical Question). The output JSON file will contain the same 3 CQs for each intervention.  

## Post-processing  

Since the LLM (Large Language Model) may not strictly follow instructions when generating CQs (e.g., it might include phrases like `This is a question that meets your requirements:`), run `src/filter.py` after inference to ensure the output contains only clean CQs.  

## Scoring  
Same as the official GitHub: 

`bash evaluation.sh`  

## Counting Labels by Category  
`python print_score.py`  

## Final Submission of 3 Systems  

Since each inference run generates only 1 CQ, you need to perform inference 3 times and then merge the 3 resulting JSON files:  

`python submission.py`