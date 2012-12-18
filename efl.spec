Name:           efl
Version:        1.7.99
Release:        1.svn81177%{?dist}
License:        BSD-2-Clause and LGPL-2.1 and Zlib
Summary:        Enlightenment Foundation Libraries - set of libraries used (not only) by E17
Url:            http://www.enlightenment.org/
Group:          System Environment/Libraries
Source:         %{name}-%{version}.svn81177.tar.xz
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

%description
EFL is library collection providing various functinality used (not only)
by Enlightenment 17, terminology, Tizen mobile platform and much more.

%package devel
Summary:        Headers, pkgconfig files and other files for development with EFL
Group:          System Environment/Libraries

Requires:       %{name} = %{version}
Requires:       libecore1 = %{version}
Requires:       libeet1 = %{version}
Requires:       libeina1 = %{version}
Requires:       libeio1 = %{version}
Requires:       libembryo1 = %{version}
Requires:       libeo1 = %{version}
Requires:       libevas1 = %{version}
Provides:       ecore-devel = %{version}
Provides:       eina-devel = %{version}
Provides:       eio-devel = %{version}
Provides:       eet-devel = %{version}
Provides:       embryo-devel = %{version}
Provides:       eo-devel = %{version}
Provides:       evas-devel = %{version}
Obsoletes:      ecore-devel < %{version}
Obsoletes:      eina-devel < %{version}
Obsoletes:      eio-devel < %{version}
Obsoletes:      eet-devel < %{version}
Obsoletes:      embryo-devel < %{version}
Obsoletes:      eo-devel < %{version}
Obsoletes:      evas-devel < %{version}

%description devel
Headers, pkgconfig files and other files needed for development with EFL.

%package -n libecore1
Summary:        Ecore, part of EFL
Group:          System Environment/Libraries
License:        BSD-2-Clause

%description -n libecore1
Ecore is a clean and tiny event loop library with many modules to do lots of
convenient things for a programmer, to save time and effort.

%package -n libeet1
Summary:        Eet, part of EFL
Group:          System Environment/Libraries
License:        BSD-2-Clause

%description -n libeet1
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

%package -n libeina1
License:        LGPL-2.1
Summary:        Eina, part of EFL
Group:          System Environment/Libraries

%description -n libeina1
Eina is library handling various data types.

%package -n libeio1
License:        LGPL-2.1
Summary:        Eio, part of EFL
Group:          System Environment/Libraries

%description -n libeio1
Extension of ecore for parallel I/O operations. Part of Enlightenment Foundation Libraries.

%package -n libembryo1
License:        BSD-2-Clause and Zlib
Summary:        Embryo, part of EFL
Group:          System Environment/Libraries

%description -n libembryo1
Embryo is a tiny library designed to interpret limited small programs compiled
by the included compiler, embryo_cc. It is mostly a cleaned up and smaller
version of the original Small abstract machine. The compiler is mostly
untouched.

%package -n libeo1
License:        BSD-2-Clause
Summary:        Eo, part of EFL
Group:          System Environment/Libraries

%description -n libeo1
Eo is library providing basic E object in OOP way of programming.

%package -n libevas1
License:        BSD-2-Clause
Summary:        Evas, part of EFL
Group:          System Environment/Libraries

%description -n libevas1
Evas is a clean display canvas API that implements a scene graph, not an
immediate-mode rendering target, is cross-platform, for several target display
systems that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects and much more.

%prep
%setup -q -n %{name}-%{version}.svn81177

%build
autoreconf -ifv

%configure \
    --disable-static \
    --disable-silent-rules \
    --disable-tslib \
    --enable-harfbuzz \
    --enable-fb \

make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find %{buildroot}%{_libdir} -name '*.la' -exec rm -v {} \;
%find_lang efl

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n libecore1 -p /sbin/ldconfig
%postun -n libecore1 -p /sbin/ldconfig

%post -n libeet1 -p /sbin/ldconfig
%postun -n libeet1 -p /sbin/ldconfig

%post -n libeina1 -p /sbin/ldconfig
%postun -n libeina1 -p /sbin/ldconfig

%post -n libeio1 -p /sbin/ldconfig
%postun -n libeio1 -p /sbin/ldconfig

%post -n libembryo1 -p /sbin/ldconfig
%postun -n libembryo1 -p /sbin/ldconfig

%post -n libeo1 -p /sbin/ldconfig
%postun -n libeo1 -p /sbin/ldconfig

%post -n libevas1 -p /sbin/ldconfig
%postun -n libevas1 -p /sbin/ldconfig

%files -f efl.lang
%{_bindir}/*
%doc README COPYING AUTHORS
%{_libexecdir}/dummy_slave
%{_libexecdir}/evas_cserve2*
%{_libdir}/evas
%{_libdir}/ecore
%{_libdir}/ecore_evas
%{_datadir}/embryo
%{_datadir}/evas
%{_datadir}/eo

%files -n libecore1
%{_libdir}/libecore*.so.*

%files -n libeet1
%{_libdir}/libeet.so.*

%files -n libeina1
%{_libdir}/libeina.so.*

%files -n libeio1
%{_libdir}/libeio.so.*

%files -n libembryo1
%{_libdir}/libembryo.so.*

%files -n libeo1
%{_libdir}/libeo.so.*

%files -n libevas1
%{_libdir}/libevas.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_includedir}/ecore-1
%{_includedir}/eina-1
%{_includedir}/eio-1
%{_includedir}/eet-1
%{_includedir}/embryo-1
%{_includedir}/eo-1
%{_includedir}/evas-1

%changelog
* Sun Dec 16 2012 <vlevitan91@gmail.com>
- let there be efl
