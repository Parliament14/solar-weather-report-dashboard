# solar-weather-report-dashboard
#### Introduction 
My goal here is to create a dashboard using Flask that displays data regarding the "weather conditions" in the solar system. I plan on using the open API's provided by NASA to pull real-time data regarding near-earth objects, coronoal mass ejections, solar flares, and more as time goes on. Currently, the project is in its **veeeeery** early stages. 

#### High-Level Roadmap 
* Build functional nasa API that pulls and formats data from NASA APIs to feed into the dashboard 
* Build the dashboard itself. I'm thinking it will run on top of flask, but not sure exactly how to structure the web applictaion at this stage 
* Figure out the JS, HTML, and CSS for the webapp


#### Usage (thus far) 
1. Geneare an API key from [NASA's API Portal](https://api.nasa.gov/)
2. Store said key in `/path/to/solar-weather-report-dashboard/api_key.txt`
    * tip: store in `.gitignore` if you plan on contributing :) 
3. Execute `python3 -i nasa_api.py` to interact with the NASA API (which is functional as of writing this) 
