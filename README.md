# Electronic-Air-Rifle-Target


Reason why I am starting this project: Due to strict import regulations in my country, the cost of the open-source kit is significantly higher, making it less affordable.

Description:
The Python Target System is a simple and efficient solution that eliminates the need for individuals to walk down the range to check their shots. This system integrates a graphical user interface (GUI) that displays a target image where shots are represented as circles. The system communicates with an API to retrieve shot coordinates and updates the target image in real-time based on the received data.

Key Features:

Real-time Updates: The system continuously fetches the latest shot coordinates from an API, ensuring that the target image stays up to date with the most recent shots.


Graphical Representation: The target image is displayed in a GUI window using the Tkinter library. Shots are depicted as circles on the target, allowing users to visualize their shooting accuracy at a glance.

Multiple Shots Support: The system accommodates multiple shots and provides separate entry fields for each shot's Y and Z coordinates. Each shot is represented by a circle on the target image, making it easy to differentiate between different shots.

Last Shot Highlight: The system highlights the most recent shot on the target image by drawing it in red, while all other shots are displayed in black. This distinction helps users quickly identify their latest shot.

Dynamic Shot Addition: If the API returns additional shots, the system dynamically adjusts the target image and coordinate lists to accommodate the new shots. This flexibility allows for a scalable system that can handle varying shot quantities.

API Integration: The system communicates with a specified API endpoint to retrieve shot data in JSON format. It utilizes the requests library to send HTTP requests and retrieve the JSON response.

 ```
Route::get('/electronic-air-rifle-target', function () {
    $json = [
        "target" => [
            ["schot" => "1", "y" => "20", "z" => "20"],
            ["schot" => "2", "y" => "10", "z" => "20"],
            ["schot" => "3", "y" => "25", "z" => "20"],
            ["schot" => "4", "y" => "20", "z" => "60"],
            ["schot" => "5", "y" => "0", "z" => "0"]
          
        ]
    ];

    return response()->json($json);
});
``` 
The Python Target System empowers shooting enthusiasts by providing a convenient and efficient way to track their shots without the need for physical movement downrange. Its real-time updates, graphical representation, and support for multiple shots make it an invaluable tool for improving shooting accuracy and optimizing training sessions.



#TODO-List

*Develop a Web Version - Create a web-based version of the application to make it accessible and usable on a tablet.

Research and choose a suitable web development framework.
Design and implement the user interface optimized for tablet devices.
Adapt the existing functionality to work in the web environment.
Determine Pellet Location Detection Method - Identify an affordable and reliable sensor or method to accurately detect the location of the pellet.

*Research different sensor options that can effectively detect the pellet's location.
Consider factors such as accuracy, cost, compatibility, and ease of integration.
Select the most suitable sensor or method for pellet location detection.
Acquire and test the chosen sensor or method to ensure it meets the requirements.
Perform Rigorous Testing - Conduct thorough testing to ensure the functionality and reliability of the system.

*Create a comprehensive test plan covering different scenarios and use cases.
Perform unit testing to verify the individual components of the system.
Conduct integration testing to ensure the seamless operation of the different modules.
Carry out extensive user testing to gather feedback and identify any usability issues.
Iterate and refine the system based on the testing results and user feedback.
Optimize Performance and Stability - Continuously improve the performance and stability of the system.

*Identify and address any bottlenecks or performance issues.
Optimize algorithms and data structures for efficiency.
Implement error handling and exception management to enhance stability.
Monitor system performance in real-world scenarios and fine-tune as necessary.
Document and Maintain the System - Document the system's architecture, functionality, and usage instructions. Ensure ongoing maintenance and support.

*Create comprehensive documentation explaining the system's components, their interactions, and deployment instructions.
Update the documentation to reflect any changes or enhancements to the system.
Provide ongoing support to users, addressing any issues or inquiries promptly.
Maintain version control and track changes to the codebase.


<a href="https://www.buymeacoffee.com/Eyonic" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
