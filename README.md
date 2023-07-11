# Electronic-Air-Rifle-Target


Description:
The Python or HTML Target System is a simple and efficient solution that eliminates the need for individuals to walk down the range to check their shots. This system integrates a graphical user interface (GUI) that displays a target image where shots are represented as circles. The system communicates with an API to retrieve shot coordinates and updates the target image in real-time based on the received data.

![Target.jpg](https://raw.githubusercontent.com/Eyonic/Electronic-Air-Rifle-Target/main/Doc/exsample-v1.jpg)


Key Features:

Real-time Updates: The system continuously fetches the latest shot coordinates from an API, ensuring that the target image stays up to date with the most recent shots.


Graphical Representation: The target image is displayed in a GUI window using the Tkinter library. Shots are depicted as circles on the target, allowing users to visualize their shooting accuracy at a glance.

Multiple Shots Support: The system accommodates multiple shots and provides separate entry fields for each shot's Y and X coordinates. Each shot is represented by a circle on the target image, making it easy to differentiate between different shots.

Last Shot Highlight: The system highlights the most recent shot on the target image by drawing it in red, while all other shots are displayed in black. This distinction helps users quickly identify their latest shot.

Dynamic Shot Addition: If the API returns additional shots, the system dynamically adjusts the target image and coordinate lists to accommodate the new shots. This flexibility allows for a scalable system that can handle varying shot quantities.

API Integration: The system communicates with a specified API endpoint to retrieve shot data in JSON format. It utilizes the requests library to send HTTP requests and retrieve the JSON response.

 ```php
// coordinates range: 100 / -100 ( The Laravel website uses the "web.php" file to handle routes, but the content is in plain JSON format, allowing for flexible modification of the delivery method.)
Route::get('/electronic-air-rifle-target', function () {
    $json = [
        "target" => [
            ["schot" => "1", "x" => "20", "z" => "20"],
            ["schot" => "2", "x" => "-10", "z" => "-20"],
            ["schot" => "3", "x" => "0", "z" => "0"]
        ]
    ];

    return response()->json($json)
        ->header('Access-Control-Allow-Origin', '*')
        ->header('Access-Control-Allow-Methods', 'GET');
});
``` 
The Python Target System empowers shooting enthusiasts by providing a convenient and efficient way to track their shots without the need for physical movement downrange. Its real-time updates, graphical representation, and support for multiple shots make it an invaluable tool for improving shooting accuracy and optimizing training sessions.



#TODO-List

*Develop a Web Version - Create a web-based version of the application to make it accessible and usable on a tablet.

*Score system and multiplayer support.

*Determine Pellet Location Detection Method - Identify an affordable and reliable sensor or method to accurately detect the location of the pellet.



<a href="https://www.buymeacoffee.com/Eyonic" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
