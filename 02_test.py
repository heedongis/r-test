from typing import List, Union


def get_elements(data: dict, element_name: str) -> List[List[Union[int, str]]]:
    paths = []
    def traverse(data, path):
        if isinstance(data, list):
            for i, item in enumerate(data):
                traverse(item, path + [i])
        elif isinstance(data, dict):
            for key, value in data.items():
                if key == "NAME" and value == element_name:
                    paths.append(path)
                traverse(value, path + [key])
    traverse(data, [])
    return paths


data = {
   "children": [
     [
       "paragraph",
       {
         "numbering": "#none",
         "indent-level": 0,
         "children": [
           [
             "text",
             {
               "value": "뤼이드와 함께 글로벌로 성장하고 싶은 인재를 모시고 있습니다.",
               "weight": "#w400"
             }
           ]
         ]
       }
     ]
   ]
 }

element_name = "text"

# result = get_elements(data, element_name)
result2 = get_elements(data, element_name)

print(result2)