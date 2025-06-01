import requests
import logging,os,sys
import argparse,json
from tqdm import tqdm
from prompt_template import make_prompt

def get_logger(name):
    r"""
    Gets a standard logger with a stream hander to stdout.
    """
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%m/%d/%Y %H:%M:%S"
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


logger = get_logger("QWen")
        
def post(url, prompt):
    data = {
        "Messages": prompt,
        # "Images": data,
        # "TopK":5,
        # "TopP":0.5,
        # "Temperature":0.6,
        # "Seed":100
    }
    resp = requests.post(url, json=data)

    if resp.status_code != 200:
        return False, resp
    else:
        print(resp.json())
        return True, resp.json()['result']['Output']
    
def json_load(in_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def main(model_path, testfile, prompt_type, output_file):

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            results = json.load(f)
    except:
        results = json_load(testfile)
    data_length = len(results)
    logger.info("data_length: {} ".format(data_length))

    for i,item in tqdm(results.items()):
        if "model_output" in results[i] and len(results[i]['model_output']):
                continue

        messages = [
            {"role": "system", "content": "You are a helpful assistant with critical thinking skills."},
            {"role": "user", "content": make_prompt(item, prompt_type)}
        ]

        status,response = post(model_path,messages)

        if status:
            logger.info("question: {}".format(item['intervention']))
            logger.info("model_output: {}".format(response))

            results[i]["raw_model_output"] = response
            results[i]["model_output"] = response.split('</think>')[-1]
            logger.info("-" * 50)

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            
            # break

    logger.info(f"***********Finished Infer************")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",'-i', type=str, default='')
    parser.add_argument("--output",'-o', type=str, default='')
    parser.add_argument("--model_path",'-m', type=str, default='')
    parser.add_argument("--prompt_type",'-p', type=str, default='zero_shot')

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    output = args.output + '/api_' + args.model_path.split('9080/')[-1].split('/common')[0] + '.json'
    main(args.model_path, args.input, args.prompt_type, output)
