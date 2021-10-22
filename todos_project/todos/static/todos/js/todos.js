///////////////////////////////////////////////////////////////////////////////
// FILE     : todos.js
// SYNOPSIS : All JavaScript used in this app.
// LICENSE  : MIT
// NOTES    :
//   1. This code is written only with browser compatability in mind. It can
//      be improved with the lastest version of ECMAScript.
//   2. Uses jQuery
///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
// CONSTANTS
///////////////////////////////////////////////////////////////////////////////

var COLD_THRESHOLD = 10.0;
var HOT_THRESHOLD = 25.0;
var HOT_COLOUR = 'red';
var WARM_COLOUR = 'gold';
var COLD_COLOUR = 'blue';

var REGEX_TASK = new RegExp('<li>Location\s*:\s*(.*)\s*</li>', 'm');
var REGEX_LOCATION = new RegExp('id="(.*)"', 'm');
var BASE_URL = 'http://localhost:8000/todos/weather/?q=';


///////////////////////////////////////////////////////////////////////////////
// FUNCTIONS
///////////////////////////////////////////////////////////////////////////////

function get_colour(temperature) {
    if (temperature < COLD_THRESHOLD) {
        return (COLD_COLOUR);
    } else if (temperature > HOT_THRESHOLD) {
        return (HOT_COLOUR);
    } else {
        return (WARM_COLOUR);
    }
}


///////////////////////////////////////////////////////////////////////////////
// MAIN
///////////////////////////////////////////////////////////////////////////////

$(document).ready(function(){
    // If 'todo' classes are there give them a colour based on temperature.
    var $tasks = $('.todo');
    for (var i = 0; i < $tasks.length; i++) {
        var $current_task = $tasks.eq(i);
        var $task_html = $current_task.html();
        var $task_location = $task_html.match(REGEX_TASK)[1].trim();
        if ($task_location.length) {
            var url_get = BASE_URL + $task_location;
            $.ajax({
                type: 'GET',
                url: url_get,
                context: {'task': $current_task},
                success: function(data) {
                    var temperature = data.temperature;
                    var colour = get_colour(temperature);
                    this.task.css('background-color', colour);                }
            });
        }
    }

    // Show weather at the beginning for an update.
    var $update_marker = $(".temperature");
    if ($update_marker.length) {
        var $location = $update_marker.prop('outerHTML');
        if (REGEX_LOCATION.test($location)) {
            var start_location = $update_marker.prop('outerHTML').match(REGEX_LOCATION)[1];
            var url_get = BASE_URL + start_location;
            $.ajax({
                type: 'GET',
                url: url_get,
                context: {
                    'marker': $update_marker,
                    'form': $('.todo_form')
                },
                success: function(data) {
                    var temperature = data.temperature;
                    var colour = get_colour(temperature);
                    this.form.css('background-color', colour);
                    this.marker.html(`<strong>Current Temperature: ${temperature}C</strong>`);
                }
            });
        }
    }
    
    // Let location decide the colour of 'Create' and 'Update' forms.
    var $location = $('#id_location');
    if ($location.length) {
        $location.on('input', function(){
            var location = $location.val();
            var $form = $('.todo_form');
            if ($form.length) {
                var url_get = BASE_URL + location;
                $.ajax({
                    type: 'GET',
                    url: url_get,
                    context: {'form': $form},
                    success: function(data) {
                        var temperature = data.temperature;
                        var colour = get_colour(temperature);
                        this.form.css('background-color', colour);
                        var $temperature_text = $('.temperature');
                        if ($temperature_text.length) {
                            $temperature_text.html(`<strong>Current Temperature: ${temperature}C</strong>`);
                        }
                    }
                });
            }
        });
    }
});


///////////////////////////////////////////////////////////////////////////////
// END
///////////////////////////////////////////////////////////////////////////////
