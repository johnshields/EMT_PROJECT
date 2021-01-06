/**
 * Code References:
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

    // works with the predict_power method in web_service.py
    $.ajax("/api/model-playground", {
        type: "POST",
         // take the entered speed value
        data: speedData,
        success: function (data) {
            // send back a prediction response
            const powerData = data[['response']];
            $("#prediction").text(` Predicted Wind Turbine Power = ${powerData}`);
        },
        error: function () {
            // error for catching any unwanted values
            $("#prediction").text("ERROR! Please Enter a NUMBER!");
        },
    });
})