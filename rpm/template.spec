%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-moveit-resources-prbt-support
Version:        0.8.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_resources_prbt_support package

License:        Apache 2.0
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-canopen-motor-node
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-joint-state-controller
Requires:       ros-noetic-robot-state-publisher
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosservice
Requires:       ros-noetic-topic-tools
Requires:       ros-noetic-xacro
BuildRequires:  eigen3-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-code-coverage
BuildRequires:  ros-noetic-joint-state-publisher
BuildRequires:  ros-noetic-moveit-core
BuildRequires:  ros-noetic-moveit-ros-planning
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-rviz
BuildRequires:  ros-noetic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Mechanical, kinematic and visual description of the Pilz light weight arm PRBT.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon May 03 2021 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.8.0-1
- Autogenerated by Bloom

* Mon Mar 29 2021 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.7.2-1
- Autogenerated by Bloom

