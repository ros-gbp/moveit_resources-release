%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-moveit-resources-panda-moveit-config
Version:        0.8.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_resources_panda_moveit_config package

License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-joint-state-publisher
Requires:       ros-noetic-joint-state-publisher-gui
Requires:       ros-noetic-moveit-resources-panda-description
Requires:       ros-noetic-robot-state-publisher
Requires:       ros-noetic-rviz
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-xacro
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MoveIt Resources for testing: Franka Emika Panda A project-internal
configuration for testing in MoveIt.

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
* Thu Nov 18 2021 MoveIt maintainer team <moveit_releasers@googlegroups.com> - 0.8.2-1
- Autogenerated by Bloom

* Sat Nov 06 2021 MoveIt maintainer team <moveit_releasers@googlegroups.com> - 0.8.1-1
- Autogenerated by Bloom

* Mon May 03 2021 Mike Lautman <mike@picknik.ai> - 0.8.0-1
- Autogenerated by Bloom

* Mon Mar 29 2021 Mike Lautman <mike@picknik.ai> - 0.7.2-1
- Autogenerated by Bloom

* Fri Oct 09 2020 Mike Lautman <mike@picknik.ai> - 0.7.1-1
- Autogenerated by Bloom

* Thu Aug 13 2020 Mike Lautman <mike@picknik.ai> - 0.7.0-1
- Autogenerated by Bloom

