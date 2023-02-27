import yaml

def get_yaml_data(yaml_file):
    with open(yaml_file,'r',encoding='utf-8')as file:
        file_data=file.read()
    data = yaml.safe_load(file_data)
    return data



