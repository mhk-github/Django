/* JavaScript file for Todos */

function get_colour(temperature) {
    var COLD_THRESHOLD = 10.0;
    var HOT_THRESHOLD = 25.0;
    var HOT_COLOUR = 'red';
    var WARM_COLOUR = 'gold';
    var COLD_COLOUR = 'blue';

    if (temperature < COLD_THRESHOLD) {
        return (COLD_COLOUR);
    } else if (temperature > HOT_THRESHOLD) {
        return (HOT_COLOUR);
    } else {
        return (WARM_COLOUR);
    }
}

var REGEX = new RegExp('<li>Location\s*:\s*(.*)\s*</li>', 'm');
var BASE_URL = 'http://localhost:8000/todos/weather/?q=';

$(document).ready(function(){
    var $tasks = $('.todo');
    for (var i = 0; i < $tasks.length; i++) {
        var $current_task = $tasks.eq(i);
        var $task_html = $current_task.html();
        var $task_location = $task_html.match(REGEX)[1].trim();
        if ($task_location.length) {
            var temperature;
            var url_get = BASE_URL + $task_location;
            $.ajax({
                async: false,
                type: 'GET',
                url: url_get,
                success: function(data) {
                    temperature = data.temperature;
                }
            });
            var colour = get_colour(temperature); 
            $current_task.css('background-color', colour);
        }
    }
    
    var $location = $('#id_location');
    if ($location.length) {
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        $location.on('input', function(){
            var location = $location.val();
            console.log(`Location = '${location}'`);
            console.log(`    Encoded URI = ${encodeURI(location)}`);
            console.log(`    CSRF Token = '${csrfToken}'`);
            var $form = $('.todo_form');
            if ($form.length) {
                var url_get = BASE_URL + location;
                $.ajax({
                    async: false,
                    type: 'GET',
                    url: url_get,
                    success: function(data) {
                        var temperature = data.temperature;
                        var colour = get_colour(temperature);
                        $form.css('background-color', colour);
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
