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

const COLD_THRESHOLD = 15.0;
const HOT_THRESHOLD = 25.0;
const HOT_COLOUR = 'red';
const WARM_COLOUR = 'gold';
const COLD_COLOUR = 'blue';

const REGEX_TASK_LOCATION = new RegExp('<li>Location\s*:\s*(.*)\s*</li>', 'm');
const REGEX_TASK_DONE = new RegExp('<li>Done: False</li>', 'm');
const REGEX_TEMPERATURE_LOCATION = new RegExp('id="(.*)"', 'm');
const BASE_URL = 'http://localhost:8000/todos/weather/';


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
    const $tasks = $('.todo');
    for (let i = 0; i < $tasks.length; i++) {
        const $current_task = $tasks.eq(i);
        const $task_html = $current_task.html();
        if (REGEX_TASK_DONE.test($task_html)) {
            const $task_location = $task_html.match(REGEX_TASK_LOCATION)[1].trim();
            if ($task_location.length) {
                $.ajax({
                    type: 'GET',
                    url: BASE_URL,
                    data: {'q': $task_location},
                    context: {'task': $current_task},
                    success: function(data) {
                        const temperature = data.temperature;
                        const colour = get_colour(temperature);
                        this.task.css('background-color', colour);
                    }
                });
            }
        }
    }

    // Show weather at the beginning for an update.
    const $update_marker = $(".temperature");
    if ($update_marker.length) {
        const $location = $update_marker.prop('outerHTML');
        if (REGEX_TEMPERATURE_LOCATION.test($location)) {
            const $start_location = $update_marker.prop('outerHTML').match(REGEX_TEMPERATURE_LOCATION)[1];
            $.ajax({
                type: 'GET',
                url: BASE_URL,
                data: {'q': $start_location},
                context: {
                    'marker': $update_marker,
                    'form': $('.todo_form')
                },
                success: function(data) {
                    const temperature = data.temperature;
                    const colour = get_colour(temperature);
                    this.form.css('background-color', colour);
                    this.marker.html(`<strong>Current Temperature: ${temperature}C</strong>`);
                }
            });
        }
    }
    
    // Let location decide the colour of 'Create' and 'Update' forms.
    const $location = $('#id_location');
    if ($location.length) {
        $location.on('input', function(){
            const $form = $('.todo_form');
            if ($form.length) {
                $.ajax({
                    type: 'GET',
                    url: BASE_URL,
                    data: {'q': $location.val()},
                    context: {'form': $form},
                    success: function(data) {
                        const temperature = data.temperature;
                        const colour = get_colour(temperature);
                        this.form.css('background-color', colour);
                        const $temperature_text = $('.temperature');
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
