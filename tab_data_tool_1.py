#!/usr/bin/python

import re
import os


# *get one standard attribute list and a condensed standard attribute list in which
# *all the attributes contains no special characters


# std_attr_lst = []
# condensed_std_attr_lst = []
# line = '1'
# lst_path = r'/Users/alexhex/Scripts/Py_Tab_Data/Attributes_List.txt'
# lst_in = open(lst_path, 'r')
# while(line):
#     line = lst_in.readline()
#     line = line.strip()
#     std_attr_lst.append(line)
#     line = re.sub('\W', '', line)
#     condensed_std_attr_lst.append(line)
# lst_in.close()


# generate an attributes list for each type or category of packer


# Define the common groups of attributes
std_attr_lst = [
	'ACTIVE FLOW WETTED MATERIAL - YIELD STRENGTH (KSI)',
	'APPROXIMATE WEIGHT (LBS)',
	'BORE I.D. (IN)',
	'CASING I.D. MAX.',
	'CASING I.D. MIN.',
	'CASING SIZE (IN)',
	'CASING WEIGHT RANGE (PPF)',
	'CERTIFICATION STATUS',
	'CONFIGURATION',
	'CONTROL LINE SET',
	'CONVEYANCE METHOD',
	'DIFFERENTIAL PRESSURE RATING - ACROSS SEALS (PSI)',
	'DIFFERENTIAL PRESSURE RATING (PSI)',
	'DIFFERENTIAL RATING ISOLATED (PSI):',
	'DIFFERENTIAL RATING PLUGGED (PSI)',
	'DIFFERENTIAL RATING UNPLUGGED (PSI)',
	'EXTERNAL WORKING PRESSURE (PSI) - AT SPECIFIED TEMP (F)',
	'EXTERNAL WORKING PRESSURE (PSI) - EOEC AT SPECIFIED TEMP (F)',
	'FEED THROUGH',
	'FITS PACKING BORE I.D. (IN)',
	'H2S SERVICE',
	'HYDRAULIC RELEASE PRESSURE (PSI)',
	'I.D. - DRIFT (IN)',
	'I.D. - DRIFT PRIMARY (IN)',
	'I.D. - DRIFT SECONDARY (IN)',
	'I.D. - MIN. (IN)',
	'I.D. - PRIMARY (IN)',
	'I.D. - PRIMARY MIN (IN)',
	'I.D. - REF. (IN)',
	'I.D. - SECONDARY (IN)',
	'I.D. - SECONDARY MIN (IN)',
	'I.D. (IN)',
	'INTERNAL WORKING PRESSURE (PSI) - AT SPECIFIED TEMP (F)',
	'INTERNAL WORKING PRESSURE (PSI) - EOEC AT SPECIFIED TEMP (F)',
	'ISO QUALIFIED CASING ID',
	'JAY TYPE',
	'LATCH ANCHOR RATING COMPRESSION (LBS) - AT SPECIFIED TEMP (F)',
	'LATCH ANCHOR RATING TENSION (LBS) - AT SPECIFIED TEMP (F)',
	'LOWER THREAD CONNECTING - SIZE (IN), WT (PPF), TYPE, CONFIG',
	'LOWER THREAD SECONDARY - SIZE (IN), WT (PPF), TYPE, CONFIG',
	'MAKE-UP LENGTH (IN)',
	'MAKE-UP LENGTH PRIMARY (IN)',
	'MAKE-UP LENGTH SECONDARY (IN)',
	'MAKE-UP/STACK-OUT LENGTH (IN)',
	'MATERIAL/ELASTOMERS',
	'MATERIAL/ELEMENTS',
	'MATERIAL/NON FLOW WETTED',
	'MATERIAL/O-RING(S)',
	'MAX. CIRCULATION RATE PAST PACKER (BPM)',
	'MAX. DELTA T (F)',
    'MAX. HYDROSTATIC PRESSURE (PSI) - AT SPECIFIED TEMP (F)',
	'MAX. RIH RATE (FPM)',
	'MAX. WORKING TEMPERATURE (DEG.F)',
	'MIN. WORKING TEMPERATURE (DEG.F)',
	'NO-GO LOCATOR RATING COMPRESSION (LBS) - AT SPECIFIED TEMP (F)',
	'O.D. - DRAG BLOCK EXPANDED (IN)',
	'O.D. - MAX. (IN)',
	'O.D. (IN)',
	'OFFSET (IN)',
	'OPERATIONS MANUAL',
	'OVERALL LENGTH (IN)',
	'PACKER CONNECTING THREAD - SIZE (IN), PITCH (INTEGER), TYPE',
	'PACKER ENVELOPE POINTS ISOLATED - LOAD (LBS)',
	'PACKER ENVELOPE POINTS ISOLATED - PRESSURE (PSI)',
	'PACKER ENVELOPE POINTS PLUGGED - BELOW - LOAD (LBS)',
	'PACKER ENVELOPE POINTS PLUGGED - BELOW - PRESSURE (PSI)',
	'PACKER ENVELOPE POINTS UNPLUGGED - LOAD (LBS)',
	'PACKER ENVELOPE POINTS UNPLUGGED - PRESSURE (PSI)',
	'QUALITY CONTROL GRADE',
	'QUALITY CONTROL PLAN - QCP',
	'RELEASE STUD (LBS)',
	'RETRIEVAL METHOD',
	'SEAL DIAMETER (IN)',
	'SEAL MAKE UP LENGTH (IN)',
	'SERVICE NACE (YES/NO)',
	'SETTING DIFFERENTIAL PRESSURE - RECOMMENDED (MIN)(PSI)',
	'SETTING FORCE (LB)',
	'SETTING MANDREL (PRIMARY/SECONDARY)',
	'SETTING METHOD',
	'SETTING PRESSURE 1ST SHEAR (PSI)',
	'SETTING PRESSURE SLIP ENGAGEMENT (PSI)',
	'SHEAR RELEASE FORCE (LB)',
	'SNAP LATCH LOCATOR RATING COMPRESSION (LBS) - AT SPECIFIED TEMP (F)',
	'TENSILE STRENGTH (LBS) - AT SPECIFIED TEMP (F)',
	'TENSILE STRENGTH (LBS) - EOEC AT SPECIFIED TEMP (F)',
	'TORQUE CAPACITY - EOEC (FT-LBS)',
	'TORQUE SHEAR VALUE/RIGHT HAND TORQUE RELEASE (FT-LBS)',
	'UPPER BORE I.D. (IN)',
	'UPPER THREAD CONNECTING - SIZE (IN), WT (PPF), TYPE, CONFIG',
	'UPPER THREAD SECONDARY - SIZE (IN), WT (PPF), TYPE, CONFIG'
]


# condensed_std_attr_lst = [re.sub('\W', '', elem) for elem in std_attr_lst]

packer_tubing = [3,3,0,0,0,3,3,3,0,2,3,0,3,0,0,0,0,3,2,0,2,0,3,2,2,3,2,2,0,2,2,
                 3,0,3,0,2,0,0,3,2,3,2,2,0,3,3,3,3,0,0,2,0,3,3,0,2,3,3,2,3,3,0,
                 0,0,0,0,0,0,0,3,0,3,3,0,3,3,0,2,3,3,3,2,0,0,3,3,2,2,3,2]

packer_seal_bore = [3,3,3,0,0,3,3,3,0,0,3,0,3,0,0,0,0,3,0,0,0,0,3,0,0,3,0,0,0,0,
                    0,3,0,3,0,0,0,0,3,0,3,0,0,0,3,3,3,3,0,0,0,0,3,3,0,0,3,3,0,3,
                    3,0,0,0,0,0,0,0,0,3,0,3,3,0,3,2,3,0,3,0,0,2,0,0,3,3,2,2,3,0]

iso_attr = [3,3,0,0,0,3,3,3,0,0,3,0,3,3,3,3,0,0,0,0,2,0,3,0,0,0,0,0,0,0,0,0,0,
            0,3,0,0,0,3,0,0,0,0,0,0,3,3,3,3,3,0,3,3,3,0,0,3,0,0,3,3,0,3,3,3,3,
            3,3,3,0,0,3,0,0,3,3,0,0,3,0,0,0,0,0,0,0,0,0,3,0]


def type_attr(typ):
    attr_lst_ncssry = []
    attr_lst_opnl = []
    for i in range(len(packer_tubing)):
        if typ[i] == 3:
            attr_lst_ncssry.append(std_attr_lst[i])
        elif typ[i] == 2:
            attr_lst_opnl.append(std_attr_lst[i])
        else:
            pass
    return [attr_lst_ncssry, attr_lst_opnl]

def choose_type(choice):
    packer_type = ''
    iso_type = ''
    attr_choice = []
    [packer_type, iso_type] = choice.split(',', 1)
    print packer_type, iso_type
    if packer_type == 'pt' and iso_attr == 'n':
        attr_choice = packer_tubing
    elif packer_type == 'ps' and iso_attr == 'n':
        attr_choice = packer_seal_bore
    elif packer_type == 'pt' and iso_type == 'y':
        for i in range(len(packer_tubing)):
            if packer_tubing[i] > iso_attr[i]:
                attr_choice.append(packer_tubing[i])
            else:
                attr_choice.append(iso_attr[i])
    elif packer_type == 'ps' and iso_attr == 'y':
        print 'here we go'
        for i in range(len(packer_seal_bore)):
            if packer_seal_bore[i] > iso_attr[i]:
                attr_choice.append(packer_seal_bore[i])
            else:
                attr_choice.append(iso_attr[i])
    else:
        pass
    print attr_choice
    return attr_choice

print type_attr(choose_type('ps,y'))
# test = 'ps,y'
# print test.split(',', 1)

# To generate a reference packer tab data dictionary

def read_ref_tab_data(filepath):
    ref_in = open(filepath, 'r')
    lines = ref_in.readlines()
    ref_in.close()
    ref_tab_data = {}
    ref_attr = []
    attr = ''
    val = ''
    for sen in lines:
        [att, val] = [elem.strip() for elem in sen.split('=', 1)]
        ref_attr.append(att)
        ref_tab_data[att] = val
    return ref_tab_data



path = r'/Users/alexhex/Scripts/Py_Tab_Data/in.txt'
ref_items = read_ref_tab_data(path).items()
ref_items.sort()
for key, value in ref_items:
    print key, value



# Generate a blank standard new packer tab data dictionary
choice = raw_input('What is the type of packer, and Is it ISO qualified?')
