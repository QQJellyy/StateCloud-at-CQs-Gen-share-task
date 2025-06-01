import os,json

loc = 'output/validation/few_shot'

results = {}

for root,_,files in os.walk(loc):
    exp = os.path.basename(root)
    if 'test' in exp:
        continue

    results[exp] = {}
    for file in files:
        if 'similarity' in file:
            data = json.load(open(root+'/'+file))

            score = {
                'Useful':0,
                'not_able_to_evaluate':0,
                'Unhelpful':0,
                'Invalid':0,
            }

            for k,v in data.items():
                for cq in v['cqs']:
                    score[cq['label']] += 1

            if 'cmb' in exp:
                results[exp][file[:-5]] = ','.join(str(i) for i in [score['Useful'],score['not_able_to_evaluate'],score['Unhelpful'],score['Invalid']])
            else:
                results[exp][file[:-5]] = ','.join(str(i//3) for i in [score['Useful'],score['not_able_to_evaluate'],score['Unhelpful'],score['Invalid']])

print(json.dumps(results,indent=2))
