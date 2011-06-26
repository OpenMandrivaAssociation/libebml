%define name    libebml
%define version 1.2.1
%define major 3
%define libname %mklibname ebml %{major}
%define develname %mklibname ebml -d

Summary:        Extensible Binary Meta Language Library
Name:           %name
Version:        %version
Release: %mkrel 1
License:        LGPLv2+
Group:		System/Libraries
URL:            http://www.matroska.org/
Source0:        http://dl.matroska.org/downloads/libebml/%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{libname}
Summary:        Extensible Binary Meta Language shared Library
Group: System/Libraries

%description -n %{libname}
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{develname}
Group: Development/C++
Summary: Extensible Binary Meta Language Library headers and static library
Provides: libebml-devel = %version
Requires: %{libname} = %version
Obsoletes: %{libname}-devel

%description -n %{develname}
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

This package contains the C++ headers and the static library needed
for development with EBML.

%prep
%setup -q

%build
cd make/linux
%make


%install
rm -rf %buildroot
cd make/linux
%makeinstall_std prefix=%buildroot/%_prefix libdir=%buildroot/%_libdir

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc LICENSE*
#%doc src/api/index.html
%{_includedir}/ebml
%{_libdir}/libebml.a
%{_libdir}/libebml.so


