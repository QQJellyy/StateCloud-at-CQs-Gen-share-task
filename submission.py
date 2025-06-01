import json, os

locs = [
    'output/test/few_shot/api_vllm-huize2p-72b-awq-int4-hf-chat.json',
    'output/test/sequential_2/api_vllm-huize2p-72b-awq-int4-hf-chat.json',
    'output/test/sequential_3/api_vllm-huize2p-72b-awq-int4-hf-chat.json',
    ]
dst = 'output/test/submisstion'

files = [
    os.path.split(loc)[-1][:-5] for loc in locs
]
datas = [
    json.load(open(loc,'r')) for loc in locs
]
for k in datas[0]:
    datas[0][k]['cqs'][1] = datas[1][k]['cqs'][1]
    datas[0][k]['cqs'][2] = datas[2][k]['cqs'][2]
    datas[0][k]['cqs'][0]['cq'] = datas[0][k]['cqs'][0]['cq'].strip('"')
    datas[0][k]['cqs'][1]['cq'] = datas[0][k]['cqs'][1]['cq'].strip('"')
    datas[0][k]['cqs'][2]['cq'] = datas[0][k]['cqs'][2]['cq'].strip('"')
    datas[0][k].pop('raw_model_output')
    datas[0][k].pop('schemes')
    if 'model_output' in datas[0][k]:
        datas[0][k].pop('model_output')

os.makedirs(dst,exist_ok=True)
json.dump(datas[0],open(dst+'/'+'StateCloud_test_run1.json','w'),indent=2,ensure_ascii=False)



locs = [
    'output/test/few_shot/api_vllm-huize2p-72b-awq-int4-hf-chat.json',
    'output/test/few_shot/Qwen2.5-7B-Instruct.json',
    'output/test/few_shot/Qwen2.5-32B-Instruct.json',
    ]
dst = 'output/test/few_shot_cmb'

files = [
    os.path.split(loc)[-1][:-5] for loc in locs
]
datas = [
    json.load(open(loc,'r')) for loc in locs
]
for k in datas[0]:
    datas[0][k]['cqs'][1] = datas[1][k]['cqs'][1]
    datas[0][k]['cqs'][2] = datas[2][k]['cqs'][2]
    datas[0][k]['cqs'][0]['cq'] = datas[0][k]['cqs'][0]['cq'].strip('"')
    datas[0][k]['cqs'][1]['cq'] = datas[0][k]['cqs'][1]['cq'].strip('"')
    datas[0][k]['cqs'][2]['cq'] = datas[0][k]['cqs'][2]['cq'].strip('"')
    datas[0][k].pop('raw_model_output')
    datas[0][k].pop('schemes')
    if 'model_output' in datas[0][k]:
        datas[0][k].pop('model_output')

os.makedirs(dst,exist_ok=True)
json.dump(datas[0],open(dst+'/'+'StateCloud_test_run2.json','w'),indent=2,ensure_ascii=False)



locs = [
    'output/test/few_shot/api_vllm-huize2p-72b-awq-int4-hf-chat.json',
    'output/test/few_shot/api_vllm-qwq-32b-awq.json',
    'output/test/few_shot/api_vllm-deepseek-r1.json',
    ]
dst = 'output/test/few_shot_cmb'

files = [
    os.path.split(loc)[-1][:-5] for loc in locs
]
datas = [
    json.load(open(loc,'r')) for loc in locs
]
for k in datas[0]:
    datas[0][k]['cqs'][1] = datas[1][k]['cqs'][1]
    datas[0][k]['cqs'][2] = datas[2][k]['cqs'][2]
    datas[0][k]['cqs'][0]['cq'] = datas[0][k]['cqs'][0]['cq'].strip('"')
    datas[0][k]['cqs'][1]['cq'] = datas[0][k]['cqs'][1]['cq'].strip('"')
    datas[0][k]['cqs'][2]['cq'] = datas[0][k]['cqs'][2]['cq'].strip('"')
    datas[0][k].pop('raw_model_output')
    datas[0][k].pop('schemes')
    if 'model_output' in datas[0][k]:
        datas[0][k].pop('model_output')

os.makedirs(dst,exist_ok=True)
json.dump(datas[0],open(dst+'/'+'StateCloud_test_run3.json','w'),indent=2,ensure_ascii=False)