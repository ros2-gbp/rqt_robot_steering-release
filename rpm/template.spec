%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt-robot-steering
Version:        1.0.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rqt_robot_steering package

License:        BSD
URL:            http://wiki.ros.org/rqt_robot_steering
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ament-index-python
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-python-qt-binding >= 0.2.19
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rqt-gui
Requires:       ros-rolling-rqt-gui-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_robot_steering provides a GUI plugin for steering a robot using Twist
messages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Mar 21 2025 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.1-2
- Autogenerated by Bloom

* Fri Mar 21 2025 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.0-5
- Autogenerated by Bloom

