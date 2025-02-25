import requests

KEY = '<your_key>'

def get_location(input_str):
    url = "https://restapi.amap.com/v3/geocode/geo"
    params = {
        'address': input_str,
        'key': KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:
        if data['status'] == '1' and len(data['geocodes']) > 0:
            location = data['geocodes'][0]['location'].split(',')
        else:
            return [-1, -1]
    except:
        print(data)
        input()
        return [-1, -1]
    return [float(location[0]), float(location[1])]

if __name__ == "__main__":
    input_str = "北京市 朝阳 定福庄 定福家园1号院"
    print(get_location(input_str))