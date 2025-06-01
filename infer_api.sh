
APIs=(
    "api1" \
    "api2" \
)

for API in "${APIs[@]}"
do
# 推理
python src/infer_api.py \
--i output/validation/sequential_2/api_vllm-huize2p-72b-awq-int4-hf-chat.json \
--o output/validation/sequential_3 \
--m ${API} \
--p sequential_3
done

