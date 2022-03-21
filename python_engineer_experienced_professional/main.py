import json
import os
from genson import SchemaBuilder



def schema(input_path, filename):
    
    current_path= os.getcwd()
    schema_path= current_path+'/schema'    
    builder = SchemaBuilder()

    with open(input_path, 'r') as f:
        datastore = json.load(f)
        builder.add_object(datastore)

    schema= builder.to_schema()

    os.chdir(schema_path)
    out_file = open(filename+".json", "w")
    json.dump(schema, out_file, indent = 2)

    out_file.close()

data= 'data\data_1.json'

schema(data, 'hello')