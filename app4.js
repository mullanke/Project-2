// chelsea is playing with js in this file

// from data.js
var tableData = data2;

// YOUR CODE HERE!
// Table Stuff
var $tbody = d3.select("tbody");
var button = d3.select("#filter-btn");
var inputFieldDate = d3.select("#date");
var inputdeathConfirmed = d3.select("#deathconfirmed");
var columns = ["date", "deathConfirmed", "deathIncrease", "deathConfirmed", "deathIncrease",
"positive","positiveIncrease","recovered","totalTestResults","totalTestResultsIncrease"]


var addData = (dataInput) => {
    dataInput.forEach(Covidstatistics => {
        var row = $tbody.append("tr");
        columns.forEach(column => row.append("td").text(Covidstatistics[column])
        )
    });
}
addData(tableData);


button.on("click here", () => {

    d3.event.preventDefault();
    

    var inputDate = inputFieldDate.property("value").trim();
    var filterDate = tableData.filter(tableData => tableData.date === inputDate);
    

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
// YOUR CODE HERE!
function buildTable(cats) {  
    // First, clear out any existing data  
        tbody.html("");
    // Next, loop through each object in the data  
    // and append a row and cells for each value in the row  
    cats.forEach(function(dogs) {    
    // Append a row to the table body    
        var row = tbody.append("tr");
    // Loop through each field in the dataRow and add    
    // each value as a table cell (td)    
        Object.values(dogs).forEach((birds) => {      
            var cell = row.append("td");        
            cell.text(birds);      
        }    
        );  
    });
    }
    function handleClick() {
    // Grab the datetime value from the filter  
    var date = d3.select("#datetime").property("value");  
    let filteredData = tableData;
    // Check to see if a date was entered and filter the  
    // data using that date.  
    if (date) {    
    // Apply filter to the table data to only keep the    
    // rows where the datetime value matches the filter value    
    filteredData = tableData.filter(function(keyboard) {
        keyboard.datetime === date});  
    }
    // Rebuild the table using the filtered data  
    // @NOTE: If no date was entered, then filteredData will  
    // just be the original tableData.  
    buildTable(filteredData);
    }
    // Attach an event to listen for the form button
    d3.selectAll("#filter-btn").on("click", handleClick);
    // Build the table when the page loads
    buildTable(tableData);