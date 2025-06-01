
python src/evaluation.py \
    --metric similarity \
    --input_path data_splits/validation.json \
    --submission_path output/validation/few_shot/api_vllm-huize2p-72b-awq-int4-hf-chat.json \
    --threshold 0.6 