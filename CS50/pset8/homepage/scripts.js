function greet() {
    alert('HI THERE')
}


function greet_with_name() {
    let name = document.querySelector('#name').value;
    alert('Hello, ' + name);
}


document.addEventListener('DOMContentLoaded', function() {
    // console.log('DOM yüklendi')

    // Example: Search in spotify
    document.querySelector('#spotify_form').addEventListener('submit', function(event) {
        let search = document.querySelector('#spotify_input').value;
        window.location.href = `https://open.spotify.com/search/${search}`;
        event.preventDefault();
    });

    // Example: Name2
    document.querySelector('#form_name2').addEventListener('submit', function(event) {
        let name2 = document.querySelector('#name2').value;
        //console.log(name2)
        alert('Hello, ' + name2);
        event.preventDefault();
    });

    // Example: Name3
    let input = document.querySelector('#name3')    // select input area
    let name3 = document.querySelector('#p_name3'); // the place we want to write
    input.addEventListener('keyup', function(event) {
        //console.log(name3 + "    " + input.value)
        if (name3) {
            name3.innerHTML = `hello, ${input.value}`;
        }
        else {
            name3.innerHTML = `hello, there`;
        }
    });

    // Example: Blink
    // Toggles visibility of #part_id
    /*
    function blink() {
        let part = document.querySelector('#part_id');
        if (part.style.visibility == 'hidden')
            { part.style.visibility = 'visible'; }
        else
            { part.style.visibility = 'hidden'; }
    }

    // Blink every 500ms
    window.setInterval(blink, 500);
    */

    // Example: Geolocation
    let example_read = document.querySelector('#geo_button');
    let example_write = document.querySelector('#geo_p')
    example_read.addEventListener('click', function() {
        navigator.geolocation.getCurrentPosition(function(position) {
            example_write.innerHTML = (position.coords.latitude + ", " + position.coords.longitude);
        });
    });
});

