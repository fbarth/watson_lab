import json
from os.path import join, dirname, isfile
from watson_developer_cloud import VisualRecognitionV2Beta
from os import listdir

visual_recognition = VisualRecognitionV2Beta(
    username= '3a7d8a48-c06c-4ce0-93f5-b0f5a4f7e0ac',
    password= 'hwuFCmrL2Pr2',
    version='2015-12-02')

#print(json.dumps(visual_recognition.list_classifiers(), indent=2))

mypath = 'test/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print("img,c0,c1,c2,c3,c4,c5,c6,c7,c8,c9")

for file_name in onlyfiles:
    with open(join(dirname(__file__), str(mypath)+str(file_name)), 'rb') as image_file:
        data = visual_recognition.classify(
        image_file,
        #classifier_ids=['c0_1426205524','c1_1671733380','c2_1789520524', \
        #'c3_1854736816','c4_1161856969','c5_1176556357','c6_666729714', \
        #'c7_2023914669','c8_856405232','c9_1312473946'])

        classifier_ids=['c0_v2_1088998397','c1_v2_1990050263','c2_v2_1846033697', \
        'c3_v2_112975662','c4_v2_533463033','c5_v2_2041082738','c6_v2_1326932955', \
        'c7_v2_319929614','c8_v2_1466227715','c9_v2_540192390'])

        #print(data['images'][0]['image'])

        record = {}
        record["name"] = data['images'][0]['image']
        record["c0_v2"] = 0
        record["c1_v2"] = 0
        record["c2_v2"] = 0
        record["c3_v2"] = 0
        record["c4_v2"] = 0
        record["c5_v2"] = 0
        record["c6_v2"] = 0
        record["c7_v2"] = 0
        record["c8_v2"] = 0
        record["c9_v2"] = 0
        try:
            for s in data['images'][0]['scores']:
                record[s['name']] = s['score']
        except:
            pass
        line = record['name']+','+str(record['c0_v2'])+','+ \
        str(record['c1_v2'])+','+str(record['c2_v2'])+','+ \
        str(record['c3_v2'])+','+str(record['c4_v2'])+','+ \
        str(record['c5_v2'])+','+str(record['c6_v2'])+','+ \
        str(record['c7_v2'])+','+str(record['c8_v2'])+','+ \
        str(record['c9_v2'])
        print(line)
