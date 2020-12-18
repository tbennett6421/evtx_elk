# evtx_elk

This package is a repository of information for running an elk stack on docker

I've run into instances in the past where investigators have been dealing with an incident and extracted forensic artifacts from a machine and needed to extract information from the data quickly. The purpose of this repository is to allow an analysts to hunt through raw event logs using kibana rather then using xpath searching with powershell's `get-winevent` function or using the event viewer.

Repository contents
* docker/
    * the resources for running the elk stack on docker
* docs/
    * contains installation or architecture-specific notes
* evtxshipper/
    * the python command to collect evtx files and package them for forwarding to logstash
