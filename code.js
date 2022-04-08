


// Using fetch: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
// API: https://randomuser.me/

function createEmployeeElement(fName, lName, email, country, pic) {
    const employeeDiv = document.createElement("div");
    employeeDiv.classList.add("employee");

    const employeePic = document.createElement("img");
    employeePic.src = pic;
    employeeDiv.append(employeePic);
    
    const employeeName = document.createElement("p");
    employeeName.innerText = `${fName} ${lName}`;
    employeeDiv.append(employeeName);
    
    const employeeCountry = document.createElement("p");
    employeeCountry.innerText = country;
    employeeDiv.append(employeeCountry);
    
    const employeeEmail = document.createElement("a");
    employeeEmail.href = `mailto:${email}`;
    employeeEmail.innerText = email;
    employeeDiv.append(employeeEmail);

    document.querySelector("#employees").append(employeeDiv);
}

// createEmployeeElement("Dylan", "Ford", "dford@gmail.com", "Canada", "https://cdn.shopify.com/s/files/1/0272/4770/6214/articles/when-do-puppies-start-walking.jpg")

fetch("https://randomuser.me/api/?results=6")
    .then(response => response.json())
    .then(data => {
        const employees = data.results;
        employees.forEach(employee => {
            createEmployeeElement(employee.name.first, employee.name.last,
                employee.email, employee.location.country, 
                employee.picture.large);
        })
    });


    
// console.log(data.results[0].name.first)
// console.log(data.results[0].name.last)
// console.log(data.results[0].email)
// console.log(data.results[0].location.country)
// console.log(data.results[0].picture.large)

// console.log(data.value);
// const p = document.createElement("p");
// p.innerText = data.value;
// console.log(p)
// document.querySelector("#employees").append(p);