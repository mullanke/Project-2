// from data.js
var tableData = data2;

// YOUR CODE HERE!
// Table Stuff
var $tbody = d3.select("tbody");
var button = d3.select("#filter-btn");
var inputFieldDate = d3.select("#datetime");
var inputFieldCity = d3.select("#city");
var columns = ["date", "state", "death", "deathConfirmed", "deathIncrease"]


// Putting the data into HTML
var addData = (dataInput) => {
    dataInput.forEach(ufoSightings => {
        var row = $tbody.append("tr");
        columns.forEach(column => row.append("td").text(ufoSightings[column])
        )
    });
}



addData(tableData);


// Button for date search

button.on("click here", () => {

    d3.event.preventDefault();
    

    var inputDate = inputFieldDate.property("value").trim();
    var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);
    

    $tbody.html("");

    let response = {
        filterDate
    }


    if(response.filterDate.length !== 0) {
        addData(filterDate);
    }

    //Else statement
    
        else {
            $tbody.append("tr").append("td").text("Sorry about your luck...Keep er Moving...");
        }
})
