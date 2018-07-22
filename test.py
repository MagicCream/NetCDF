from netCDF4 import Dataset
from decimal import Decimal
from netCDF4 import Dimension
def main():
    dataset1 = Dataset('sresa1b_ncar_ccsm3-example.nc')
    # dataset1 = Dataset('test_hgroups.nc')
    print(dataset1.dimensions.keys())
    # print(dataset1.dimensions['lat'])
    print(dataset1.variables.keys())
    # print(dataset1.variables['lat'])
    # print(dataset1.variables['lat'].ncattrs())
    print("-------------------")
    for item in dataset1.variables.values():
        print(item.name)
        print(item.ncattrs())
        print("-------------------")
    # print(dataset1)
    print(dataset1.variables['time'])
    print(dataset1.variables['time'][:])
    # val = dataset1.variables['pr'].getncattr('_FillValue')
    # print(float(val))
    # print(type(val))
    # dataset2 = Dataset('test_echam_spectral-deflated.nc')
    # print(dataset2.dimensions)
    # print(dataset2)
    # print("-------------------")
    # dataset3 = Dataset('test_hgroups.nc')
    # print(dataset3.dimensions)
    # print(dataset3)
    # print("-------------------")

if __name__ == '__main__':
    main()