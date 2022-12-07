# HoneyPI beehive monitor
an attempt to leverage raspberryPI to monitor hive vital signs. leverate Lorawan
for remote montoring.

## BOM
- lorawan gateway
    - [PI 4b 4g](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
    - [RAKwireless Lora hat](https://www.rakwireless.com/en-us/products/lpwan-gateways-and-concentrators/rak2245-pihat)
- monitor
    - [gpio grove hat, seeed studio](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/)
    - [lora Grove Wio-E5, seeed studio](https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/)
    - [sound sensor grove, seeed studio](https://wiki.seeedstudio.com/Grove-Sound_Sensor/)
    - [temp humidity sensor, switchdoc labs](https://shop.switchdoc.com/collections/shop-all/products/sht30-i2c-waterproof-temperature-and-humidity-sensor-with-grove)

## python libs
- [pipdeptree](https://pypi.org/project/pipdeptree/)
- [coverage](https://pypi.org/project/coverage/)
- [black](https://pypi.org/project/black/)
- [RPi.gpio](https://pypi.org/project/RPi.GPIO/)

## tests
 p3 setup.py test -v  -s <fully qualified test class>

## build system
- [jenkins](https://www.jenkins.io/)
    - [docker container](https://github.com/jenkinsci/docker/)
    - [credentials plugin](https://github.com/jenkinsci/credentials-plugin)
    - [ssh agent plugin](https://plugins.jenkins.io/ssh-agent/)
    - [sonarqube scanner plugin](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-jenkins/)
- [remote agent on PI](https://www.gdcorner.com/2019/12/27/JenkinsHomeLab-P2-LinuxAgents.html)
    - [added known_host to docker data](https://stackoverflow.com/questions/44441935/cant-connect-to-jenkins-slave-no-known-hosts-file-was-found-at-var-jenkins-hom)
    - gen ssh key via [putty](https://www.ssh.com/academy/ssh/putty/windows/puttygen)
    - for jenkins ssh key creds need to export private key as [openssh format](https://stackoverflow.com/questions/53636532/jenkins-what-is-the-correct-format-for-private-key-in-credentials) 
