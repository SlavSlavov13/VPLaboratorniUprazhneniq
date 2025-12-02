import json

python_obj = {
	"name": "Ivan",
	"age": 25,
	"city": "Sofia",
	"is_student": True
}

json_data = json.dumps(python_obj, indent=4)

print("JSON данни:")
print(json_data)