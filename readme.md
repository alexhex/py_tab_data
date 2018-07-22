# Tab Data Tool Logic

## Operating Logic

1. Select the packer type;
2. Paste the reference tab data;
3. Generate a table with 3 columns: std. attr. | ref. val | new val |
4. Overwrite the values to be changed;
5. Define the output format; 
6. Pop a new window with defined format;

## Program Logic

1. The full standard tab data is defined at Attributes_List.txt, which contains all the attributes defined for packer and bridge plugs;
2. The specific packer attributes list is defined at "\<packer type\>.txt", for example MRP.txt lists the attributes for MRP packer;
3. Program "import_and_compare.py" could check the correctness of the packer.txt file;
4. The tab_data_tool.py would use the packer type list file to establish the format;