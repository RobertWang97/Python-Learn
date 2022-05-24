aa = {"companyCode": {"type": "Select", "length": "2"},
              "enablementProcessId": {"type": "Select", "length": "4"},
              "businessTemplateId": {"type": "Select", "length": "16"},
              "licenseAgreementTypeId": {"type": "Select", "length": "2"},
              "shortName": {}, "longName": {}, "programTypeId": {"type": "Select", "length": "4"},
              "swProdBrandCode": {"type": "Select", "length": "13"}, "version": {},
              "release": {}, "modification": {}, "scheduleName": {},
              "rfaNumber": {}, "announcementDate": {}, "genAvailDateLicenseDsw": {}, "electronicAvailDate": {},
              "physicalAvailDate": {}}
# print(aa.keys())
# aa.has_key("222")
for key, value in aa.items():
    # print(value)
    # print(item)
    if "type" in value.keys():
        print(value["type"])