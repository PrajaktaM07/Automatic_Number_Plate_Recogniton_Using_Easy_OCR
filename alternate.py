from easyocr import Reader
import cv2
import matplotlib.pyplot as plt
import os
import requests
from pprint import pprint

file_to_number = {
    "Cars301.png": "G526 JHD",
    "Cars302.png" :"KL 01 CC 50",
    "Cars303.png" :"KL 54 A 2670",
    "Cars304.png" :"HNYCHIL3",
    "Cars305.png" :"SGQ51 JU",
    "Cars306.png" :"LAWYER",
    "Cars307.png" :"M 90 60 90 K",
    "Cars308.png" :"HR 26 BC 5514",
    "Cars309.png" :"EAB 0001",
    "Cars310.png" :"4 GET OIL",
    "Cars311.png" :"TN 21 AT 8349",
    "Cars312.png" :"PU18 BES",
    "Cars313.png" :"NBEYOND",
    "Cars314.png" :"6PIV728",
    "Cars315.png" :"J98257",
    "Cars316.png" :"MH 02 BB 2",
    "Cars317.png" :"HR 26 BC 5514",
    "Cars318.png" :"ALR 486",
    "Cars319.png" :"FALLYOU",
    "Cars320.png" :"KA 09 MA 2662",
    "Cars321.png" :"LOL OIL",
    "Cars322.png" :"700V",
    "Cars323.png" :"TN 99 F 2378",
    "Cars324.png" :"VI2 LAF",
    "Cars325.png" :"XXX",
    "Cars326.png" :"DL 8C X 4850",
    "Cars327.png" :"PG MN 112",
    "Cars328.png" :"IM4U 555",
    "Cars329.png" :"16M",
    "Cars330.png" :"",
    "Cars331.png" :"HR 26 CB 1900",
    "Cars332.png" :"DZI7 YXR",
    "Cars333.png" :"MH 20 EJ 0364",
    "Cars334.png" :"E8 OLA",
    "Cars335.png" :"NOTACOP",
    "Cars336.png" :"DL 8C X 4850",
    "Cars346.png" :"KA 03 AB 3380",
    "Cars365.png" :"TN 21 BZ 0768",
    "Cars366.png" :"MH 20 BQ 20",
    "Cars372.png" :"HR 26 CE 1485",
    "Cars373.png" :"TN 21 BC 6225",
    "Cars379.png" :"MH 14 GN 9239",
    "Cars386.png" :"AB 44 887",
    "Cars387.png" :"HR 26 AZ 5927",
    "Cars415.png" :"MH 12 NE 8922",
    "Cars424.png" :"KA 03 MG 2784",
    "Cars432.png" :"DL49 AK49",
    "Cars433.png" :"MH 46 Z 8264",
    "Cars434.png" :"MH 46 BE 5892",
    "Cars435.png" :"MH 46 Z 8264",
    "Cars437.png" :"KA 02 MP 9657",
    "Cars438.png" :"KL 41 B6016",
    "Cars439.png" :"MH 46 BZ 4206",
    "Cars600.png" :"MH 46 BE 9851",
    "Cars601.jpeg" :"MH 46 W 3204",
    "Cars603.jpeg" :"MH 10 AG 2095",
    "Cars604.jpeg" :"MH 46 BV 2359",
    "Cars605.jpeg" :"MH 46 AL 5260",
    "Cars606.jpeg" :"MH 12 NE 3656",
    "Cars607.jpeg" :"MH4 46 BV 2359",
    "Cars608.jpeg" :"MH 43 A 9658",
    "Cars609.jpeg" :"MH 46 BQ 2232",
    "Cars610.jpeg" :"MH 46 N 8653",
    "Cars611.jpeg" :"RJ13 CC 0951",
    "Cars612.jpeg" :"KA 02 MP 9657",
    "Cars613.jpeg" :"DL 9C AQ 0982",
    "Cars614.jpeg" :"GJ 07 BR 1336",
    "Cars615.jpeg" :"WB 06 F 5977",
}

token = '7973d5e87688470071665d71849f8a58cd599c3e'

def get_np_text(filename):
    # pip install requests 
    regions = ['in'] # Change to your country
    # with open(filename, 'rb') as fp:
    #     response = requests.post(
    #         'https://api.platerecognizer.com/v1/plate-reader/',
    #         data=dict(regions=regions),  # Optional
    #         files=dict(upload=fp),
    #         headers={'Authorization': 'Token ' + token})
    # pprint(response.json())
    # return response.json()
    dummy_response = {
            'camera_id': None,
            'filename': '0719_BcbhL_1.jpg',
            'processing_time': 59.075,
            'results': [
                {
                    'box': {'xmax': 865, 'xmin': 341, 'ymax': 1524, 'ymin': 1414},
                    'candidates': [{'plate': 'mh46bk4291', 'score': 0.904}],
                    'dscore': 0.894,
                    'plate': 'mh46bk4291',
                    'region': {'code': 'in', 'score': 0.879},
                    'score': 0.904,
                    'vehicle': {
                        'box': {
                            'xmax': 1200,   
                            'xmin': 0,
                            'ymax': 1593,
                            'ymin': 460
                        },
                        'score': 0.647,
                        'type': 'Sedan'
                    }
                }
            ],
            'timestamp': '2023-03-26T07:19:35.474212Z',
            'version': 1
        }
    return dummy_response
        


def get_car_details(number):
    url = "https://vehicle-rc-verification.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_rc_basic"
    payload = {
        "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
        "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
        "data": {"rc_number": number}
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "91bdf66265msh281f2e86c0f57cap11446fjsnf3bffef2e0a6",
        "X-RapidAPI-Host": "vehicle-rc-verification.p.rapidapi.com"
    }
    # response = requests.request("POST", url, json=payload, headers=headers)
    # pprint(response.json())
    # print(response.text)
    dummy_details_repsonse = {
            'action': 'verify_with_source',
            'completed_at': '2023-03-26T13:33:15+05:30',
            'created_at': '2023-03-26T13:33:15+05:30',
            'group_id': '8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e',
            'request_id': 'bfd465a8-2f17-49fa-a0d5-394b3496e0e3',
            'result': {
                'extraction_output': {
                        'avg_gross_vehicle_weight': '1315',
                        'axle_configuration': None,
                        'chassis_number': 'MBHCZC63SJK2XXXXX',
                        'color': None,
                        'emission_norms': 'BHARAT STAGE IV',
                        'engine_number': None,
                        'fitness_upto': '2034-01-29',
                        'fuel_type': 'PETROL',
                        'insurance_details': None,
                        'insurance_validity': '2024-01-23',
                        'maker_model': 'MARUTI SWIFT ZXI+',
                        'manufacturer': 'MARUTI SUZUKI INDIA LTD',
                        'mv_tax_upto': None,
                        'owner_name': 'PRABODH NARAYAN TANDON',
                        'owner_number': None,
                        'permit_issue_date': None,
                        'permit_number': None,
                        'permit_type': None,
                        'permit_validity': None,
                        'puc_number_upto': '2024-03-09',
                        'registration_date': '2019-01-30',
                        'registration_number': 'MH46BK4291',
                        'rto_name': None,
                        'status': 'id_found',
                        'unladen_weight': '880',
                        'vehicle_class': 'LMV',
                        'vehicle_financier': None
                    }
                },
            'status': 'completed',
            'task_id': '74f4c926-250c-43ca-9c53-453e87ceacd1',
            'type': 'ind_rc_basic'
        }
    return dummy_details_repsonse

def read_text(filename):
    try:
        # load the image and resize it
        print("Starting with :", filename)
        image = cv2.imread(filename)
        image = cv2.resize(image, (800, 600))

        # convert the input image to grayscale,
        # blur it, and detect the edges 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        blur = cv2.GaussianBlur(gray, (5,5), 0) 
        edged = cv2.Canny(blur, 10, 200) 
        # cv2.imshow('Canny', edged)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # find the contours, sort them, and keep only the 5 largest ones
        contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]

        # loop over the contours
        for c in contours:
            # approximate each contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # if the contour has 4 points, we can say
            # that we have found our license plate
            # print(f"peri - {peri}, approx - {approx}, len - {len(approx)}")
            if len(approx) >= 4:
                n_plate_cnt = approx
                break        

        # get the bounding box of the contour and 
        # extract the license plate from the image
        (x, y, w, h) = cv2.boundingRect(n_plate_cnt)
        license_plate = gray[y:y + h, x:x + w]

        # initialize the reader object
        reader = Reader(['en'])
        # detect the text from the license plate
        detection = reader.readtext(license_plate)

        if len(detection) == 0:
            # if the text couldn't be read, show a custom message
            text = "Impossible to read the text from the license plate"
            cv2.putText(image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 3)
            # cv2.imshow('Image', image)
            # plt.imshow('Image', image)
            # cv2.waitKey(0)
        else:
            # draw the contour and write the detected text on the image
            cv2.drawContours(image, [n_plate_cnt], -1, (0, 255, 0), 3)
            text = f"{detection[0][1]} {detection[0][2] * 100:.2f}%"
            print("Plate text:", text, "\n")
            # cv2.putText(image, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            # display the license plate and the output image
            # cv2.imshow('license plate', license_plate)
            # cv2.imshow('Image', image)
            # cv2.waitKey(0)

    except:
        print('Temporary error')
    finally:
        # api call here
        print("Will call api here for file_name:", filename)
        # get_np_text(filename)
        plate_details = get_np_text(filename)
        plate = plate_details['results'][0]['plate']
        print("plate:", plate)
        details = get_car_details(plate)
        return details

