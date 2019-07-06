%define debug_package %{nil}

%define major 4
%define libname %mklibname ebml %{major}
%define devname %mklibname ebml -d

Summary:	Extensible Binary Meta Language Library
Name:		libebml
Version:	1.3.9
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.matroska.org/
Source0:	http://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.xz
BuildRequires:	cmake

%description
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{libname}
Summary:	Extensible Binary Meta Language shared Library
Group:		System/Libraries

%description -n %{libname}
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{devname}
Group:		Development/C++
Summary:	Extensible Binary Meta Language Library headers and static library
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the C++ headers and the static library needed
for development with EBML.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make_build

%install
%make_install -C build

rm -f %{buildroot}%{_libdir}/*.a

# To avoid unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/lib*.so.%{major}*

%files -n %{libname}
%{_libdir}/libebml.so.%{major}*

%files -n %{devname}
%doc LICENSE*
%{_includedir}/ebml
%{_libdir}/libebml.so
%{_libdir}/cmake/ebml/
%{_libdir}/pkgconfig/*.pc
