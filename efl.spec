%global svn_revision svn81641

Name:           efl
Version:        1.7.4
Release:        1.%{svn_revision}%{?dist}
License:        BSD and LGPLv2+ and zlib
Summary:        Enlightenment Foundation Libraries - set of libraries used (not only) by E17
Url:            http://www.enlightenment.org/
Group:          System Environment/Libraries
Source:         %{name}-%{version}.%{svn_revision}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  glibc-devel
BuildRequires:  harfbuzz-devel >= 0.9.0
BuildRequires:  libjpeg-devel 
BuildRequires:  openssl-devel
BuildRequires:  SDL-devel
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel 
BuildRequires:  pixman-devel
BuildRequires:  libpng-devel >= 1.2.10
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXp-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libX11-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  zlib-devel
BuildRequires:  doxygen

Requires:       ecore = %{version}
Requires:       eet = %{version}
Requires:       libeina = %{version}
Requires:       eio = %{version}
Requires:       embryo = %{version}
Requires:       evas = %{version}
Requires:       eo = %{version}

%description
EFL is library collection providing various functinality used (not only)
by Enlightenment 17, terminology, Tizen mobile platform and much more.

%package devel
Summary:        Headers, pkgconfig files and other files for development with EFL
Group:          System Environment/Libraries

Requires:       %{name} = %{version}
Requires:       ecore = %{version}
Requires:       eet = %{version}
Requires:       libeina = %{version}
Requires:       eio = %{version}
Requires:       embryo = %{version}
Requires:       evas = %{version}
Requires:       eo = %{version}
Requires:       ecore-devel = %{version}
Requires:       libeina-devel = %{version}
Requires:       eet-devel = %{version}
Requires:       evas-devel = %{version}

%description devel
Headers, pkgconfig files and other files needed for development with EFL.

%package -n ecore
Summary:        Ecore, part of EFL
Group:          System Environment/Libraries
License:        BSD
Requires:       libeina = %{version}
Requires:       evas = %{version}

%description -n ecore
Ecore is a clean and tiny event loop library with many modules to do lots of
convenient things for a programmer, to save time and effort.

%package -n ecore-devel
Summary:        Files needed for development with Ecore
Group:          System Environment/Libraries
Requires:       ecore = %{version}
Requires:       eet-devel = %{version}
Requires:       evas-devel = %{version}
Requires:       libeina-devel = %{version}


%description -n ecore-devel
Files needed for development with Ecore

%package -n eet
Summary:        Eet, part of EFL
Group:          System Environment/Libraries
License:        BSD
Requires:       libeina = %{version}

%description -n eet
Eet is a tiny library designed to write an arbitrary set of chunks of
data to a file and optionally compress each chunk (very much like a
zip file) and allow fast random-access reading of the file later
on. It does not do zip as a zip itself has more complexity than is
needed, and it was much simpler to implement this once here.

It also can encode and decode data structures in memory, as well as
image data for saving to eet files or sending across the network to
other machines, or just writing to arbitrary files on the system. All
data is encoded in a platform independent way and can be written and
read by any architecture.

%package -n eet-devel
Summary:        Files needed for development with eet
Group:          System Environment/Libraries
Requires:       eet = %{version}
Requires:       libeina-devel = %{version}

%description -n eet-devel
Files needed for development with eet

%package -n libeina
Summary:        Eina, part of EFL
Group:          System Environment/Libraries
License:        LGPLv2+

%description -n libeina
Eina is library handling various data types.

%package -n libeina-devel
Summary:        Files needed for development with eina
Group:          System Environment/Libraries
Requires:       libeina = %{version}

%description -n libeina-devel
Files needed for development with eina

%package -n eio
Summary:        Eio, part of EFL
Group:          System Environment/Libraries
License:        LGPLv2+

%description -n eio
Extension of ecore for parallel I/O operations. 
Part of Enlightenment Foundation Libraries.

%package -n embryo
Summary:        Embryo, part of EFL
Group:          System Environment/Libraries
License:        BSD and zlib

%description -n embryo
Embryo is a tiny library designed to interpret limited small programs compiled
by the included compiler, embryo_cc. It is mostly a cleaned up and smaller
version of the original Small abstract machine. The compiler is mostly
untouched.

%package -n eo
License:        BSD
Summary:        Eo, part of EFL
Group:          System Environment/Libraries

%description -n eo
Eo is library providing basic E object in OOP way of programming.

%package -n evas
Summary:        Evas, part of EFL
Group:          System Environment/Libraries
License:        BSD
Requires:       eet = %{version}
Requires:       libeina = %{version}

%description -n evas
Evas is a clean display canvas API that implements a scene graph, not an
immediate-mode rendering target, is cross-platform, for several target display
systems that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects and much more.

%package -n evas-devel
Summary:        Files needed for development with evas
Group:          System Environment/Libraries
Requires:       evas = %{version}
Requires:       libeina-devel = %{version}
Requires:       eet-devel = %{version}

%description -n evas-devel
Files needed for development with evas

%package -n libevas1
License:        BSD
Summary:        Evas, part of EFL
Group:          System Environment/Libraries

%description -n libevas1
Evas is a clean display canvas API that implements a scene graph, not an
immediate-mode rendering target, is cross-platform, for several target display
systems that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects and much more.

%prep
%setup -q -n %{name}-%{version}.%{svn_revision}

%build
autoreconf -ifv

%configure \
    --disable-static \
    --disable-silent-rules \
    --disable-tslib \
    --enable-harfbuzz \
    --enable-fb \
    --enable-pixman \
    --enable-pixman-font \
    --enable-pixman-rect \
    --enable-pixman-line \
    --enable-pixman-poly \
    --enable-pixman-image \
    --enable-sdl \
    

make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find %{buildroot}%{_libdir} -name '*.la' -exec rm -v {} \;
%find_lang efl

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n ecore -p /sbin/ldconfig
%postun -n ecore -p /sbin/ldconfig

%post -n eet -p /sbin/ldconfig
%postun -n eet -p /sbin/ldconfig

%post -n libeina -p /sbin/ldconfig
%postun -n libeina -p /sbin/ldconfig

%post -n eio -p /sbin/ldconfig
%postun -n eio -p /sbin/ldconfig

%post -n embryo -p /sbin/ldconfig
%postun -n embryo -p /sbin/ldconfig

%post -n eo -p /sbin/ldconfig
%postun -n eo -p /sbin/ldconfig

%post -n evas -p /sbin/ldconfig
%postun -n evas -p /sbin/ldconfig

%files -f efl.lang
%doc README COPYING AUTHORS

%files -n ecore
%{_libdir}/ecore
%{_libdir}/ecore_evas
%{_libdir}/libecore*.so.*

%files -n eet
%{_libdir}/libeet.so.*
%{_bindir}/eet

%files -n libeina
%{_bindir}/eina-bench-cmp
%{_libdir}/libeina.so.*

%files -n eio
%{_libdir}/libeio.so.*

%files -n embryo
%{_bindir}/embryo_cc
%{_libdir}/libembryo.so.*

%files -n eo
%{_libdir}/libeo.so.*

%files -n evas
%{_bindir}/evas*
%{_libdir}/libevas.so.*
%{_libdir}/evas

%files -n eo
%{_libdir}/libeo.so.*
%{_datadir}/eo

%files -n ecore-devel
%{_libdir}/libecore*.so
%{_libdir}/pkgconfig/ecore*
%{_includedir}/ecore-1

%files -n eet-devel
%{_libdir}/libeet*.so
%{_libdir}/pkgconfig/eet*
%{_includedir}/eet-1

%files -n libeina-devel
%{_libdir}/libeina*.so
%{_libdir}/pkgconfig/eina*
%{_includedir}/eina-1

%files -n evas-devel
%{_libdir}/libevas*.so
%{_libdir}/pkgconfig/evas*
%{_includedir}/evas-1
%{_datadir}/evas
%{_libexecdir}/evas_cserve2*
%{_libexecdir}/dummy_slave

%files devel
%{_libdir}/libembryo*.so
%{_libdir}/pkgconfig/embryo*
%{_includedir}/embryo-1
%{_datadir}/embryo
%{_libdir}/libeo.so
%{_includedir}/eo-1
%{_libdir}/pkgconfig/eo*
%{_libdir}/libeio*.so
%{_libdir}/pkgconfig/eio*
%{_includedir}/eio-1

%changelog
* Sat Dec 22 2012 <vlevitan91@gmail.com> - 1.7.4-1.svn81641
- Update to release version
* Thu Dec 20 2012 <vlevitan91@gmail.com> - 0.7.99-1.svn81177
- Remake spec to fedora standart
* Wed Dec 19 2012 <vlevitan91@gmail.com> - 0.7.99-1.svn81177
- Add support pixman and SDL
* Sun Dec 16 2012 <vlevitan91@gmail.com> - 0.7.99-1.svn81177
- let there be efl
