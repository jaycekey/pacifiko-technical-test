import requests

API_URL = "https://dummy.restapiexample.com/api/v1"

# The server returns 406 error if the User-Agent is python (python-requests/2.21.0) 
# therefore, in this line of code I change the user agent, this to change the identity of the client
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}

# Get all employees
def get_employees():
  try:
    response = requests.get(f"{API_URL}/employees", headers=headers)
    if response.status_code == 200:
      data = response.json()
      print(data)
    else:
      print(response.status_code)
  except requests.exceptions.RequestException as err:
    print(f"Error al obtener la lista de empleados:")

# Get employee by id
def get_employee_by_id(id):
  try:
    response = requests.get(f"{API_URL}/employee/{id}", headers=headers)
    if response.status_code == 200:
      data = response.json()
      print(data)
    else:
      print(response.status_code)
  except requests.exceptions.RequestException as err:
    print(f"Error al obtener la lista de empleados: {err}")

# Create employee
def create_employee(employee_data):
  try:
    post_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1', 'Content-Type': 'application/json', 'Accept': "*/*"}
    response = requests.post(f"{API_URL}/create", json=employee_data, headers=post_headers)
    if response.status_code == 200:
      data = response.json()
      print(data)
    else:
      print(response)
  except requests.exceptions.RequestException as err:
    print(f"Error al crear el nuevo empleado: {err}")


new_employee = {
  "employee_name": "Carlos Enriquez",
  "employee_salary": 30000,
  "employee_age": 21,
  "profile_image": "",
}

#get_employees()
#get_employee_by_id(1)
#create_employee(new_employee)

