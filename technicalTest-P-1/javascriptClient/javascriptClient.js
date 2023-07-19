import fetch from "node-fetch";

const API_URL = "https://dummy.restapiexample.com/api/v1";

// Get all employees
const getEmployee = () => {
  fetch(`${API_URL}/employees`)
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
};

// Get employee by id
const getEmployeeById = (id) => {
  fetch(`${API_URL}/employee/${id}`)
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
};

// Post employee
const createEmployee = (employeeData) => {
  fetch(`${API_URL}/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "*/*",
    },
    body: JSON.stringify(employeeData),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
};

const newEmployee = {
  employee_name: "Carlos Enrique",
  employee_salary: 10000,
  employee_age: 21,
  profile_image: "",
};

// getEmployee();
// getEmployeeById(1);
// createEmployee(newEmployee);
