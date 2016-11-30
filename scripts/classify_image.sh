# train
curl -X POST -F "_positive_examples=@train/c0_positive.zip" -F "negative_examples=@train/c1_positive.zip" -F "name=drivers" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20"
# output
{
    "classifier_id": "drivers_1130412468",
    "name": "drivers",
    "owner": "ff726070-d51f-4f2a-97be-5fb5a39c4b21",
    "status": "training",
    "created": "2016-11-30T18:16:10.547Z",
    "classes": [{"class": "positive_ex"}]
}

# training status
curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20"
# output
{"classifiers": [{
    "classifier_id": "drivers_1130412468",
    "name": "drivers",
    "status": "ready"
}]}

curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/drivers_1130412468?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20"
# output
{
    "classifier_id": "drivers_1130412468",
    "name": "drivers",
    "owner": "ff726070-d51f-4f2a-97be-5fb5a39c4b21",
    "status": "ready",
    "created": "2016-11-30T18:16:10.547Z",
    "classes": [{"class": "positive_ex"}]
}

# classify
curl -X POST -F "images_file=@test/img_22.jpg" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20"

curl -X POST -F "images_file=@test/img_22.jpg" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20&classifier_ids=drivers_1130412468"

curl -X POST -F "images_file=@test/img_25.jpg" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=ed36255294436d2845dacc344c79e26f813220a8&version=2016-05-20&classifier_ids=drivers_1130412468"
