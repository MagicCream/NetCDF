from pymongo import MongoClient
from netCDF4 import Dataset
from numpy import float32

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    filename = 'test_hgroups.nc'
    db = client[filename.split('.')[0]]
    dataset1 = Dataset(filename)
    dimensions = dataset1.dimensions.keys()
    variables_name = dataset1.variables.keys()
    print(dimensions)
    for item in variables_name:
        print(dataset1.variables[item])
        variable = dataset1.variables[item]
        print(dataset1.variables[item].dimensions)
        collection = db[item]
        print(collection)
        data = {
            'values': variable[:].tolist(),
            'dimensions':list(variable.dimensions),
            'name': variable.name
        }
        for attr in variable.ncattrs():
            if attr not in data.keys():
                if isinstance(variable.getncattr(attr),float32):
                    data[attr] = float(variable.getncattr(attr))
                else:
                    data[attr] = variable.getncattr(attr)

        post_id = collection.insert_one(data)
        # for dim in dataset1.variables[item].dimensions:
        #     data_dim = dataset1.variables[dim][:]
        #     print(data_dim)


    # print(dataset1.dimensions.keys())
    # # print(dataset1.dimensions['DATETIME'])
    # print(dataset1.variables.keys())
    # # print(dataset1.variables['UTC_time'])
    # print(dataset1.variables['UTC_time'][:])
    # # print(dataset1)
    # print("-------------------")
    # print(client["testdb"].collection_names())
