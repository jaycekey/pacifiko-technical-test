<?php

$API_URL = "https://dummy.restapiexample.com/api/v1";

// Get all employees
function getEmployee() {
  global $API_URL;
  $response = file_get_contents($API_URL."/employees");
  $data = json_decode($response);
  print_r($data);
}

// Get employee by id
function getEmployeeById($id) {
  global $API_URL;
  $response = file_get_contents($API_URL."/employee/".$id);
  $data = json_decode($response);
  print_r($data);
}

// Create employee
function createEmployee($employeeData) {
  global $API_URL;
  $options = array(
    "http" => array(
      "method" => "POST",
      "header" => "Content-Type: application/json\r\n" .
                  "Accept: */*\r\n",
      "content" => json_encode($employeeData)
    )
  );
  $context = stream_context_create($options);
  $response = file_get_contents($API_URL."/create", false, $context);
  $data = json_decode($response);
  print_r($data);
}

$newEmployee = array(
  "employee_name" => "Carlos Enrique",
  "employee_salary" => 10000,
  "employee_age" => 21,
  "profile_image" => ""
);

# getEmployee();
# getEmployeeById(1);
# createEmployee($newEmployee);

?>