# Digital.ai Release Plugin - JFrog Xray

This Plugin offers an interface in Digital.ai Release to a JFrog Xray Server or Cloud API.

# How to Use

1. Download this repository.
1. From the root folder, run `./gradlew build`. A `build` folder should be generated.
1. Go to `build/libs` and you should see a `.jar` file. Place this file to your Digital.ai Release folder under `plugins/__local__`.
1. Restart Digital.ai Release.
1. In Digital.ai Release, go to `Settings` > `Shared Configuration`, and you should see the Xray Server configuration. Click `+` and add your configuration.
![](images/xray/getreport.png)

### Get Vulnerabilities Report

+ `Xray` > `Get Reports` : Get a vulnerabilities report based on Report ID and artifact identifier (as specified in the configuration).

# References

* [JFrog Xray REST API](https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API)