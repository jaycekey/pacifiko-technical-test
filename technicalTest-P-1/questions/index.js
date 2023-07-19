import fetch from 'node-fetch'

function getHighSalaryEmployees() {
  return fetch("http://dummy.restapiexample.com/api/v1/employees")
    .then((res) => res.json())
    .then((data) => {
      const employees = data?.data;
      const highSalaryEmployees = employees.filter(
        (employee) => employee.employee_salary > 300000
      );
      return highSalaryEmployees;
    });
}

getHighSalaryEmployees()
  .then((highSalaryEmployees) => {
    highSalaryEmployees.forEach(employee => {
      if(!employee?.employee_salary > 300000){
        console.log("No se cumple la condición");
      }
    })
  })
  .catch((error) => console.error(error));