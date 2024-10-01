Name:           hardinfo2
Version:        2.1.17
Release:        1
Summary:        System Information and Benchmark for Linux Systems
Group:          System/Kernel and hardware
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only
URL:            https://hardinfo2.org/
Source0:        https://github.com/hardinfo2/hardinfo2/archive/release-%{version}/hardinfo2-release-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

# Qt5 deps, needed only for GPU OpenGL benchmark (optional)
BuildRequires:  qmake5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5OpenGL)

Requires:  pciutils
Recommends:     lm_sensors
Recommends:     sysbench
Recommends:     lsscsi
Recommends:     glxinfo
Recommends:     mesa-demos
Recommends:     dmidecode
Recommends:     udisks2
Recommends:     xdg-utils
Recommends:     iperf3

%description
Hardinfo2 is based on hardinfo, which have not been released >10 years.
Hardinfo2 is the reboot that was needed.

Hardinfo2 offers System Information and Benchmark for Linux Systems. It is able
to obtain information from both hardware and basic software. It can benchmark
your system and compare to other machines online.

Features include:
- Report generation (in either HTML or plain text)
- Online Benchmarking - compare your machine against other machines

%prep
%autosetup -n hardinfo2-release-%{version} -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/hardinfo2
%dir %{_libdir}/hardinfo2
%dir %{_libdir}/hardinfo2/modules
%{_libdir}/hardinfo2/modules/benchmark.so
%{_libdir}/hardinfo2/modules/computer.so
%{_libdir}/hardinfo2/modules/devices.so
%{_libdir}/hardinfo2/modules/network.so
%{_libdir}/hardinfo2/modules/qgears2
%{_prefix}/lib/systemd/system/hardinfo2.service
%{_datadir}/applications/hardinfo2.desktop
%dir %{_datadir}/hardinfo2
%{_datadir}/hardinfo2/*.ids
%{_datadir}/hardinfo2/benchmark.data
%{_datadir}/hardinfo2/*.json
%{_datadir}/metainfo/org.hardinfo2.hardinfo2.metainfo.xml
%{_datadir}/hardinfo2/pixmaps/
%{_iconsdir}/hicolor/scalable/apps/hardinfo2.svg
%{_mandir}/man1/hardinfo2.1*
