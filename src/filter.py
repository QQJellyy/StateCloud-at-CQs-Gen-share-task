import json, os, jsonlines

loc = 'output/test/unfiltered'
dst = 'output/test'

pre = [
    'challenges one of the arguments:',
    'that meets your criteria:',
    'arguments in the text:',
    'challenges the argument presented:',
    'meets your requirements:',
    'uestion:**  \n',
    'argument in the provided text:',
    'argument in the text:',
    'argument:\n\n',
    'speech:\n\n',
    'critical question:\n\n',
    'an argument could be:\n\n',
    'argument in the original text:\n\n',
]
post = [
    '\n_user',
    '\n_system',
    '/assistant',
    'Reasoning:',
    'Explanation:',
    'This question',
    '\n\nThis question ',
]

for root,_,files in os.walk(loc):
    for file in files:
        if not file.endswith('json'):
            continue

        data = json.load(open(root+'/'+file,'r'))
        model = file.split('.')[0]

        for abbr, summ in data.items():
            output = summ['model_output'] if 'model_output' in summ else ''
            for p in pre:
                output = output.split(p)[-1]
            for p in post:
                output = output.split(p)[0]
            summ['cqs'] = [{
                "id":summ['intervention_id']+'_'+model,
                "cq":output.strip('\n').strip(' ').strip('*').strip('#').strip('\n').strip(' ')
            }]*3
            if 'model_output' in summ:
                summ.pop('model_output')

        out = root.replace(loc,dst)
        os.makedirs(out,exist_ok=True)
        json.dump(data,open(out+'/'+file,'w'),indent=2,ensure_ascii=False)
