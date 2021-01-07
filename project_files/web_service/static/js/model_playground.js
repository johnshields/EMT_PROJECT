/**
 * Code References:
 * https://web.microsoftstream.com/video/63704d51-e829-4da9-ab3d-ae73b71ee8f2
 * https://api.jquery.com/jquery.post/
 * https://tinyurl.com/y39o626z
 * https://www.w3schools.com/jquery/jquery_ajax_load.asp
 * https://stackoverflow.com/questions/2320069/jquery-ajax-file-upload
 *
 * John Shields - G00348436
 * Model Playground Script for button function for predictions
 */

$("#predict_power").click(function () {
    let value = jQuery("#input").val();
    const speedData = {value: value};
    console.log("speed input value:");
    console.log(speedData);

    // works with the predict_power method in web_service.py
    $.ajax("/api/model-playground", {
        type: "POST",
         // take the entered speed value
        data: speedData,
        success: function (data) {
            const powerData = data[['response']];
            // fix the power result to 4 decimal places
            let result = Number(powerData).toFixed(4);
            // send back a prediction response
            $("#prediction").val(`${result}`);
            console.log("power output value:");
            console.log(result);
        },
        error: function () {
            // error for catching any unwanted values
            $("#prediction").val("ERROR! Enter NUMBER!");
            console.log("failed to respond/unwanted value entered");
        },
    });
})