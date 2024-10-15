# **ACROBA Platform**

## **0. Requirements** 

* Host operating system:
    - Linux
    - Windows 11 with WSL 2 
* Software: 
    - git: 
        https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    - docker:
        https://docs.docker.com/engine/install/

* Hardware: 
    - NVIDIA GPU (optional)

<br>

>[!WARNING]
> **Known Issues**<br>
> 
> **Docker**<br>
> it is required to use:
> - a docker version >= 24.x <br>
> older versions are not supported due to some issues with the path resolution of docker compose file extensions<br>
> - a docker compose v2 version >= 2.23.x ( :bangbang: uninstall older versions of docker-compose v1 ) <br>
> :warning: **DO NOT USE** docker compose 2.24.3, 2.24.4, 2.24.6 or 2.24.7, they have some bugs and cannot be used, cf:<br>
> https://github.com/docker/compose/issues/11394 <br>
> https://github.com/compose-spec/compose-go/pull/547 <br>
> https://github.com/docker/compose/issues/11544 <br>
> 
>
> **WSL 2**<br>
> When using WSL 2 as the host system, there are a couple of limitations in docker:  
> - OpenCL with Nvidia GPUs is not supported:
>       https://github.com/microsoft/WSL/issues/6951
> - The ports used by the services running in the docker container are not 
>   visible in WSL2 if the network host mode is used:  
>   https://github.com/docker/for-win/issues/6736 
> - The reverse, accessing a service running on WSL2 from a docker using 
>   host network is also not supported
>   https://github.com/docker/for-win/issues/9168#issuecomment-771971994 
> - the moveit setup assistant is not working under WSL with ros noetic. Some fixes are availabe here: 
>   https://answers.ros.org/question/394135/robot-meshes-not-visible-in-rviz-windows11-wsl2/
>
>
> **Linux**<br>
> - Docker desktop
>   * X11 forwarding does not seem to work properly with docker desktop under Ubuntu. 
>   * Some problems were encountered with the Nvidia GPU support while using docker desktop under Ubuntu 20.04 as the host OS: <br>
>     https://github.com/NVIDIA/nvidia-docker/issues/1711 <br>
>     The same issue seems to occur with Ubuntu 22.04 LTS: <br>
>     https://github.com/NVIDIA/nvidia-docker/issues/1652 <br>
> 
>   :white_check_mark: The solution is to desinstall Docker desktop and to use docker engine instead. 
>
> - When using an NVidia GPU with docker engine, docker could trigger the following error "docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed". In this case, it is necessary to re-set up the container toolkit: <br>
> https://github.com/NVIDIA/nvidia-docker/issues/1648 <br>
> https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
> 
>
> **Windows**<br>
> - windows cannot be used as the host os, as teh host network mode (which is the mode used by the platform) is not available in docker for windows.


## **1. Setup**

### 1.1 NVIDIA GPU 

Some setup is necessary to be able to use the Nvidia GPUs inside the docker containers:

#### 1.1.1 Linux Host OS 

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

#### 1.1.2 Windows 11 + WSL 2

https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl<br>
https://docs.nvidia.com/cuda/wsl-user-guide/index.html


### 1.2 Git

#### 1.2.1 SSH 

To be able to checkout packages, you need to set up your git account to use SSH authentification. 

https://github.com/settings/keys
https://docs.github.com/en/authentication/connecting-to-github-with-ssh

>[!WARNING]
> Do not use a passphrase in your ssh keys (submodules checkout will fail)!

#### 1.2.2 Personal Acess Tokens  

The platform images are available as packages on github. 
To be able to pull or push/release packages from/to github it is necessary to set up PAT (Personal Access Token) authentification. 

##### *Generate a git token*

1. From the git user menu, go to Settings > Developper settings > Personal access tokens > Tokens (classic)
2. Click on Generate new token menu > Generate new token (classic)
3. check the boxes repo write:packages delete:packages
4. Generate token, put a name and save the token somewhere. 

    
##### *Set up a git credential helper*

On linux, one way is to use libsecret to store the PAT in an encrypted format: 
```
sudo apt-get install libsecret-1-0 libsecret-1-dev
sudo make --directory=/usr/share/doc/git/contrib/credential/libsecret
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
``` 

some other alternatives are described [here](https://stackoverflow.com/questions/46645843/where-to-store-my-git-personal-access-token)


##### *Test the access*
```
docker login ghcr.io -u <Your-GitHub-Username>
password: <enter your PAT>
```

>[!WARNING]
> if you do get some "permission denied error" with docker, you need to set docker up for non root user:<br>
> ```
> sudo usermod -aG docker $USER
> ```
> more information [here](https://docs.docker.com/engine/install/linux-postinstall/)

## **2. Installation**

```
git clone git@github.com:ACROBA-Project/ACROBA-Platform.git
cd ACROBA-Platform
```

## **3. Usage for the impatient**

### 3.1 <ins>Run</ins> the platform without building

Using a release version 
```
git checkout <tag> # e.g. git checkout v0.3.0
make pull
make run
```

using the main branch
```
make pull TAG=latest
make run
```

The commands download the ACROBA generic modules docker images, and run the platform without a cell config. See section [Running](#5-running) for more details. 

### 3.2 <ins>Build</ins> the platform 

```
make
```

This checks out the submodule code, builds the platform and runs it. 
The commands download the ACROBA generic modules docker images, and run the platform without a cell config. See section [Building](#4-building) for more details. 


## **4. Building**

### 4.1 Build process

#### 4.1.1 Checkout

To build the platform, one needs to first checkout the submodules code, which is achieved by using one of the below commands: 

```
make checkout                   # checks out the submodules code (detached head mode)

make checkout-update            # checks out the last versions of the submodules code
```


>[!Important]<br><br>
> **Checkout & acroba-modules versions** <br>
> when running `make checkout`, the versions of the acroba modules which were explicitely committed in the platform will be used. The acroba modules (submodules) work in detached head mode by default, i.e. if some new commits are available in the acroba module(s) repo(s), they won't be downloaded. This feature allows to fix the versions of acroba modules that are used, build, pulled, etc, by the platform, and avoid ending up in cases where downloading the latest available commits do not compile. <br><br>
> If you want to use the latest versions of the acroba modules which are tracking a branch, then do: `make checkout-update` before building. This will update the submodules, the ones tracking a branch, to the latest commits (c.f. [Working with git submodules](./doc/git.md)). <br><br>
> In order to commit the latest module(s) changes to the platform, i.e. such that each  submodule detached head points to the latest commit, one can do: 
> ```make update-modules```. This command will commits the versions currently checked out in the platform, such that they are now used by default. 
>

#### 4.1.2 Building 

To build the full platform then use the command: 
```
make build [TAG=<tag>]          # build the acroba platform using the given tag for each images. 
                                # default: TAG = `last git commit hash for each submodules` 
```

>[!Important]<br>
> 
> **HASH Values** <br>
> when running `make build`, the hash values being used for the platform modules are:
> - for the GUI, skills, skills_mockup, taskplanner, VG: the git hash of the last commit in each module repo. 
> - for the ros1-base-nvidia, acroba-base-ros1,  acroba-base-ros1-gpu, acroba-base-ros2, cell-config-base, and ros1-bridge components: the git hash of the last commit in the platform repo, 
>   as these modules are docker only and have no associated repo.  
<br>


### 4.2 Docker images management

#### 4.2.1 Deployment on github registry

The following make commands are available for managing the versions of the platform, in particular, for pushing built images to the github registry 

```
make push [TAG=<tag>]           # push the built images with the given tag to the github registry 
                                # default: TAG = `last git commit hash for each submodules` 
make release [LABEL=<label>]    # push the built image to the github register
                                # default: LABEL = "latest"
```

#### 4.2.2 Deleting unused local images

When developping some acroba module(s), one may end up building the platform repeatedly while modifying locally some submodule(s). This process may result in building many docker images, some being outdated and not used anymore. Some make commands help cleaning and checking which images are currently used by the platform: 

```
make check-images     # checks and returns the list of docker image names
                      # which are currently used by the platform, i.e. in the generic image names acroba/<xyz>. 
make clean-images     # removes the local docker images that are not used by   
                      # the platform, i.e. the generic image names acroba/<xyz>. 
```

## **5. Running**

 There is the possibility to run the platform without building it by "pulling" images which have already published to the git register 

### 5.1 Pull

#### *Checked-out version*

To pull a version of the platform composed of the modules which have been (automatically or manually) checked out, one can simply do: 

```
make pull 
```

For each platform module, this command retrieves the hash of the current git checkout, and pulls the module image with the corresponding hash. Some error will be thrown in case a module does not have an image available with the corresponding git hash on ghcr.io. 


#### *Release version*
 
To pull the latest (released) version of the platform: 
```
make pull TAG=latest
```

### 5.2 Run

To run the platform: 
```
make run [<optional-arguments>]
```

Optional Arguments: 
*  `X11=(YES|NO) [default: YES]` Use X11 port forwarding or not. If not, a NoVnc server service will be started and the platform is accessible through the web browser at http://localhost:8080/

* `GPU=(YES|NO) [default: YES]` Enable the nvidia GPU support or not (i.e. use CPU only). 

* `CELL=<cell_image_name> [default: NONE]` The docker image name to use for the robotic cell without the acroba prefix, e.g. `CELL=cell-config-bfh` to use the docker image `acroba/cell-config-bfh`. By default the platform is launched without a cell config.

<br>

>[!NOTE]
> **Cell Configuration Image**<br>
> Cell config images do not belong to the generic acroba platform modules; cell configs are configured/built/pulled separately.
>  
> Instructions on how to create a cell configuration image and how to integrate/use it in the platform are available in the following link: <br>
> [setting up a cell config image](./doc/cell-config.md) 
> 
> To pull an available cell-config image directly from the platform repo, without checking out the cell-config git repo, one can use the following (hidden) command: 
> ``` 
> make _pull_<cell-config-name> TAG=<version_to_use>
> ```
> e.g
> ```
> make _pull_cell-config-bfh TAG=latest
> ```


## **6. Folders** 

the platform is using the following folders across all containers:

```
/home/acroba/ros-workspaces/ros1-noetic/   # ros1 workspace will contain src build devel log subfolders
/home/acroba/ros-workspaces/ros2-galactic/ # ros2 workspace will contain src build install log subfolders
/home/acroba/logs                          # volume containing logs 
/home/acroba/data                          # volume for the acroba data
/home/acroba/config/ssh                    # bind mount to folder holding the ssh keys needed for
                                           # inter-container communication 
/home/acroba/shared                        # bind mount to the ./shared directory in the architecture repo
```
  
The "shared" folder can be used to hold any specific code file, any change in this folder will be reflected in platform and vice versa.


## **7. Development**

Instructions for developing and debugging specific modules on the full platform are available at the following link:
[Developing some module(s) in the platform](./doc/dev.md) 

