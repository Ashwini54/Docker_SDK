import docker,os
from docker.api import container, network, volume
from docker import APIClient

client = docker.from_env()
host_config = docker.APIClient()

### BUILDING PYTESt SAMPLE CODE USING PYTEST BASE IMAGE ### 
print(client.images.build(path="F:\\fixture_pytest_", tag='testimg_py', quiet=True))

### RUNNING THE PYTEST IMAGE ###
pytestimg=client.containers.run("testimg_py",command='/bin/bash', tty=True, detach=True, auto_remove=False)
print("pytestimage:",pytestimg)

##  RUNNING PYTHON IMAGE WITH VOLUME MOUNTED ##
pytestimg_vol=client.containers.run(image='testimg_py', command='python test_div_by_.py ',auto_remove=False, stdin_open=True, detach=True, volumes={'testimg_py-volume': {'bind': '/data', 'mode': 'rw'}})
print("testimg_py:", pytestimg_vol)


## COMMAND TO RUN INSIDE THE CONTAINER ##
cmd='/bin/bash -c "cd googleTest_framework/googleTest_framework-main && cmake CMakeLists.txt &&  make && ./executeTests "'

## RUNNING CATCH2_GOOGLETEST IMAGE ##
gtestimg=client.containers.run("ashwinis2/catch2_googletest:1",command=cmd, tty=True, detach=True, auto_remove=False )
print(gtestimg)

## RUNNING CATCH2_GOOGLETEST WITH VOLUME MOUNTED ##
r3=client.containers.run(image='ashwinis2/catch2_googletest:1',auto_remove=False, stdin_open=True, detach=True, volumes={'catch2_googletes-volume': {'bind': '/googleTest_framework', 'mode': 'rw'}})
print("catch2_googletest:" ,r3)

# RUNNING GTEST WITH VOLUME MOUNTED ##
r4=client.containers.run(image='ashwinis2/gtest',auto_remove=False, stdin_open=True, detach=True,volumes={'gtest-volume': {'bind': '/data', 'mode': 'rw'}})
print("gtest:" , r4)


## RUNNING UBUNTU IMAGE WITH VOLUME MOUNTED ##
ubuntu_img = client.containers.run(image='ubuntu', auto_remove=False, stdin_open=True, detach=True,volumes={'ubuntu-volume': {'bind': '/data', 'mode': 'rw'}})
print("ubuntu :" , ubuntu_img)
print(ubuntu_img.exec_run(cmd='echo $(find /)'))

## RUNNING COMMAND INSIDE CONTAINER USING RUN COMMAND ##
catch2_googletest_img = client.containers.run(image='ashwinis2/catch2_googletest:1',command=cmd, auto_remove=False, stdin_open=True, detach=False, volumes={'dummy_myvol2': {'bind': '/googleTest_framework', 'mode': 'rw'}} )
print("catch2_googletest:" , catch2_googletest_img)
# print(catch2_googletest_img.logs())

## EXECUTING THE COMMAND USING EXECUTE COMMAND ##
res=r3.exec_run(cmd, stream=False, demux=False)
print(res)

# DOCKERHUB CREDENTIALS & PUSHING IMAGE TO DOCKER HUB ##
# client.login(username='', password='')
# for line in client.images.push('ashwinis2/trial_image', stream=True, decode=True):
#   print(line)
